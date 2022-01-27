from app import app
from flask import redirect, request, render_template, session
from services import users

@app.route("/settings")
def settings():
    return render_template("settings-page.html")

# TODO - get user_id from session
@app.route("/settings/update", methods=["POST"])
def update_settings():
    user_id = session["user_id"]
    users.update_settings_values(user_id, request.form["name"], request.form["phone"], request.form["email"], 
                                 request.form["address"], request.form["city"], request.form["country"])
    return redirect("/settings")