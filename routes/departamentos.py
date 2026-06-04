from flask import request, session, render_template
from data import empresas_config
from utils import cargar_noticias, get_saludo, get_context, get_usuario_nombre, login_required, filtrar_noticias

def _transformar_logos(logos, empresa, rol):
    """Convierte la lista de URLs en dicts {nombre, url} igual que el dashboard."""
    logos_transformados = []
    for logo in logos:
        nombre_real = empresa
        if rol == "admin" and empresa == "Organizacion GYJ":
            for nombre_emp, conf in empresas_config.items():
                if nombre_emp != "Organizacion GYJ" and logo in conf.get("logos", []):
                    nombre_real = nombre_emp
                    break
        logos_transformados.append({"nombre": nombre_real, "url": logo})
    return logos_transformados

def _obtener_contexto_seccion(seccion_key, usuario, empresa, logos, rol):
    data_noticias = cargar_noticias()
    noticias_filtradas = filtrar_noticias(data_noticias.get(seccion_key, []), usuario, rol)
    
    return {
        "usuario": usuario,
        "empresa": empresa,
        "rol": rol,
        "saludo": get_saludo(),
        "noticias": noticias_filtradas,
        "logos": _transformar_logos(logos, empresa, rol),
        "seccion": seccion_key
    }

@login_required
def contabilidad():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("contabilidad", usuario, empresa, logos, rol)
    contexto["nombre_usuario"] = nombre_usuario
    return render_template('contabilidad/contabilidad.html', data=contexto)

@login_required
def contraloria():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("contraloria", usuario, empresa, logos, rol)
    contexto["nombre_usuario"] = nombre_usuario
    return render_template('contraloria/contraloria.html', data=contexto)

@login_required
def abastecimiento():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("abastecimiento", usuario, empresa, logos, rol)
    contexto["nombre_usuario"] = nombre_usuario
    return render_template('abastecimiento/abastecimiento.html', data=contexto)

@login_required
def indicadores():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("indicadores", usuario, empresa, logos, rol)
    contexto["nombre_usuario"] = nombre_usuario
    return render_template('indicadores/indicadores.html', data=contexto)

@login_required
def tic():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("tic", usuario, empresa, logos, rol)
    contexto["nombre_usuario"] = nombre_usuario
    return render_template('tic/tic.html', data=contexto)

@login_required
def comercio():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = _obtener_contexto_seccion("comercio", usuario, empresa, logos, rol)
    contexto["nombre_usuario"] = nombre_usuario
    return render_template('comercio/comercio.html', data=contexto)


@login_required
def tesoreria():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = {
        "usuario": usuario, "nombre_usuario": nombre_usuario,
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, rol),
        "saludo": get_saludo(), "noticias": cargar_noticias().get("tesoreria", []),
        "rol": rol
    }
    return render_template('tesoreria/tesoreria.html', data=contexto)
                           
@login_required
def tesoreria_reporte(nombre):
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": nombre, "rol": session.get("rol"), "saludo": get_saludo()
    }
    return render_template('tesoreria/reporte.html', data=contexto)

@login_required
def auditoria():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Auditoría", "rol": session.get("rol"), "saludo": get_saludo()
    }
    return render_template('contabilidad/auditoria.html', data=contexto)

@login_required
def revision_fiscal():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Revisión Fiscal", "rol": session.get("rol"), "saludo": get_saludo()
    }
    return render_template('contabilidad/revision_fiscal.html', data=contexto)

@login_required
def indicador_1():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Indicador 1", "rol": session.get("rol"), "saludo": get_saludo()
    }
    return render_template('contraloria/indicador_1.html', data=contexto)

@login_required
def indicador_2():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Indicador 2", "rol": session.get("rol"), "saludo": get_saludo()
    }
    return render_template('contraloria/indicador_2.html', data=contexto)

@login_required
def contraloria_reportes():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Reportes de Contraloría", "rol": session.get("rol"), "saludo": get_saludo()
    }
    return render_template('contraloria/reportes.html', data=contexto)

@login_required
def campañas():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa":empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Campañas de abastecimiento", "rol": session.get("rol"), "saludo": get_saludo()
    } 

    return render_template('abastecimiento/campañas.html', data=contexto)