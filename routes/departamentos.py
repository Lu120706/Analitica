from flask import request, session, render_template, url_for
from data import empresas_config
from utils import cargar_noticias, get_saludo, get_context, get_usuario_nombre, login_required, filtrar_noticias

def _transformar_logos(logos, empresa, rol):
    logos_transformados = []
    
    orden_logos = {
        "https://cdn.phototourl.com/free/2026-05-08-c4138ab4-2de9-48d8-a38a-0c85bc40a293.png": 1, # GyJ Ferreterias (Arriba)
        "https://cdn.phototourl.com/free/2026-05-08-5729c248-9b06-4eec-85a9-656cabf66c54.png": 2, # Colmena (Medio)
        "https://cdn.phototourl.com/free/2026-05-08-96a31c18-592e-4d88-ad11-2b32bc4c58aa.png": 3  # Almasa (Abajo)
    }
    
    for logo in logos:
        nombre_real = empresa
        if rol == "admin" and empresa == "Organizacion GYJ":
            for nombre_emp, conf in empresas_config.items():
                if nombre_emp != "Organizacion GYJ" and logo in conf.get("logos", []):
                    nombre_real = nombre_emp
                    break
        logos_transformados.append({"nombre": nombre_real, "url": logo})
    
    # Ordenar según el índice definido en orden_logos
    return sorted(logos_transformados, key=lambda x: orden_logos.get(x['url'], 99))

def _obtener_logos_fijos(usuario, empresa, rol):
    # Obtener logos base usando la lógica de get_context()
    # Asumiendo que get_context devuelve (usuario, empresa, logos)
    from utils import get_context
    _, _, logos = get_context()
    return _transformar_logos(logos, empresa, rol)

def _obtener_contexto_seccion(seccion_key, usuario, empresa, logos, rol, ruta_inicio):
    data_noticias = cargar_noticias()
    noticias_filtradas = filtrar_noticias(data_noticias.get(seccion_key, []), usuario, rol)
    return {
        "usuario": usuario,
        "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa,
        "rol": rol,
        "saludo": get_saludo(),
        "noticias": noticias_filtradas,
        "logos": _transformar_logos(logos, empresa, rol),
        "seccion": seccion_key,
        "url_inicio_modulo": ruta_inicio
    }

@login_required
def contabilidad():
    usuario, empresa, logos = get_context()
    contexto = _obtener_contexto_seccion("contabilidad", usuario, empresa, logos, session.get("rol"), url_for('dashboard'))
    contexto["nombre_usuario"] = get_usuario_nombre()
    return render_template('contabilidad/contabilidad.html', data=contexto)

@login_required
def auditoria():
    tenant_id = session.get("tenant_id")
    config = empresas_config.get(tenant_id, {})
    return render_template('contabilidad/auditoria.html', data={
        "usuario": session.get("usuario"),
        "nombre_usuario": get_usuario_nombre(),
        "saludo": get_saludo(),
        "auditoria": config.get("auditoria", {}),
        "logos": _transformar_logos(config.get("logos", []), tenant_id, session.get("rol")),
        "url_inicio_modulo": url_for('contabilidad')
    })

@login_required
def nomina():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Nomina", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('contabilidad')
    }
    return render_template('contabilidad/nomina.html', data=contexto)

@login_required
def contraloria():
    usuario, empresa, logos = get_context()
    contexto = _obtener_contexto_seccion("contraloria", usuario, empresa, logos, session.get("rol"), url_for('dashboard'))
    contexto["nombre_usuario"] = get_usuario_nombre()
    return render_template('contraloria/contraloria.html', data=contexto)

@login_required
def indicador_financiero():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Indicador financiero", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('contraloria')
    }
    return render_template('contraloria/indicador_financiero.html', data=contexto)

@login_required
def indicador_gestion():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Indicador de gestión", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('contraloria')
    }
    return render_template('contraloria/indicador_gestion.html', data=contexto)

@login_required
def contraloria_reportes():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Reportes de Contraloría", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('contraloria')
    }
    return render_template('contraloria/reportes.html', data=contexto)

@login_required
def abastecimiento():
    usuario, empresa, logos = get_context()
    contexto = _obtener_contexto_seccion("abastecimiento", usuario, empresa, logos, session.get("rol"), url_for('dashboard'))
    contexto["nombre_usuario"] = get_usuario_nombre()
    return render_template('abastecimiento/abastecimiento.html', data=contexto)

@login_required
def campañas():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa":empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Campañas", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('abastecimiento')
    } 
    return render_template('abastecimiento/campañas.html', data=contexto)

@login_required
def comercio():
    usuario, empresa, logos = get_context()
    contexto = _obtener_contexto_seccion("comercio", usuario, empresa, logos, session.get("rol"), url_for('dashboard'))
    contexto["nombre_usuario"] = get_usuario_nombre()
    return render_template('comercio/comercio.html', data=contexto)

@login_required
def comercio_campañas():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Campañas de Comercio", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('comercio')
    }
    return render_template('comercio/campañas.html', data=contexto)

@login_required
def comercio_clientes():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Clientes de Comercio", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('comercio')
    }
    return render_template('comercio/clientes.html', data=contexto)

@login_required
def comercio_ventas():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Ventas de Comercio", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('comercio')
    }
    return render_template('comercio/ventas.html', data=contexto)

