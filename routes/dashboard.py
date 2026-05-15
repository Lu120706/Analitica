from flask import request, redirect, url_for, session, jsonify, render_template
from data import empresas_config, contactos_tic
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
def dashboard_view():
    data_noticias = cargar_noticias()
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
        logos_transformados.append({"nombre": nombre_real, "url": logo})

    noticias_filtradas = filtrar_noticias(data_noticias.get("general", []), usuario, rol)

    contexto = {
        "status": "success",
        "usuario": usuario,
        "empresa": empresa,
        "rol": rol,
        "saludo": get_saludo(),
        "noticias": noticias_filtradas,
        "logos": logos_transformados,
        "contactos_tic": contactos_tic
    }
    
    return render_template('dashboard.html', data=contexto)

@login_required
def dashboard_api():
    usuario, empresa, _ = get_context()
    return jsonify({
        "status": "success", 
        "usuario": usuario, 
        "empresa": empresa
    })


@role_required(["admin"])
@login_required
def crear_noticia():
    """Procesa la creación de noticias. Retorna JSON o renderiza el formulario."""
    if request.method == "POST":
        payload = request.get_json(silent=True) if request.is_json else request.form
        seccion = payload.get("seccion")
        titulo = payload.get("titulo")
        texto = payload.get("texto")
        roles_raw = payload.get("roles", "")
        usuarios_raw = payload.get("usuarios", "")
        fecha_expiracion = payload.get("fecha_expiracion", "").strip()

        roles = [r.strip().lower() for r in roles_raw.split(",") if r.strip()]
        usuarios = [u.strip().lower() for u in usuarios_raw.split(",") if u.strip()]

        data_noticias = cargar_noticias()
        nueva = {
            "titulo": titulo,
            "texto": texto,
            "roles": roles,
            "usuarios": usuarios,
            "fecha_expiracion": fecha_expiracion if fecha_expiracion else None
        }

        if seccion in data_noticias:
            data_noticias[seccion].append(nueva)
            guardar_noticias(data_noticias)
            if request.is_json:
                return jsonify({"status": "success", "message": "Noticia publicada"}), 200
            else:
                from flask import flash
                flash("Noticia publicada exitosamente", "success")
                return redirect(url_for('crear_noticia'))

        if request.is_json:
            return jsonify({"status": "error", "message": "Sección inválida"}), 400
        else:
            from flask import flash
            flash("Sección inválida", "danger")
            return redirect(url_for('crear_noticia'))

    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario,
        "empresa": empresa,
        "logos": logos,
        "saludo": get_saludo(),
        "rol": session.get("rol")
    }
    return render_template('crear_noticia.html', data=contexto)

@login_required
def api_comentarios():
    """Ruta unificada para el sistema de soporte (POST para enviar, GET para listar)."""
    usuario_real, empresa_real, _ = get_context()

    if request.method == "POST":
        datos_recibidos = request.get_json(silent=True) or {}
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
        return jsonify({"status": "error", "message": error_msg}), 500

    comentarios = obtener_comentarios()
    return jsonify({"status": "success", "comments": comentarios}), 200

@login_required
def empresa(nombre):
    """Renderiza la página de informes específicos de una empresa."""
    usuario, empresa_ctx, logos_ctx = get_context()
    
    # Buscamos la configuración de la empresa seleccionada
    from data import empresas_config # Asegurar la importación
    config = empresas_config.get(nombre, {})
    informes = config.get("informes", [])
    contexto = {
        "usuario": usuario,
        "empresa": empresa_ctx,
        "saludo": get_saludo(),
        "nombre_empresa_informe": nombre,
        "informes": informes,
        "logos": logos_ctx
    }

    return render_template('empresa.html', data=contexto)