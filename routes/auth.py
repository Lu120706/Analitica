from flask import render_template, request, redirect, url_for, session
from data import usuarios

def login():
    error = ""
    if request.method == "POST":
        username = request.form.get("usuario")
        password = request.form.get("password")
        if username in usuarios and usuarios[username]["password"] == password:
            session["usuario"] = username
            session["empresa"] = usuarios[username]["empresa"]
            session["rol"] = usuarios[username]["rol"]
            return redirect(url_for("dashboard"))
        error = "Credenciales inválidas"
    return render_template("login.html", error=error)

def logout():
    session.clear()
    return redirect(url_for("login"))
