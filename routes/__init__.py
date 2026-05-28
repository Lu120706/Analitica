# Este archivo permite que la carpeta 'routes' sea tratada como un paquete.
from .auth import login, logout
from .dashboard import (
    dashboard_view, dashboard_api, crear_noticia, api_comentarios, 
    empresa, ver_comentarios, responder_comentario, 
    api_notificaciones, api_marcar_leido_admin, api_marcar_leido_usuario
)
from .departamentos import (
    contabilidad, auditoria, revision_fiscal, contraloria, abastecimiento, 
    indicadores, tic, comercio, tesoreria
)

from .informes import informe_ventas, balance_lineas, estado_financiero
