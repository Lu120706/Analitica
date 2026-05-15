from flask import request, session, render_template
from utils import cargar_noticias, get_saludo, get_context, login_required, filtrar_noticias

def _obtener_contexto_seccion(seccion_key, usuario, empresa, logos, rol):
    data_noticias = cargar_noticias()
    noticias_filtradas = filtrar_noticias(data_noticias.get(seccion_key, []), usuario, rol)
    
    return {
        "usuario": usuario,
        "empresa": empresa,
        "rol": rol,
        "saludo": get_saludo(),
        "noticias": noticias_filtradas,
        "logos": logos,
        "seccion": seccion_key
    }

@login_required
def contabilidad():
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("contabilidad", usuario, empresa, logos, rol)
    return render_template('contabilidad.html', data=contexto)

@login_required
def contraloria():
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("contraloria", usuario, empresa, logos, rol)
    return render_template('contraloria.html', data=contexto)

@login_required
def abastecimiento():
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    # Ajustado a la sección específica "abastecimiento" según tus códigos previos
    contexto = _obtener_contexto_seccion("abastecimiento", usuario, empresa, logos, rol)
    return render_template('abastecimiento.html', data=contexto)

@login_required
def indicadores():
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("indicadores", usuario, empresa, logos, rol)
    return render_template('indicadores.html', data=contexto)

@login_required
def tic():
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("tic", usuario, empresa, logos, rol)
    return render_template('tic.html', data=contexto)

@login_required
def comercio():
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("comercio", usuario, empresa, logos, rol)
    return render_template('comercio.html', data=contexto)

@login_required
def tesoreria():
    usuario, empresa, logos = get_context()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("tesoreria", usuario, empresa, logos, rol)
    return render_template('tesoreria.html', data=contexto)