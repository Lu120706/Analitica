from flask import Flask, redirect, render_template
from routes import auth, dashboard, departamentos, informes

app = Flask(__name__)
app.secret_key = "analitics_erp_2026"

app.add_url_rule("/api/login", "login", auth.login, methods=["GET", "POST"])
app.add_url_rule("/api/logout", "logout", auth.logout)

app.add_url_rule("/api/dashboard", "dashboard", dashboard.dashboard)
app.add_url_rule("/api/noticias", "crear_noticia", dashboard.crear_noticia, methods=["GET", "POST"])
app.add_url_rule("/api/comentarios", "api_comentarios", dashboard.api_comentarios, methods=["GET", "POST"])
app.add_url_rule("/api/guardar-comentario", "guardar_comentario", dashboard.guardar_comentario, methods=["POST"])
app.add_url_rule("/api/empresa/<nombre>", "empresa", dashboard.empresa)


app.add_url_rule("/api/contabilidad", "contabilidad", departamentos.contabilidad)
app.add_url_rule("/api/contraloria", "contraloria", departamentos.contraloria)
app.add_url_rule("/api/abastecimiento", "abastecimiento", departamentos.abastecimiento)
app.add_url_rule("/api/indicadores", "indicadores", departamentos.indicadores)
app.add_url_rule("/api/tic", "tic", departamentos.tic)
app.add_url_rule("/api/comercio", "comercio", departamentos.comercio)
app.add_url_rule("/api/tesoreria", "tesoreria", departamentos.tesoreria)


app.add_url_rule("/api/informe/ventas", "informe_ventas", informes.informe_ventas)
app.add_url_rule("/api/informe/balance", "balance_lineas", informes.balance_lineas)
app.add_url_rule("/api/informe/financiero", "estado_financiero", informes.estado_financiero)

# Rutas para servir templates HTML (frontend)
app.add_url_rule("/login", "login_page", lambda: render_template("login.html"))
app.add_url_rule("/dashboard", "dashboard_page", lambda: render_template("dashboard.html"))
app.add_url_rule("/noticias", "crear_noticia_page", lambda: render_template("crear_noticia.html"))
app.add_url_rule("/empresa/<nombre>", "empresa_page", lambda nombre: render_template("empresa.html", nombre=nombre))

app.add_url_rule("/contabilidad", "contabilidad_page", lambda: render_template("contabilidad.html"))
app.add_url_rule("/contraloria", "contraloria_page", lambda: render_template("contraloria.html"))
app.add_url_rule("/abastecimiento", "abastecimiento_page", lambda: render_template("abastecimiento.html"))
app.add_url_rule("/indicadores", "indicadores_page", lambda: render_template("indicadores.html"))
app.add_url_rule("/tic", "tic_page", lambda: render_template("tic.html"))
app.add_url_rule("/comercio", "comercio_page", lambda: render_template("comercio.html"))
app.add_url_rule("/tesoreria", "tesoreria_page", lambda: render_template("tesoreria.html"))

app.add_url_rule("/informe/ventas", "informe_ventas_page", lambda: render_template("informe_ventas.html"))
app.add_url_rule("/informe/balance", "balance_lineas_page", lambda: render_template("balance_lineas.html"))
app.add_url_rule("/informe/financiero", "estado_financiero_page", lambda: render_template("informe_financiero.html"))

app.add_url_rule("/", "home", lambda: redirect("/login"))

if __name__ == "__main__":
    app.run(debug=True)