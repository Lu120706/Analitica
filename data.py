# Usuarios
usuarios = {

    "admin@organizacion.com": {"nombre": "admin", "password": "123", "empresa": "Organizacion GYJ", "rol": "admin"},
    "juan@colmena.com": {"nombre": "juan", "password": "123", "empresa": "Colmena", "rol": "usuario"},
    "maria@almasa.com": {"nombre": "maria", "password": "123", "empresa": "Almasa", "rol": "usuario"},
    "mario@gyj.com": {"nombre": "mario", "password": "123", "empresa": "GyJ Ferreterias", "rol": "gerente"}
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