@login_required
def tesoreria():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = {
        "usuario": usuario, "nombre_usuario": nombre_usuario,
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, rol),
        "saludo": get_saludo(), "noticias": cargar_noticias().get("tesoreria", []),
        "rol": rol, "url_inicio_modulo": url_for('dashboard')
    }
    return render_template('tesoreria/tesoreria.html', data=contexto)
                            
@login_required
def tesoreria_reporte(nombre):
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": nombre, "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('tesoreria')
    }
    return render_template('tesoreria/reporte.html', data=contexto)

@login_required
def indicadores():
    usuario, empresa, logos = get_context()
    contexto = _obtener_contexto_seccion("indicadores", usuario, empresa, logos, session.get("rol"), url_for('dashboard'))
    return render_template('indicadores/indicadores.html', data=contexto)

@login_required
def tic():
    usuario, empresa, logos = get_context()
    contexto = _obtener_contexto_seccion("tic", usuario, empresa, logos, session.get("rol"), url_for('dashboard'))
    return render_template('tic/tic.html', data=contexto)

@login_required
def recursos_humanos():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = {
        "usuario": usuario, "nombre_usuario": nombre_usuario,
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, rol),
        "saludo": get_saludo(), "noticias": cargar_noticias().get("recursos_humanos", []),
        "rol": rol, "url_inicio_modulo": url_for('dashboard')
    }
    return render_template('recursos_humanos/recursos_humanos.html', data=contexto)

@login_required
def gestion_documental():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Gestión Documental", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('recursos_humanos')
    }
    return render_template('recursos_humanos/gestion_documental.html', data=contexto)

@login_required
def recursos_humanos():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = {
        "usuario": usuario, "nombre_usuario": nombre_usuario,
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, rol),
        "saludo": get_saludo(), "noticias": cargar_noticias().get("recursos_humanos", []),
        "rol": rol, "url_inicio_modulo": url_for('dashboard'),
        "noticias": cargar_noticias().get("recursos_humanos", [])
    }
    return render_template('recursos_humanos/recursos_humanos.html', data=contexto)

@login_required
def gestion_documental():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Gestión Documental", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('recursos_humanos')
    }
    return render_template('recursos_humanos/gestion_documental.html', data=contexto)

@login_required
def comercio():
    usuario, empresa, logos = get_context()
    contexto = _obtener_contexto_seccion("comercio", usuario, empresa, logos, session.get("rol"), url_for('dashboard'))
    contexto["nombre_usuario"] = get_usuario_nombre()
    return render_template('comercio/comercio.html', data=contexto)

@login_required
def comercio_campañas():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Campañas de Comercio", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('comercio')
    }
    return render_template('comercio/campañas.html', data=contexto)

@login_required
def comercio_clientes():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Clientes de Comercio", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('comercio')
    }
    return render_template('comercio/clientes.html', data=contexto)

@login_required
def comercio_ventas():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Ventas de Comercio", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('comercio')
    }
    return render_template('comercio/ventas.html', data=contexto)

@login_required
def tesoreria():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = {
        "usuario": usuario, "nombre_usuario": nombre_usuario,
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, rol),
        "saludo": get_saludo(), "noticias": cargar_noticias().get("tesoreria", []),
        "rol": rol, "url_inicio_modulo": url_for('dashboard')
    }
    return render_template('tesoreria/tesoreria.html', data=contexto)
                            
@login_required
def tesoreria_reporte(nombre):
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": nombre, "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('tesoreria')
    }
    return render_template('tesoreria/reporte.html', data=contexto)

@login_required
def indicadores():
    usuario, empresa, logos = get_context()
    contexto = _obtener_contexto_seccion("indicadores", usuario, empresa, logos, session.get("rol"), url_for('dashboard'))
    return render_template('indicadores/indicadores.html', data=contexto)

@login_required
def tic():
    usuario, empresa, logos = get_context()
    contexto = _obtener_contexto_seccion("tic", usuario, empresa, logos, session.get("rol"), url_for('dashboard'))
    return render_template('tic/tic.html', data=contexto)

@login_required
def recursos_humanos():
    usuario, empresa, logos = get_context()
    nombre_usuario = get_usuario_nombre()
    rol = session.get("rol")
    contexto = {
        "usuario": usuario, "nombre_usuario": nombre_usuario,
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, rol),
        "saludo": get_saludo(), "noticias": cargar_noticias().get("recursos_humanos", []),
        "rol": rol, "url_inicio_modulo": url_for('dashboard')
    }
    return render_template('recursos_humanos/recursos_humanos.html', data=contexto)

@login_required
def gestion_documental():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Gestión Documental", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('recursos_humanos')
    }
    return render_template('recursos_humanos/gestion_documental.html', data=contexto)

@login_required
def seguridad_y_salud():
    usuario, empresa, logos = get_context()
    contexto = {
        "usuario": usuario, "nombre_usuario": get_usuario_nombre(),
        "empresa": empresa, "logos": _transformar_logos(logos, empresa, session.get("rol")),
        "titulo": "Seguridad y Salud", "rol": session.get("rol"), "saludo": get_saludo(),
        "url_inicio_modulo": url_for('recursos_humanos')
    }
    return render_template('recursos_humanos/seguridad_y_salud.html', data=contexto)
