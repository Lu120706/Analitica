import os
from dotenv import load_dotenv
load_dotenv()

usuarios = {
    os.getenv("ADMIN_EMAIL"): {
        "nombre": os.getenv("ADMIN_NAME", "admin"),
        "password": os.getenv("ADMIN_PASSWORD"),
        "empresa": os.getenv("ADMIN_EMPRESA", "Organizacion GYJ"),
        "rol": os.getenv("ADMIN_ROL", "admin")
    },
    os.getenv("USUARIO_JUAN_EMAIL"): {
        "nombre": os.getenv("USUARIO_JUAN_NAME", "juan"),
        "password": os.getenv("USUARIO_JUAN_PASSWORD"),
        "empresa": os.getenv("USUARIO_JUAN_EMPRESA", "Colmena"),
        "rol": os.getenv("USUARIO_JUAN_ROL", "usuario")
    },
    os.getenv("USUARIO_MARIA_EMAIL"): {
        "nombre": os.getenv("USUARIO_MARIA_NAME", "maria"),
        "password": os.getenv("USUARIO_MARIA_PASSWORD"),
        "empresa": os.getenv("USUARIO_MARIA_EMPRESA", "Almasa"),
        "rol": os.getenv("USUARIO_MARIA_ROL", "usuario")
    },
    os.getenv("USUARIO_MARIO_EMAIL"): {
        "nombre": os.getenv("USUARIO_MARIO_NAME", "mario"),
        "password": os.getenv("USUARIO_MARIO_PASSWORD"),
        "empresa": os.getenv("USUARIO_MARIO_EMPRESA", "GyJ Ferreterias"),
        "rol": os.getenv("USUARIO_MARIO_ROL", "gerente")
    }
}

# contactos
contactos_tic = [
    {"nombre": "Jose Pérez", "rol": "Jefe TIC", "email": "jose.perez@empresa.com"},
    {"nombre": "Juliana Gómez", "rol": "Soporte TIC", "email": "juliana.gomez@empresa.com"},
    {"nombre": "Carlos López", "rol": "Analista TIC", "email": "carlos.lopez@empresa.com"}
]

