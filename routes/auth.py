from flask import request, session, jsonify, render_template, redirect, url_for, flash
from data import usuarios

def login():
    if request.method == "POST":
        if request.is_json:
            payload = request.get_json(silent=True) or {}
            username = payload.get("usuario")
            password = payload.get("password")
        else:
            username = request.form.get("usuario")
            password = request.form.get("password")

        if username in usuarios and usuarios[username]["password"] == password:
            session["usuario"] = username
            session["empresa"] = usuarios[username]["empresa"]
            session["rol"] = usuarios[username]["rol"]
            
            if request.is_json:
                return jsonify({
                    "status": "success", 
                    "message": "Logged in", 
                    "redirect": "/dashboard"
                }), 200
            else:
                return redirect(url_for("dashboard"))

        if request.is_json:
            return jsonify({"status": "error", "message": "Credenciales inválidas"}), 401
        else:
            flash("Credenciales inválidas", "danger")
            return redirect(url_for("login"))
            
    return render_template('login.html')

def logout():
    session.clear()
    if request.is_json:
        return jsonify({"status": "success", "message": "Logged out", "redirect": "/login"}), 200
    else:
        return redirect(url_for("login"))