from flask import session, redirect, url_for
from datetime import datetime
from functools import wraps
import pytz
import json
import os
import sqlite3
from data import usuarios, contactos_tic, empresas_config

DEFAULT_NOTICIAS_STRUCTURE = {
    "general": [], "tic": [], "contabilidad": [], "contraloria": [],
    "abastecimiento": [], "indicadores": [], "comercio": [], "tesoreria": [], "recursos_humanos": []
}

def cargar_noticias():
    try:
        with open("data/noticias.json", "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            if not isinstance(data, dict): return DEFAULT_NOTICIAS_STRUCTURE.copy()
            for key in DEFAULT_NOTICIAS_STRUCTURE: data.setdefault(key, [])
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
    if hora < 12: return "Buenos días"
    elif hora < 18: return "Buenas tardes"
    return "Buenas noches"

def get_tenant_data():
    tenant_id = session.get("tenant_id", "Organizacion GYJ")
    config = empresas_config.get(tenant_id, empresas_config.get("Organizacion GYJ", {}))
    return tenant_id, config.get("logos", [])

def get_context():
    usuario = session.get("usuario")
    if not usuario: return None, None, []
    tenant_id, logos = get_tenant_data()
    return usuario, tenant_id, logos

def get_usuario_nombre():
    usuario = session.get("usuario")
    return usuarios.get(usuario, {}).get("nombre", usuario) if usuario else None

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("usuario"): return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper

def role_required(roles_permitidos):
    def wrapper(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if "usuario" not in session: return redirect(url_for("login"))
            if session.get("rol") not in roles_permitidos: return "No autorizado", 403
            return func(*args, **kwargs)
        return decorated_function
    return wrapper

def _noticia_vigente(n):
    fecha_exp = n.get("fecha_expiracion")
    if not fecha_exp: return True
    try:
        vence = datetime.strptime(fecha_exp, "%Y-%m-%d").date()
        return datetime.now(pytz.timezone("America/Bogota")).date() <= vence
    except: return True

def filtrar_noticias(noticias_lista, usuario_actual, rol_actual):
    if not noticias_lista: return []
    vigentes = [n for n in noticias_lista if _noticia_vigente(n)]
    if rol_actual == "admin": return vigentes
    return [n for n in vigentes if not n.get("roles") and not n.get("usuarios") or usuario_actual in n.get("usuarios", []) or rol_actual in n.get("roles", [])]

DB_PATH = os.path.join("data", "comentarios.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS comentarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_usuario TEXT, email TEXT, comentario TEXT, empresa TEXT, fecha_envio TEXT, leido_admin INTEGER DEFAULT 0)")
        cursor.execute("CREATE TABLE IF NOT EXISTS respuestas (id INTEGER PRIMARY KEY AUTOINCREMENT, comentario_id INTEGER, respuesta TEXT, fecha_respuesta TEXT, leido_usuario INTEGER DEFAULT 0, FOREIGN KEY (comentario_id) REFERENCES comentarios(id))")
        for col, table in [('leido_admin', 'comentarios'), ('leido_usuario', 'respuestas')]:
            cols = [row[1] for row in cursor.execute(f"PRAGMA table_info('{table}')").fetchall()]
            if col not in cols: cursor.execute(f"ALTER TABLE {table} ADD COLUMN {col} INTEGER DEFAULT 0")
        conn.commit()

def guardar_comentarios(datos):
    try:
        init_db()
        tenant_id = session.get("tenant_id")
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("INSERT INTO comentarios (nombre_usuario, email, comentario, empresa, fecha_envio, leido_admin) VALUES (?, ?, ?, ?, ?, 0)", 
                         (datos.get("nombre_usuario"), datos.get("email"), datos.get("comentario"), tenant_id, datos.get("fecha")))
            conn.commit()
        return True, None
    except Exception as e: return False, str(e)

def obtener_comentarios():
    init_db()
    tenant_id = session.get("tenant_id")
    rol = session.get("rol")
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        if rol == "admin":
            query = "SELECT * FROM comentarios ORDER BY id DESC"
            return [dict(row) for row in conn.execute(query).fetchall()]
        else:
            query = "SELECT * FROM comentarios WHERE empresa = ? ORDER BY id DESC"
            return [dict(row) for row in conn.execute(query, (tenant_id,)).fetchall()]

def guardar_respuesta(comentario_id, respuesta):
    try:
        init_db()
        fecha = datetime.now(pytz.timezone('America/Bogota')).strftime('%Y-%m-%d %H:%M:%S')
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            existe = cursor.execute("SELECT id FROM respuestas WHERE comentario_id = ?", (comentario_id,)).fetchone()
            if existe: cursor.execute("UPDATE respuestas SET respuesta = ?, fecha_respuesta = ?, leido_usuario = 0 WHERE comentario_id = ?", (respuesta, fecha, comentario_id))
            else: cursor.execute("INSERT INTO respuestas (comentario_id, respuesta, fecha_respuesta, leido_usuario) VALUES (?, ?, ?, 0)", (comentario_id, respuesta, fecha))
            conn.commit()
        return True, None
    except Exception as e: return False, str(e)

def obtener_respuesta(comentario_id):
    try:
        init_db()
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute("SELECT respuesta, fecha_respuesta FROM respuestas WHERE comentario_id = ? ORDER BY id DESC LIMIT 1", (comentario_id,)).fetchone()
            return dict(row) if row else None
    except: return None
