from flask import render_template, request, session
from utils import cargar_noticias, get_saludo, get_context, login_required, filtrar_noticias

@login_required
def contabilidad():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("contabilidad", []), usuario, rol)
    return render_template(
        "contabilidad.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        noticias_contabilidad=noticias_filtradas,
        logos=logos
    )

@login_required
def contraloria():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("contraloria", []), usuario, rol)
    return render_template(
        "contraloria.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        noticias_contraloria=noticias_filtradas
    )

@login_required
def abastecimiento():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("abastecimiento", []), usuario, rol)
    return render_template(
        "abastecimiento.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        noticias_abastecimiento=noticias_filtradas
    )

@login_required
def indicadores():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    seccion = request.args.get("seccion")
    noticias_filtradas = filtrar_noticias(data.get("indicadores", []), usuario, rol)
    return render_template(
        "indicadores.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        seccion=seccion,
        noticias_indicadores=noticias_filtradas
    )

@login_required
def tic():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("tic", []), usuario, rol)
    return render_template(
        "tic.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        noticias_tic=noticias_filtradas
    )

@login_required
def comercio():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("comercio", []), usuario, rol)
    return render_template(
        "comercio.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        noticias_comercio=noticias_filtradas
    )

@login_required
def tesoreria():
    data = cargar_noticias()
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    noticias_filtradas = filtrar_noticias(data.get("tesoreria", []), usuario, rol)
    return render_template(
        "tesoreria.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        noticias_tesoreria=noticias_filtradas
    )
