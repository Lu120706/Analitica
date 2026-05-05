from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
from functools import wraps
from data import (
    usuarios,
    contactos_tic,
    empresas_config,
    noticias_contabilidad,
    noticias_indicadores,
    noticias_abastecimiento,
    noticias_tic, 
    noticias_tesoreria
)
import pytz

app = Flask(__name__)
app.secret_key = "analitics_erp_2026"


def get_saludo():
    zona = pytz.timezone("America/Bogota")
    hora = datetime.now(zona).hour

    if hora < 12:
        return "Buenos días"
    elif hora < 18:
        return "Buenas tardes"
    return "Buenas noches"


def get_context():
    usuario = session.get("usuario")

    if not usuario:
        return None, None, None

    rol = session.get("rol")
    empresa = session.get("empresa")

    if rol == "admin":
        empresa = "Organizacion GYJ"

    config = empresas_config.get(empresa)

    if not config:
        empresa = "Organizacion GYJ"
        config = empresas_config.get(empresa)

    return usuario, empresa, config


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("usuario"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper


@app.route("/", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        username = request.form.get("usuario")
        password = request.form.get("password")

        if username in usuarios and usuarios[username]["password"] == password:
            session["usuario"] = username
            session["empresa"] = usuarios[username]["empresa"]
            session["rol"] = "admin" if username == "admin" else "user"

            return redirect(url_for("dashboard"))

        error = "Credenciales inválidas"

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    usuario, empresa, config = get_context()

    return render_template(
        "dashboard.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        noticias=config.get("noticias", []),
        logos=config.get("logos", []),
        contactos_tic=contactos_tic
    )


@app.route("/contabilidad")
@login_required
def contabilidad():
    usuario, empresa, config = get_context()

    return render_template(
        "contabilidad.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        noticias=noticias_contabilidad,
        logos=config.get("logos", [])
    )

@app.route("/contraloria")
@login_required
def contraloria():
    usuario, empresa, config = get_context()

    return render_template(
        "contraloria.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=config.get("logos", [])
    )

@app.route("/abastecimiento")
@login_required
def abastecimiento():
    usuario, empresa, config = get_context()

    return render_template(
        "abastecimiento.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=config.get("logos", []),
        noticias=noticias_abastecimiento
    )


@app.route("/indicadores")
@login_required
def indicadores():
    usuario, empresa, config = get_context()
    seccion = request.args.get("seccion")

    if seccion in noticias_indicadores:
        noticias = noticias_indicadores[seccion]
    else:
        noticias = noticias_indicadores["default"]

    return render_template(
        "indicadores.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=config.get("logos", []),
        noticias=noticias
    )


@app.route("/tic")
@login_required
def tic():
    usuario, empresa, config = get_context()

    return render_template(
        "tic.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=config.get("logos", []),
        noticias=noticias_tic
    )

@app.route("/comercio")
@login_required
def comercio():
    usuario, empresa, config = get_context()

    return render_template(
        "comercio.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=config.get("logos", [])
    )

@app.route("/tesoreria")
@login_required
def tesoreria():
    usuario, empresa, config = get_context()

    return render_template(
        "tesoreria.html",
        usuario=usuario,
        empresa=empresa,
        saludo=get_saludo(),
        logos=config.get("logos", []),
        noticias= noticias_tesoreria
    )

@app.route('/informes')
def informes():
    usuario, empresa, config = get_context()

    return render_template(
        'informes.html',
        empresa=empresa,
        usuario=usuario
    )

@app.route('/informe/ventas')
def informe_ventas():
    usuario, empresa, config = get_context()

    return render_template(
        'informe_ventas.html',
        empresa=empresa,
        usuario=usuario,
        logos=config.get("logos", [])
    )

@app.route('/informe/balance')
def balance_lineas():
    usuario, empresa, config = get_context()

    return render_template(
        'balance_lineas.html',
        empresa=empresa,
        usuario=usuario,
        logos=config.get("logos", [])
    )


@app.route('/informe/financiero')
def estado_financiero():
    usuario, empresa, config = get_context()

    return render_template(
        'informe_financiero.html',
        empresa=empresa,
        usuario=usuario,
        logos=config.get("logos", [])
    )

if __name__ == "__main__":
    app.run(debug=True)