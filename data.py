# Usuarios
usuarios = {
    "admin": {"password": "123", "empresa": "Organizacion GYJ"},
    "juan": {"password": "123", "empresa": "Colmena"},
    "maria": {"password": "123", "empresa": "Almasa"},
    "mario": {"password": "123", "empresa": "GyJ Ferreterias"}
}

# contactos
contactos_tic = [
    {"nombre": "Jose Pérez", "rol": "Jefe TIC", "email": "jose.perez@empresa.com"},
    {"nombre": "Juliana Gómez", "rol": "Soporte TIC", "email": "juliana.gomez@empresa.com"},
    {"nombre": "Carlos López", "rol": "Analista TIC", "email": "carlos.lopez@empresa.com"}
]

# empresas
empresas_config = {
    "Colmena": {
        "logos": ["https://cdn.phototourl.com/free/2026-04-28-4a9e8bed-aa35-4a34-b73f-e93ee7e59627.png"],
        "pbi": "https://app.powerbi.com/",
        "noticias": [{"titulo": "Aviso Colmena", "texto": "Hoy mantenimiento"}]
    },
    "Almasa": {
        "logos": ["https://cdn.phototourl.com/member/2026-03-24-3b7755ae-b4ae-4423-b0a9-a70e72c6a815.png"],
        "pbi": "https://app.powerbi.com/",
        "noticias": [{"titulo": "Aviso Almasa", "texto": "Nuevas políticas"}]
    },
    "GyJ Ferreterias": {
        "logos": ["https://cdn.phototourl.com/member/2026-03-24-cd01a241-a822-499e-880f-81e6e291a732.png"],
        "pbi": "https://app.powerbi.com/",
        "noticias": [{"titulo": "Aviso GyJ", "texto": "Inventario fin de semana"}]
    },
    "Organizacion GYJ": {
        "logos": [
            "https://cdn.phototourl.com/member/2026-03-24-cd01a241-a822-499e-880f-81e6e291a732.png",
            "https://cdn.phototourl.com/free/2026-04-28-4a9e8bed-aa35-4a34-b73f-e93ee7e59627.png",
            "https://cdn.phototourl.com/member/2026-03-24-3b7755ae-b4ae-4423-b0a9-a70e72c6a815.png"
        ],
        "pbi": "https://app.powerbi.com/",
        "noticias": [{"titulo": "Global", "texto": "Comunicado general"}]
    }
}

# noticias indicadores
noticias_indicadores = {
    "indicadores": [
        {"titulo": "KPIs de desempeño", "texto": "Cumplimiento del 95% en metas operativas."},
        {"titulo": "Productividad por área", "texto": "El área comercial lidera en resultados."},
        {"titulo": "Tendencia mensual", "texto": "Crecimiento sostenido durante el trimestre."}
    ],
    "reportes": [
        {"titulo": "Reporte consolidado", "texto": "Disponible informe general por áreas."},
        {"titulo": "Comparativo histórico", "texto": "Mejora frente al año anterior."},
        {"titulo": "Alertas", "texto": "Variaciones en indicadores financieros detectadas."}
    ],
    "default": [
        {"titulo": "Resumen ejecutivo", "texto": "Estabilidad operativa general."},
        {"titulo": "Cumplimiento", "texto": "87% de objetivos alcanzados."},
        {"titulo": "Áreas críticas", "texto": "Mejorar tiempos de respuesta."},
        {"titulo": "Proyección", "texto": "Crecimiento positivo esperado."}
    ]
}

#Noticias areas
noticias_abastecimiento = {
    "abastecimiento": [
        {"titulo": "Nueva campaña comercial", "texto": "Se lanzaron campañas enfocadas en clientes estratégicos."},
        {"titulo": "Actualización de clientes", "texto": "Se optimizó la segmentación para mejorar decisiones."},
        {"titulo": "Resultados de ventas", "texto": "Incremento del 10% frente al mes anterior."}
    ]
}

noticias_contabilidad = [
    {"titulo": "Cierre mensual", "texto": "Fecha límite 30 abril"},
    {"titulo": "DIAN", "texto": "Nueva validación electrónica"},
    {"titulo": "Alerta", "texto": "Faltan soportes Q1"}
]

noticias_tic = [
    {"titulo": "Optimización de infraestructura", "texto": "Mejora en rendimiento de sistemas."},
    {"titulo": "Backup automático", "texto": "Respaldo diario implementado."},
    {"titulo": "Monitoreo en tiempo real", "texto": "Prevención de fallos en servidores."}
]

noticias_tesoreria = [
    {"titulo": "Flujo de caja actualizado", "texto": "Se actualizó el flujo de caja del mes."},
    {"titulo": "Pagos programados", "texto": "Se programaron pagos a proveedores."},
    {"titulo": "Conciliación bancaria", "texto": "Se está revisando la conciliación de bancos."}
]

noticias_comercio = [
    {"titulo": "Campañas", "texto": "Seguimiento a campañas activas y resultados."},
    {"titulo": "Clientes", "texto": "Segmentación y comportamiento de clientes."},
    {"titulo": "Ventas", "texto": "Análisis de desempeño comercial."}
]

noticias_indicadores = {
    "default": [
        {"titulo": "Resumen ejecutivo", "texto": "Los indicadores reflejan estabilidad operativa con oportunidades de mejora en eficiencia."},
        {"titulo": "Cumplimiento de metas", "texto": "El 87% de los objetivos estratégicos han sido alcanzados en el periodo actual."},
        {"titulo": "Áreas críticas", "texto": "Se identifican oportunidades de mejora en tiempos de respuesta y procesos internos."},
        {"titulo": "Proyección", "texto": "Se proyecta crecimiento positivo si se mantienen las condiciones actuales."}
    ]
}

noticias_contraloria = [
    {"titulo": "Control Interno", "texto": "Gestión de auditorías y control de procesos."},
    {"titulo": "Riesgos", "texto": "Identificación y mitigación de riesgos."},
]