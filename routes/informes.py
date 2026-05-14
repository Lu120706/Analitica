from flask import jsonify
from utils import get_context, login_required

@login_required
def informe_ventas():
    usuario, empresa, logos = get_context()
    return jsonify({
        "status": "success",
        "reporte": "informe_ventas",
        "usuario": usuario,
        "empresa": empresa,
        "logos": logos
    })

@login_required
def balance_lineas():
    usuario, empresa, logos = get_context()
    return jsonify({
        "status": "success",
        "reporte": "balance_lineas",
        "usuario": usuario,
        "empresa": empresa,
        "logos": logos
    })

@login_required
def estado_financiero():
    usuario, empresa, logos = get_context()
    return jsonify({
        "status": "success",
        "reporte": "estado_financiero",
        "usuario": usuario,
        "empresa": empresa,
        "logos": logos
    })
