from app import app
from flask import redirect, request, render_template, session, abort, flash
from services import users

@app.route("/settings")
def settings():
    user_id = session.get("user_id")
    if user_id is None:
        abort(401, description="User not logged in")
        
    user_info = users.get_user_info(user_id)
    return render_template("settings-page.html",
                            user_info=user_info)

@app.route("/settings/update", methods=["POST"])
def update_settings():
    user_id = session.get("user_id")
    if user_id is None:
        abort(401, description="User not logged in")
 
    users.update_settings_values(user_id, request.form["name"], request.form["phone"], request.form["email"], 
                                 request.form["address"], request.form["city"], request.form["country"])
    flash("Information updated successfully!", "success")
    return redirect("/settings")