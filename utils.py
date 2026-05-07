from flask import session, redirect, url_for
from datetime import datetime
from functools import wraps
import pytz
import json
from data import usuarios, contactos_tic, empresas_config

def cargar_noticias():
    with open("data/noticias.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def guardar_noticias(data):
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
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return wrapper

def role_required(roles_permitidos):
    def wrapper(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if "usuario" not in session:
                return redirect(url_for("auth.login"))
            rol = session.get("rol")
            if rol not in roles_permitidos:
                return "No autorizado", 403
            return func(*args, **kwargs)
        return decorated_function
    return wrapper
