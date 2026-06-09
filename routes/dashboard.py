from flask import request, redirect, url_for, session, jsonify, render_template, flash
from data import empresas_config, contactos_tic, informes_buscador
from utils import (
    cargar_noticias, guardar_noticias, get_saludo, get_context,
    get_usuario_nombre, login_required, role_required,
    filtrar_noticias, guardar_comentarios, obtener_comentarios,
    guardar_respuesta, obtener_respuesta, DB_PATH
)
import sqlite3

@login_required
def dashboard_view():
    data_noticias = cargar_noticias()
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
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
        "status": "success", "usuario": usuario, "nombre_usuario": nombre_usuario,
        "empresa": empresa, "rol": rol, "saludo": get_saludo(),
        "noticias": noticias_filtradas, "logos": logos_transformados,
        "contactos_tic": contactos_tic, "informes_buscador": informes_buscador
    }
    return render_template('dashboard.html', data=contexto)

@login_required
def dashboard_api():
    usuario, empresa, _ = get_context()
    return jsonify({"status": "success", "usuario": usuario, "empresa": empresa})

@role_required(["admin"])
@login_required
def crear_noticia():
    if request.method == "POST":
        payload = request.form
        seccion = payload.get("seccion")
        titulo = payload.get("titulo")
        texto = payload.get("texto")
        link = payload.get("link", "")
        fecha_exp = payload.get("fecha_expiracion", "")
        
        data_noticias = cargar_noticias()

        if seccion not in data_noticias:
            flash("Sección inválida", "danger")
            return redirect(url_for("crear_noticia"))

        data_noticias[seccion].append({
            "titulo": titulo,
            "texto": texto,
            "link": link,
            "roles": [],
            "usuarios": [],
            "fecha_expiracion": fecha_exp if fecha_exp else None
        })

        guardar_noticias(data_noticias)
        flash("Noticia publicada exitosamente", "success")

        return redirect(url_for("crear_noticia"))

    usuario, empresa, logos = get_context()

    return render_template(
        "crear_noticia.html",
        data={
            "usuario": usuario,
            "nombre_usuario": get_usuario_nombre(),
            "empresa": empresa,
            "logos": logos,
            "saludo": get_saludo(),
            "rol": session.get("rol")
        }
    )

@login_required
def api_comentarios():
    usuario_real, empresa_real, _ = get_context()
    if not usuario_real: return jsonify({"status": "error", "message": "Unauthorized"}), 401
    if request.method == "POST":
        datos = request.get_json(silent=True) or {}
        exito, msg = guardar_comentarios({
            "nombre_usuario": usuario_real, "email": session.get("usuario"),
            "comentario": datos.get("comentario", "").strip(),
            "empresa": empresa_real or "Sin empresa", "fecha": datos.get("fecha")
        })
        return jsonify({"status": "success" if exito else "error", "message": msg}), 200 if exito else 500
    
    comentarios = obtener_comentarios()
    rol = session.get("rol")
    if rol != "admin":
        comentarios = [c for c in comentarios if c['email'] == session.get("usuario")]
    for c in comentarios: c["respuesta"] = obtener_respuesta(c.get("id"))
    return jsonify({"status": "success", "comments": comentarios}), 200

@login_required
def api_notificaciones():
    usuario_email = session.get("usuario")
    rol = session.get("rol")
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        if rol == "admin":
            cursor = conn.execute("SELECT count(*) as count FROM comentarios WHERE leido_admin = 0")
        else:
            cursor = conn.execute("SELECT count(*) as count FROM respuestas r JOIN comentarios c ON r.comentario_id = c.id WHERE c.email = ? AND r.leido_usuario = 0", (usuario_email,))
        row = cursor.fetchone()
        return jsonify({"count": row['count'] if row else 0})

@role_required(["admin"])
@login_required
def api_marcar_leido_admin():
    datos = request.get_json(silent=True) or {}
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("UPDATE comentarios SET leido_admin = 1 WHERE id = ?", (datos.get("comentario_id"),))
    return jsonify({"status": "success"})

@login_required
def api_marcar_leido_usuario():
    datos = request.get_json(silent=True) or {}
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("UPDATE respuestas SET leido_usuario = 1 WHERE comentario_id = ?", (datos.get("comentario_id"),))
    return jsonify({"status": "success"})

@login_required
def empresa(nombre):
    usuario, empresa_ctx, logos_ctx = get_context()
    rol = session.get("rol")
    logos_transformados = []
    for logo in logos_ctx:
        nombre_real = empresa_ctx
        if rol == "admin" and empresa_ctx == "Organizacion GYJ":
            for nombre_emp, conf in empresas_config.items():
                if nombre_emp != "Organizacion GYJ" and logo in conf.get("logos", []):
                    nombre_real = nombre_emp
                    break
        logos_transformados.append({"nombre": nombre_real, "url": logo})
    config = empresas_config.get(nombre, {})
    return render_template('empresa.html', data={
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(), "empresa": empresa_ctx,
        "saludo": get_saludo(), "nombre_empresa_informe": nombre, "informes": config.get("informes", []),
        "logos": logos_transformados, "rol": rol
    })

@role_required(["admin"])
@login_required
def ver_comentarios():
    usuario, empresa, logos = get_context()
    comentarios = obtener_comentarios()
    for c in comentarios: c["respuesta"] = obtener_respuesta(c.get("id"))
    return render_template('comentarios_admin.html', data={
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(), "empresa": empresa,
        "saludo": get_saludo(), "comentarios": comentarios, "logos": logos, "rol": session.get("rol")
    })

@role_required(["admin"])
@login_required
def responder_comentario():
    datos = request.get_json(silent=True) or {}
    exito, msg = guardar_respuesta(datos.get("comentario_id"), datos.get("respuesta", "").strip())
    return jsonify({"status": "success" if exito else "error", "message": msg}), 200 if exito else 500
