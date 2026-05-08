from flask import Flask
from routes import auth, dashboard, departamentos, informes

app = Flask(__name__)
app.secret_key = "analitics_erp_2026"


app.add_url_rule("/", "login", auth.login, methods=["GET", "POST"])
app.add_url_rule("/logout", "logout", auth.logout)


app.add_url_rule("/dashboard", "dashboard", dashboard.dashboard)
app.add_url_rule("/crear-noticia", "crear_noticia", dashboard.crear_noticia, methods=["GET", "POST"])
app.add_url_rule("/empresa/<nombre>", "empresa", dashboard.empresa)


app.add_url_rule("/contabilidad", "contabilidad", departamentos.contabilidad)
app.add_url_rule("/contraloria", "contraloria", departamentos.contraloria)
app.add_url_rule("/abastecimiento", "abastecimiento", departamentos.abastecimiento)
app.add_url_rule("/indicadores", "indicadores", departamentos.indicadores)
app.add_url_rule("/tic", "tic", departamentos.tic)
app.add_url_rule("/comercio", "comercio", departamentos.comercio)
app.add_url_rule("/tesoreria", "tesoreria", departamentos.tesoreria)


app.add_url_rule("/informe/ventas", "informe_ventas", informes.informe_ventas)
app.add_url_rule("/informe/balance", "balance_lineas", informes.balance_lineas)
app.add_url_rule("/informe/financiero", "estado_financiero", informes.estado_financiero)

if __name__ == "__main__":
    app.run(debug=True)