from .auth import login, logout
from .dashboard import (
    dashboard_view, dashboard_api, crear_noticia, api_comentarios, 
    empresa, ver_comentarios, responder_comentario, 
    api_notificaciones, api_marcar_leido_admin, api_marcar_leido_usuario
)
from .departamentos import (
    contabilidad, auditoria, revision_fiscal, contraloria, 
    indicador_1, indicador_2, contraloria_reportes,
    abastecimiento, indicadores, tic, comercio, tesoreria, campañas
)

from .informes import informe_ventas, balance_lineas, estado_financiero
