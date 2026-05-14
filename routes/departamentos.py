from flask import request, session, jsonify
from utils import cargar_noticias, get_saludo, get_context, login_required, filtrar_noticias


def _build_section_response(section_name, noticias):
    return {
        "status": "success",
        "section": section_name,
        "usuario": session.get("usuario"),
        "empresa": get_context()[1],
        "saludo": get_saludo(),
        "noticias": noticias
    }


@login_required
def contabilidad():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("contabilidad", []), usuario, rol)
    return jsonify({
        "status": "success",
        "section": "contabilidad",
        "usuario": usuario,
        "empresa": empresa,
        "saludo": get_saludo(),
        "logos": logos,
        "noticias": noticias_filtradas
    })


@login_required
def contraloria():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("contraloria", []), usuario, rol)
    return jsonify({
        "status": "success",
        "section": "contraloria",
        "usuario": usuario,
        "empresa": empresa,
        "saludo": get_saludo(),
        "logos": logos,
        "noticias": noticias_filtradas
    })


@login_required
def abastecimiento():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("abastecimiento", []), usuario, rol)
    return jsonify({
        "status": "success",
        "section": "abastecimiento",
        "usuario": usuario,
        "empresa": empresa,
        "saludo": get_saludo(),
        "logos": logos,
        "noticias": noticias_filtradas
    })


@login_required
def indicadores():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    seccion = request.args.get("seccion")
    noticias_filtradas = filtrar_noticias(data.get("indicadores", []), usuario, rol)
    return jsonify({
        "status": "success",
        "section": seccion or "indicadores",
        "usuario": usuario,
        "empresa": empresa,
        "saludo": get_saludo(),
        "logos": logos,
        "noticias": noticias_filtradas
    })


@login_required
def tic():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("tic", []), usuario, rol)
    return jsonify({
        "status": "success",
        "section": "tic",
        "usuario": usuario,
        "empresa": empresa,
        "saludo": get_saludo(),
        "logos": logos,
        "noticias": noticias_filtradas
    })


@login_required
def comercio():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("comercio", []), usuario, rol)
    return jsonify({
        "status": "success",
        "section": "comercio",
        "usuario": usuario,
        "empresa": empresa,
        "saludo": get_saludo(),
        "logos": logos,
        "noticias": noticias_filtradas
    })


@login_required
def tesoreria():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("tesoreria", []), usuario, rol)
    return jsonify({
        "status": "success",
        "section": "tesoreria",
        "usuario": usuario,
        "empresa": empresa,
        "saludo": get_saludo(),
        "logos": logos,
        "noticias": noticias_filtradas
    })
