from data import empresas_config
from flask import render_template, request, redirect, url_for, session
from data import contactos_tic
from utils import (
    cargar_noticias,
    guardar_noticias,
    get_saludo,
    get_context,
    login_required,
    role_required,
    filtrar_noticias
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

    return render_template(
        "dashboard.html",
        usuario=usuario,
        empresa=empresa,
        rol=rol,
        saludo=get_saludo(),
        noticias=noticias_filtradas,
        logos=logos_transformados,
        contactos_tic=contactos_tic
    )


@role_required(["admin"])
@login_required
def crear_noticia():
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    
    if request.method == "POST":
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
        return redirect(url_for("dashboard"))

    return render_template("crear_noticia.html", empresa=empresa, logos=logos, rol=rol)


@login_required
def empresa(nombre):

    usuario, empresa_ctx, logos_ctx = get_context()
    config = empresas_config.get(nombre, {})
    informes = config.get("informes", [])

    return render_template(
        "empresa.html",
        empresa=empresa_ctx,
        nombre_empresa_informe=nombre,
        informes=informes,
        logos=logos_ctx
    )