from flask import session, redirect, url_for
from datetime import datetime
from functools import wraps
import pytz
import json
import os
import sqlite3
from data import usuarios, contactos_tic, empresas_config

def cargar_noticias():
    try:
        with open("data/noticias.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

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
        conn.execute("""
            CREATE TABLE IF NOT EXISTS comentarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_usuario TEXT,
                email TEXT,
                comment TEXT,
                empresa TEXT,
                fecha_envio TEXT
            )
        """)

def guardar_comentarios(datos):
    try:
        init_db()
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "INSERT INTO comentarios (nombre_usuario, email, comment, empresa, fecha_envio) VALUES (?, ?, ?, ?, ?)",
                (
                    datos.get("nombre_usuario"),
                    datos.get("email"),
                    datos.get("comentario"),
                    datos.get("empresa"),
                    datos.get("fecha")
                )
            )
        return True, None
    except Exception as e:
        return False, str(e)

def obtener_comentarios():
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute("SELECT * FROM comentarios ORDER BY id DESC")
        return [dict(row) for row in cursor.fetchall()]