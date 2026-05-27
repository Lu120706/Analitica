from flask import session, redirect, url_for
from datetime import datetime
from functools import wraps
import pytz
import json
import os
import sqlite3
from data import usuarios, contactos_tic, empresas_config

DEFAULT_NOTICIAS_STRUCTURE = {
    "general": [],
    "tic": [],
    "contabilidad": [],
    "contraloria": [],
    "abastecimiento": [],
    "indicadores": [],
    "comercio": [],
    "tesoreria": []
}

def cargar_noticias():
    try:
        with open("data/noticias.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            if not isinstance(data, dict):
                return DEFAULT_NOTICIAS_STRUCTURE.copy()
            # Aseguramos que siempre existan las secciones necesarias.
            for key, value in DEFAULT_NOTICIAS_STRUCTURE.items():
                data.setdefault(key, [])
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return DEFAULT_NOTICIAS_STRUCTURE.copy()

def guardar_noticias(data):
    os.makedirs("data", exist_ok=True)
    with open("data/noticias.json", "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)

def get_saludo():
    zona = pytz.timezone("America/Bogota")
    hora = datetime.now(zona).hour
    if hora < 12:
        return "Buenos días"
    elif hora < 18:
        return "Buenas tardes"
    return "Buenas noches"

def get_context():
    usuario = session.get("usuario")
    if not usuario:
        return None, None, []
    
    empresa = session.get("empresa", "Organizacion GYJ")
    config = empresas_config.get(empresa)
    
    if not config or not isinstance(config, dict):
        config = empresas_config.get("Organizacion GYJ", {})
        
    logos = config.get("logos", [])
    return usuario, empresa, logos

def get_usuario_nombre():
    usuario = session.get("usuario")
    if not usuario:
        return None
    return usuarios.get(usuario, {}).get("nombre", usuario)

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("usuario"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

def role_required(roles_permitidos):
    def wrapper(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if "usuario" not in session:
                return redirect(url_for("login"))
            rol = session.get("rol")
            if rol not in roles_permitidos:
                return "No autorizado", 403
            return func(*args, **kwargs)
        return decorated_function
    return wrapper

def _noticia_vigente(n):
    fecha_exp = n.get("fecha_expiracion")
    if not fecha_exp:
        return True
    try:
        zona = pytz.timezone("America/Bogota")
        hoy = datetime.now(zona).date()
        vence = datetime.strptime(fecha_exp, "%Y-%m-%d").date()
        return hoy <= vence
    except (ValueError, TypeError):
        return True

def filtrar_noticias(noticias_lista, usuario_actual, rol_actual):
    if not noticias_lista:
        return []
    
    vigentes = [n for n in noticias_lista if _noticia_vigente(n)]
    
    if rol_actual == "admin":
        return vigentes
    
    filtradas = []
    for n in vigentes:
        roles_p = n.get("roles", [])
        usuarios_p = n.get("usuarios", [])
        
        # Si no hay restricciones, todos ven (o solo gerentes según tu regla)
        if not roles_p and not usuarios_p:
            filtradas.append(n)
            continue
            
        if usuario_actual in usuarios_p or rol_actual in roles_p:
            filtradas.append(n)
            
    return filtradas

DB_PATH = os.path.join("data", "comentarios.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Aseguramos tabla comentarios con la columna 'comentario' (nueva)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comentarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_usuario TEXT,
                email TEXT,
                comentario TEXT,
                empresa TEXT,
                fecha_envio TEXT
            )
        """)

        # Aseguramos tabla de respuestas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS respuestas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comentario_id INTEGER,
                respuesta TEXT,
                fecha_respuesta TEXT,
                FOREIGN KEY (comentario_id) REFERENCES comentarios(id)
            )
        """)

        # Migración: si la tabla existente tiene la columna antigua 'comment', la copiamos a 'comentario'
        cols = [row[1] for row in cursor.execute("PRAGMA table_info('comentarios')").fetchall()]
        if 'comentario' not in cols:
            # Si existe la columna antigua 'comment', la migramos
            if 'comment' in cols:
                cursor.execute("ALTER TABLE comentarios ADD COLUMN comentario TEXT")
                cursor.execute("UPDATE comentarios SET comentario = comment WHERE comentario IS NULL")
            else:
                # Ninguna columna existe (caso raro), añadimos la columna 'comentario'
                cursor.execute("ALTER TABLE comentarios ADD COLUMN comentario TEXT")

        conn.commit()

def guardar_comentarios(datos):
    try:
        init_db()
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "INSERT INTO comentarios (nombre_usuario, email, comentario, empresa, fecha_envio) VALUES (?, ?, ?, ?, ?)",
                (
                    datos.get("nombre_usuario"),
                    datos.get("email"),
                    datos.get("comentario"),
                    datos.get("empresa"),
                    datos.get("fecha")
                )
            )
            conn.commit()
        return True, None
    except Exception as e:
        import traceback
        traceback.print_exc()
        return False, f"Error al guardar: {str(e)}"

def obtener_comentarios():
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute("""
            SELECT *
            FROM comentarios
            ORDER BY id DESC
        """)
        comentarios = [dict(row) for row in cursor.fetchall()]

        for comentario in comentarios:
            if "comentario" not in comentario or comentario.get("comentario") is None:
                comentario["comentario"] = comentario.get("comment", "")

        return comentarios

def guardar_respuesta(comentario_id, respuesta):
    """Guarda la respuesta del admin a un comentario."""
    try:
        init_db()

        fecha_actual = datetime.now(
            pytz.timezone('America/Bogota')
        ).strftime('%Y-%m-%d %H:%M:%S')

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id FROM respuestas WHERE comentario_id = ?",
                (comentario_id,)
            )

            existe = cursor.fetchone()
            if existe:
                cursor.execute(
                    """
                    UPDATE respuestas
                    SET respuesta = ?, fecha_respuesta = ?
                    WHERE comentario_id = ?
                    """,
                    (respuesta, fecha_actual, comentario_id)
                )
            else:
                cursor.execute(
                    """
                    INSERT INTO respuestas
                    (comentario_id, respuesta, fecha_respuesta)
                    VALUES (?, ?, ?)
                    """,
                    (comentario_id, respuesta, fecha_actual)
                )
            conn.commit()
        return True, None
    except Exception as e:
        import traceback
        traceback.print_exc()
        return False, f"Error al guardar respuesta: {str(e)}"

def obtener_respuesta(comentario_id):
    """Obtiene la respuesta de un comentario si existe."""
    try:
        init_db()
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.execute("SELECT respuesta, fecha_respuesta FROM respuestas WHERE comentario_id = ? ORDER BY id DESC LIMIT 1", (comentario_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
    except Exception as e:
        return None