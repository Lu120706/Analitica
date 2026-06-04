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

# empresasx
empresas_config = {
    "Colmena": {
        "logos": [
            "https://cdn.phototourl.com/free/2026-05-08-5729c248-9b06-4eec-85a9-656cabf66c54.png"],

        "pbi": "https://app.powerbi.com/",

        "informes": [
            {"nombre": "Gestion Col","ruta": "informe_ventas"},
            {"nombre": "Informe despachos", "ruta": "balance_lineas"},
            {"nombre": "Informe ventas", "ruta": "informe_ventas"},
            {"nombre": "IBR Colmena", "ruta": "estado_financiero"},
            {"nombre": "Inventario a un corte", "ruta": "balance_lineas"},
            {"nombre": "Venta perdida", "ruta": "estado_financiero"}
        ]
    },

    "Almasa": {
        "logos": [
            "https://cdn.phototourl.com/free/2026-05-08-96a31c18-592e-4d88-ad11-2b32bc4c58aa.png"],

        "pbi": "https://app.powerbi.com/",

        "informes": [
            {"nombre": "Contraloria", "ruta": "estado_financiero"},
            {"nombre": "Gestion clientes", "ruta": "informe_ventas"},
            {"nombre": "IBR Almasa","ruta": "balance_lineas"},
            {"nombre": "Informe ventas", "ruta": "informe_ventas"},
            {"nombre": "Venta perdida", "ruta": "estado_financiero"}
        ]
    },

    "GyJ Ferreterias": {
        "logos": [
            "https://cdn.phototourl.com/free/2026-05-08-c4138ab4-2de9-48d8-a38a-0c85bc40a293.png"
        ],

        "pbi": "https://app.powerbi.com/",

        "informes": [
            {"nombre": "Gestion clientes", "ruta": "informe_ventas"},
            {"nombre": "Balance de lineas","ruta": "balance_lineas"},
            {"nombre": "Cupo UNES", "ruta": "estado_financiero"},
            {"nombre": "IBR GyJ","ruta": "balance_lineas"},
            {"nombre": "Informe ventas","ruta": "informe_ventas"},
            {"nombre": "Venta perdida","ruta": "estado_financiero"}
        ]
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
    {"nombre": "Informe de Ventas", "url": "/informe/ventas", "keywords": ["ventas", "comercial", "dinero", "ingresos"]},
    {"nombre": "Balance de Líneas", "url": "/informe/balance", "keywords": ["balance", "lineas", "produccion", "inventario"]},
    {"nombre": "Estado Financiero", "url": "/informe/financiero", "keywords": ["financiero", "contable", "estado", "utilidad"]},
    {"nombre": "Reporte IBR", "url": "#", "keywords": ["ibr", "indicadores", "tasas"]},
    {"nombre": "Reporte de Cartera", "url": "#", "keywords": ["cartera", "deuda", "cobro"]}
]