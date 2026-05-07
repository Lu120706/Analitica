from flask import render_template, request, redirect, url_for, session
from data import contactos_tic
from utils import cargar_noticias, guardar_noticias, get_saludo, get_context, login_required, role_required

@login_required
def dashboard():
    noticias = cargar_noticias()
    usuario, empresa, logos = get_context()
    return render_template(
        "dashboard.html",
        usuario=usuario,
        empresa=empresa,
        rol=session.get("rol"),
        saludo=get_saludo(),
        noticias=noticias["tic"],
        logos=logos,
        contactos_tic=contactos_tic
    )

@role_required(["admin", "gerente"])
@login_required
def crear_noticia():
    if request.method == "POST":
        seccion = request.form.get("seccion")
        titulo = request.form.get("titulo")
        texto = request.form.get("texto")
        data = cargar_noticias()
        nueva = {"titulo": titulo, "texto": texto}
        if seccion in data:
            data[seccion].append(nueva)
        guardar_noticias(data)
        return redirect(url_for("dashboard"))
    return render_template("crear_noticia.html")
