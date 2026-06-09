from flask import render_template, session
from utils import get_context, get_usuario_nombre, login_required

def _get_informe_context(titulo):
    usuario = session.get("usuario")
    tenant_id = session.get("tenant_id")
    rol = session.get("rol")
    
    # Filtramos logos: Si es admin, mostramos todos (o podrías definir lógica para admin). 
    # Si es usuario, solo los suyos.
    from data import empresas_config
    if rol == "admin":
        logos = []
        for conf in empresas_config.values():
            if conf.get("logos"):
                logos.extend(conf["logos"])
        # Eliminamos duplicados manteniendo orden
        logos = list(dict.fromkeys(logos))
    else:
        logos = empresas_config.get(tenant_id, {}).get("logos", [])
        
    return {
        "usuario": usuario,
        "nombre_usuario": get_usuario_nombre(),
        "empresa": tenant_id,
        "logos": logos,
        "titulo": titulo,
        "rol": rol
    }

@login_required
def informe_ventas():
    return render_template('informes/informe_ventas.html', data=_get_informe_context("Informe de Ventas"))

@login_required
def balance_lineas():
    return render_template('informes/balance_lineas.html', data=_get_informe_context("Balance por Líneas"))

@login_required
def estado_financiero():
    return render_template('informes/informe_financiero.html', data=_get_informe_context("Estado Financiero"))

@login_required
def informe_produccion():
    return render_template('informes/informe_produccion.html', data=_get_informe_context("Informe de producción: corte de laminas"))