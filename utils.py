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

def _noticia_vigente(n):
    """Retorna True si la noticia no ha vencido o no tiene fecha de expiración."""
    fecha_exp = n.get("fecha_expiracion")
    if not fecha_exp:
        return True
    try:
        zona = pytz.timezone("America/Bogota")
        hoy = datetime.now(zona).date()
        vence = datetime.strptime(fecha_exp, "%Y-%m-%d").date()
        return hoy <= vence
    except ValueError:
        return True  # Si el formato es incorrecto, no ocultamos la noticia

def filtrar_noticias(noticias_lista, usuario_actual, rol_actual):
    if not noticias_lista:
        return []

    # Primero descartar noticias vencidas (para todos los roles)
    vigentes = [n for n in noticias_lista if _noticia_vigente(n)]

    # El administrador ve todas las vigentes
    if rol_actual == "admin":
        return vigentes
    
    filtradas = []
    for n in vigentes:
        roles_permitidos = n.get("roles", [])
        usuarios_permitidos = n.get("usuarios", [])
        
        # 1. Verificación por usuario específico
        if usuario_actual in usuarios_permitidos:
            filtradas.append(n)
            continue
            
        # 2. Verificación por rol específico
        if rol_actual in roles_permitidos:
            filtradas.append(n)
            continue

        # 3. Lógica para noticias "Generales" (sin restricciones en el JSON)
        if not roles_permitidos and not usuarios_permitidos:
            # Si no hay restricciones, solo los gerentes (y admin) las ven
            if rol_actual == "gerente":
                filtradas.append(n)
            
    return filtradas