# empresas con informes por empresa
empresas_config = {
    "Colmena": {
        "logos": [
            "https://cdn.phototourl.com/free/2026-05-08-5729c248-9b06-4eec-85a9-656cabf66c54.png"],

        "pbi": "https://app.powerbi.com/",

        "informes": [
            {"nombre": "Gestion Col", "url": "/informe/ventas", "keywords": ["gestion", "col", "colmena", "ventas"]},
            {"nombre": "Informe despachos", "url": "/informe/balance", "keywords": ["despachos", "balance", "lineas", "inventario"]},
            {"nombre": "Informe ventas", "url": "/informe/ventas", "keywords": ["ventas", "ingresos", "comercial"]},
            {"nombre": "IBR Colmena", "url": "/informe/financiero", "keywords": ["ibr", "colmena", "indicadores", "financiero"]},
            {"nombre": "Inventario a un corte", "url": "/informe/balance", "keywords": ["inventario", "balance", "corte", "stock"]},
            {"nombre": "Venta perdida", "url": "/informe/ventas", "keywords": ["venta", "perdida", "oportunidad"]}
        ],
        "kpis": {"meta_ventas": "85%", "meta_despachos": "92%"},
        "auditoria": {
            "ultimos_hallazgos": ["Conciliación Bancaria", "Cuentas por pagar", "Revisión IVA"],
            "fecha_ultima_auditoria": "2026-05-15"
        }
    },

    "Almasa": {
        "logos": [
            "https://cdn.phototourl.com/free/2026-05-08-96a31c18-592e-4d88-ad11-2b32bc4c58aa.png"],

        "pbi": "https://app.powerbi.com/",

        "informes": [
            {"nombre": "Contraloria", "url": "/informe/financiero", "keywords": ["contraloria", "auditoria", "financiero", "estado"]},
            {"nombre": "Gestion clientes", "url": "/informe/ventas", "keywords": ["gestion", "clientes", "comercio", "cartera"]},
            {"nombre": "IBR Almasa", "url": "/informe/balance", "keywords": ["ibr", "almasa", "indicadores", "balance"]},
            {"nombre": "Informe ventas", "url": "/informe/ventas", "keywords": ["ventas", "ingresos", "comercial"]},
            {"nombre": "Venta perdida", "url": "/informe/ventas", "keywords": ["venta", "perdida", "oportunidad"]}
        ],
        "kpis": {"meta_ventas": "78%", "meta_despachos": "88%"},
        "auditoria": {
            "ultimos_hallazgos": ["Activos fijos", "Caja menor"],
            "fecha_ultima_auditoria": "2026-04-20"
        }
    },

    "GyJ Ferreterias": {
        "logos": [
            "https://cdn.phototourl.com/free/2026-05-08-c4138ab4-2de9-48d8-a38a-0c85bc40a293.png"
        ],

        "pbi": "https://app.powerbi.com/",

        "informes": [
            {"nombre": "Gestion clientes", "url": "/informe/ventas", "keywords": ["gestion", "clientes", "comercio", "cartera"]},
            {"nombre": "Balance de lineas", "url": "/informe/balance", "keywords": ["balance", "lineas", "produccion", "inventario"]},
            {"nombre": "Cupo UNES", "url": "/informe/financiero", "keywords": ["cupo", "unes", "credito", "financiero"]},
            {"nombre": "IBR GyJ", "url": "/informe/balance", "keywords": ["ibr", "gyj", "indicadores", "balance"]},
            {"nombre": "Informe ventas", "url": "/informe/ventas", "keywords": ["ventas", "ingresos", "comercial"]},
            {"nombre": "Venta perdida", "url": "/informe/ventas", "keywords": ["venta", "perdida", "oportunidad"]}
        ],
        "kpis": {"meta_ventas": "95%", "meta_despachos": "98%"},
        "auditoria": {
            "ultimos_hallazgos": ["Inventarios", "Auditoría de nomina"],
            "fecha_ultima_auditoria": "2026-06-01"
        }
    },

    "Organizacion GYJ": {
        "logos": [
            "https://cdn.phototourl.com/free/2026-05-08-c4138ab4-2de9-48d8-a38a-0c85bc40a293.png",
            "https://cdn.phototourl.com/free/2026-05-08-5729c248-9b06-4eec-85a9-656cabf66c54.png",
            "https://cdn.phototourl.com/free/2026-05-08-96a31c18-592e-4d88-ad11-2b32bc4c58aa.png"
        ],

        "pbi": "https://app.powerbi.com/"
    }
}

informes_buscador = [
    {"nombre": "Informe de Ventas", "url": "/informe/ventas", "keywords": ["ventas", "comercial", "dinero", "ingresos", "venta", "reportes"]},
    {"nombre": "Balance de Líneas", "url": "/informe/balance", "keywords": ["balance", "lineas", "produccion", "inventario", "stock", "reportes"]},
    {"nombre": "Estado Financiero", "url": "/informe/financiero", "keywords": ["financiero", "contable", "estado", "utilidad", "ingresos", "reportes"]},
    {"nombre": "Informe de Producción", "url": "/informe/produccion", "keywords": ["produccion", "corte", "laminas", "fabricacion", "reportes"]},
    {"nombre": "Reporte IBR", "url": "/informe/balance", "keywords": ["ibr", "indicadores", "tasas", "rendimiento", "reportes"]},
    {"nombre": "Reporte de Cartera", "url": "/informe/ventas", "keywords": ["cartera", "deuda", "cobro", "cliente", "reportes"]},
    {"nombre": "Gestión de Clientes", "url": "/informe/ventas", "keywords": ["gestion", "clientes", "comercio", "cartera", "reportes"]},
    {"nombre": "Control de Inventario", "url": "/informe/balance", "keywords": ["inventario", "balance", "corte", "stock", "reportes"]},
    {"nombre": "Cupo y Créditos", "url": "/informe/financiero", "keywords": ["cupo", "credito", "financiero", "unes", "reportes"]},
    {"nombre": "Auditoría y Control", "url": "/informe/financiero", "keywords": ["auditoria", "control", "contraloria", "financiero", "reportes"]}
]