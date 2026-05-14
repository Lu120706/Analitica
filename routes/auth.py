from flask import request, session, jsonify
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
            return jsonify({"status": "success", "message": "Logged in", "redirect": "/api/dashboard"}), 200

        return jsonify({"status": "error", "message": "Credenciales inválidas"}), 401

    return jsonify({"status": "ready", "message": "Envía POST con usuario y password"}), 200

def logout():
    session.clear()
    return jsonify({"status": "success", "message": "Logged out"}), 200
