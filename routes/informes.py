from flask import render_template
from utils import get_context, login_required

@login_required
def informe_ventas():
    usuario, empresa, logos = get_context()
    return render_template(
        'informe_ventas.html',
        empresa=empresa,
        usuario=usuario,
        logos=logos
    )

@login_required
def balance_lineas():
    usuario, empresa, logos = get_context()
    return render_template(
        'balance_lineas.html',
        empresa=empresa,
        usuario=usuario,
        logos=logos
    )

@login_required
def estado_financiero():
    usuario, empresa, logos = get_context()
    return render_template(
        'informe_financiero.html',
        empresa=empresa,
        usuario=usuario,
        logos=logos
    )
