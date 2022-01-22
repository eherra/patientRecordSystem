from app import app
from flask import redirect, request, render_template
from services import users

@app.route("/settings")
def settings():
    return render_template("settings-page.html")

@app.route("/update-settings", methods=["POST"])
def update_settings():
    users.update_settings_values(request.form["name"], request.form["phone"], request.form["email"], 
                                 request.form["address"], request.form["city"], request.form["country"])
    return redirect("/settings")