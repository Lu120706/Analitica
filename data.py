# Usuarios
usuarios = {
    "admin": {"password": "123", "empresa": "Organizacion GYJ", "rol": "admin"},
    "juan": {"password": "123", "empresa": "Colmena", "rol": "usuario"},
    "maria": {"password": "123", "empresa": "Almasa", "rol": "usuario"},
    "mario": {"password": "123", "empresa": "GyJ Ferreterias", "rol": "gerente"}
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
            {"nombre": "Gestion Col","ruta": "informe_ventas_page"},
            {"nombre": "Informe despachos", "ruta": "balance_lineas_page"},
            {"nombre": "Informe ventas", "ruta": "informe_ventas_page"},
            {"nombre": "IBR Colmena", "ruta": "estado_financiero_page"},
            {"nombre": "Inventario a un corte", "ruta": "balance_lineas_page"},
            {"nombre": "Venta perdida", "ruta": "estado_financiero_page"}
        ]
    },

    "Almasa": {
        "logos": [
            "https://cdn.phototourl.com/free/2026-05-08-96a31c18-592e-4d88-ad11-2b32bc4c58aa.png"],

        "pbi": "https://app.powerbi.com/",

        "informes": [
            {"nombre": "Contraloria", "ruta": "estado_financiero_page"},
            {"nombre": "Gestion clientes", "ruta": "informe_ventas_page"},
            {"nombre": "IBR Almasa","ruta": "balance_lineas_page"},
            {"nombre": "Informe ventas", "ruta": "informe_ventas_page"},
            {"nombre": "Venta perdida", "ruta": "estado_financiero_page"}
        ]
    },

    "GyJ Ferreterias": {
        "logos": [
            "https://cdn.phototourl.com/free/2026-05-08-c4138ab4-2de9-48d8-a38a-0c85bc40a293.png"
        ],

        "pbi": "https://app.powerbi.com/",

        "informes": [
            {"nombre": "Gestion clientes", "ruta": "informe_ventas_page"},
            {"nombre": "Balance de lineas","ruta": "balance_lineas_page"},
            {"nombre": "Cupo UNES", "ruta": "estado_financiero_page"},
            {"nombre": "IBR GyJ","ruta": "balance_lineas_page"},
            {"nombre": "Informe ventas","ruta": "informe_ventas_page"},
            {"nombre": "Venta perdida","ruta": "estado_financiero_page"}
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