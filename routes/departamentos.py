from flask import render_template, request, session
from utils import cargar_noticias, get_saludo, get_context, login_required

@login_required
def contabilidad():
    noticias = cargar_noticias()
    usuario, empresa, logos = get_context()
    return render_template(
        "contabilidad.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        noticias_contabilidad=noticias["contabilidad"],
        logos=logos
    )

@login_required
def contraloria():
    noticias = cargar_noticias()
    usuario, empresa, logos = get_context()
    return render_template(
        "contraloria.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        noticias_contraloria=noticias["contraloria"]
    )

@login_required
def abastecimiento():
    noticias = cargar_noticias()
    usuario, empresa, logos = get_context()
    return render_template(
        "abastecimiento.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        noticias_abastecimiento=noticias["abastecimiento"]
    )

@login_required
def indicadores():
    noticias = cargar_noticias()
    usuario, empresa, logos = get_context()
    seccion = request.args.get("seccion")
    return render_template(
        "indicadores.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        seccion=seccion,
        noticias_indicadores=noticias["indicadores"]
    )

@login_required
def tic():
    noticias = cargar_noticias()
    usuario, empresa, logos = get_context()
    return render_template(
        "tic.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        noticias_tic=noticias["tic"]
    )

@login_required
def comercio():
    noticias = cargar_noticias()
    usuario, empresa, logos = get_context()
    return render_template(
        "comercio.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        noticias_comercio=noticias["comercio"]
    )

@login_required
def tesoreria():
    noticias = cargar_noticias()
    usuario, empresa, logos = get_context()
    return render_template(
        "tesoreria.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=logos,
        noticias_tesoreria=noticias["tesoreria"]
    )
