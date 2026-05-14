from data import empresas_config
from flask import request, redirect, url_for, session, jsonify
from data import contactos_tic
from utils import (
    cargar_noticias,
    guardar_noticias,
    get_saludo,
    get_context,
    login_required,
    role_required,
    filtrar_noticias,
    guardar_comentarios,
    obtener_comentarios,
)

@login_required
def dashboard():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()

    rol = session.get("rol")
    
    logos_transformados = []
    for logo in logos:
        nombre_real = empresa
        if rol == "admin" and empresa == "Organizacion GYJ":
            for nombre_emp, conf in empresas_config.items():
                if nombre_emp != "Organizacion GYJ" and logo in conf.get("logos", []):
                    nombre_real = nombre_emp
                    break
        
        logos_transformados.append({
            "nombre": nombre_real,
            "url": logo
        })

    noticias_filtradas = filtrar_noticias(data.get("general", []), usuario, rol)

    return jsonify({
        "status": "success",
        "usuario": usuario,
        "empresa": empresa,
        "rol": rol,
        "saludo": get_saludo(),
        "noticias": noticias_filtradas,
        "logos": logos_transformados,
        "contactos_tic": contactos_tic
    })


@role_required(["admin"])
@login_required
def crear_noticia():
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    
    if request.method == "POST":
        if request.is_json:
            payload = request.get_json(silent=True) or {}
            seccion = payload.get("seccion")
            titulo = payload.get("titulo")
            texto = payload.get("texto")
            roles_raw = payload.get("roles", "")
            usuarios_raw = payload.get("usuarios", "")
            fecha_expiracion = payload.get("fecha_expiracion", "").strip()
        else:
            seccion = request.form.get("seccion")
            titulo = request.form.get("titulo")
            texto = request.form.get("texto")
            roles_raw = request.form.get("roles", "")
            usuarios_raw = request.form.get("usuarios", "")
            fecha_expiracion = request.form.get("fecha_expiracion", "").strip()

        roles = [r.strip().lower() for r in roles_raw.split(",") if r.strip()]
        usuarios = [u.strip().lower() for u in usuarios_raw.split(",") if u.strip()]

        data = cargar_noticias()

        nueva = {
            "titulo": titulo,
            "texto": texto,
            "roles": roles,
            "usuarios": usuarios,
            "fecha_expiracion": fecha_expiracion if fecha_expiracion else None
        }

        if seccion in data:
            data[seccion].append(nueva)
            guardar_noticias(data)
            return jsonify({"status": "success", "message": "Noticia publicada"}), 200

        return jsonify({"status": "error", "message": "Sección inválida"}), 400

    return jsonify({
        "status": "ready",
        "message": "Envía POST JSON para publicar noticia",
        "empresa": empresa,
        "usuario": usuario,
        "rol": rol,
        "secciones_disponibles": ["general", "tic", "contabilidad", "contraloria", "abastecimiento", "indicadores", "comercio", "tesoreria"]
    })


@login_required
def api_comentarios():
    if request.method == "POST":
        datos_recibidos = request.get_json(silent=True) or {}
        usuario_real, empresa_real, _ = get_context()
        datos_finales = {
            "nombre_usuario": usuario_real,
            "email": session.get("usuario"),
            "comentario": datos_recibidos.get("comentario"),
            "empresa": empresa_real,
            "fecha": datos_recibidos.get("fecha")
        }

        exito, error_msg = guardar_comentarios(datos_finales)
        if exito:
            return jsonify({"status": "success", "message": "Comentario registrado"}), 200
        return jsonify({"status": "error", "message": "No se pudo guardar el comentario", "detail": error_msg}), 500

    comentarios = obtener_comentarios()
    return jsonify({"status": "success", "comments": comentarios}), 200


@login_required
def guardar_comentario():
    datos_recibidos = request.get_json(silent=True) or {}

    usuario_real, empresa_real, _ = get_context()
    datos_finales = {
        "nombre_usuario": usuario_real,
        "email": session.get("usuario"),
        "comentario": datos_recibidos.get("comentario"),
        "empresa": empresa_real,
        "fecha": datos_recibidos.get("fecha")
    }

    exito, error_msg = guardar_comentarios(datos_finales)
    if exito:
        return jsonify({"status": "success", "message": "Comentario registrado"}), 200
    return jsonify({"status": "error", "message": "No se pudo guardar el comentario", "detail": error_msg}), 500


@login_required
def empresa(nombre):

    usuario, empresa_ctx, logos_ctx = get_context()
    config = empresas_config.get(nombre, {})
    informes = config.get("informes", [])

    return jsonify({
        "status": "success",
        "usuario": usuario,
        "empresa_actual": empresa_ctx,
        "nombre_empresa_informe": nombre,
        "informes": informes,
        "logos": logos_ctx
    })