import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template
from routes import auth, dashboard, departamentos, informes
from utils import init_db

load_dotenv()

from data import informes_buscador

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "analitics_erp_2026")

@app.context_processor
def inject_globals():
    return dict(informes_buscador=informes_buscador)

init_db()

app.add_url_rule("/login", "login", auth.login, methods=["GET", "POST"])
app.add_url_rule("/api/logout", "logout", auth.logout)

app.add_url_rule("/api/dashboard", "dashboard_api", dashboard.dashboard_api)
app.add_url_rule("/api/comentarios", "api_comentarios", dashboard.api_comentarios, methods=["GET", "POST"])
app.add_url_rule("/api/notificaciones", "api_notificaciones", dashboard.api_notificaciones)
app.add_url_rule("/api/notificaciones/leido_admin", "api_marcar_leido_admin", dashboard.api_marcar_leido_admin, methods=["POST"])
app.add_url_rule("/api/notificaciones/leido_usuario", "api_marcar_leido_usuario", dashboard.api_marcar_leido_usuario, methods=["POST"])
app.add_url_rule("/api/responder-comentario", "responder_comentario", dashboard.responder_comentario, methods=["POST"])

app.add_url_rule("/dashboard", "dashboard", dashboard.dashboard_view)
app.add_url_rule("/noticias", "crear_noticia", dashboard.crear_noticia, methods=["GET", "POST"])
app.add_url_rule("/comentarios", "ver_comentarios", dashboard.ver_comentarios)
app.add_url_rule("/empresa/<nombre>", "empresa", dashboard.empresa)

app.add_url_rule("/contabilidad", "contabilidad", departamentos.contabilidad)
app.add_url_rule("/auditoria", "auditoria", departamentos.auditoria)
app.add_url_rule("/revision-fiscal", "revision_fiscal", departamentos.revision_fiscal)
app.add_url_rule("/contraloria", "contraloria", departamentos.contraloria)
app.add_url_rule("/contraloria/indicador-1", "indicador_1", departamentos.indicador_1)
app.add_url_rule("/contraloria/indicador-2", "indicador_2", departamentos.indicador_2)
app.add_url_rule("/contraloria/reportes", "contraloria_reportes", departamentos.contraloria_reportes)
app.add_url_rule("/abastecimiento", "abastecimiento", departamentos.abastecimiento)
app.add_url_rule("/abastecimiento/campañas", "campañas", departamentos.campañas)
app.add_url_rule("/indicadores", "indicadores", departamentos.indicadores)
app.add_url_rule("/tic", "tic", departamentos.tic)
app.add_url_rule("/comercio", "comercio", departamentos.comercio)
app.add_url_rule("/tesoreria", "tesoreria", departamentos.tesoreria)
app.add_url_rule("/tesoreria/reporte/<nombre>", "tesoreria_reporte", departamentos.tesoreria_reporte)

app.add_url_rule("/informe/ventas", "informe_ventas", informes.informe_ventas)
app.add_url_rule("/informe/balance", "balance_lineas", informes.balance_lineas)
app.add_url_rule("/informe/financiero", "estado_financiero", informes.estado_financiero)

app.add_url_rule("/", "home", lambda: redirect("/login"))

if __name__ == "__main__":
    app.run(debug=True)