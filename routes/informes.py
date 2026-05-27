from flask import render_template, session
from utils import get_context, get_usuario_nombre, login_required

@login_required
def informe_ventas():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    contexto = {
        "usuario": usuario,
        "nombre_usuario": nombre_usuario,
        "empresa": empresa,
        "logos": logos,
        "titulo": "Informe de Ventas",
        "rol": session.get("rol")
    }
    return render_template('informe_ventas.html', data=contexto)

@login_required
def balance_lineas():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    contexto = {
        "usuario": usuario,
        "nombre_usuario": nombre_usuario,
        "empresa": empresa,
        "logos": logos,
        "titulo": "Balance por Líneas",
        "rol": session.get("rol")
    }
    return render_template('balance_lineas.html', data=contexto)

@login_required
def estado_financiero():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    contexto = {
        "usuario": usuario,
        "nombre_usuario": nombre_usuario,
        "empresa": empresa,
        "logos": logos,
        "titulo": "Estado Financiero",
        "rol": session.get("rol")
    }
    return render_template('informe_financiero.html', data=contexto)