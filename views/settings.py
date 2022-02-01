from flask import redirect, request, render_template, session, abort, flash, Blueprint
from services import users

settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/settings")
def settings():
    user_id = session.get("user_id")
    if user_id is None:
        abort(401, description="User not logged in")
        
    user_info = users.get_user_info(user_id)
    return render_template("settings/settings-page.html",
                            user_info=user_info)

@settings_bp.route("/settings/update", methods=["POST"])
def update_settings():
    user_id = session.get("user_id")
    if user_id is None:
        abort(401, description="User not logged in")
 
    users.update_settings_values(user_id, request.form["name"], request.form["phone"], request.form["email"], 
                                 request.form["address"], request.form["city"], request.form["country"])
    flash("Information updated successfully!", "success")
    return redirect("/settings")