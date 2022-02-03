from flask import redirect, request, render_template, session, flash, Blueprint
from services import users
from utils.constant import SUCCESS_CATEGORY
from utils.validators.auth_validator import requires_login

INFORMATION_UPDATED_MESSAGE = "Information updated successfully!"

settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/settings")
@requires_login
def settings():
    user_id = session.get("user_id")        
    user_info = users.get_user_info(user_id)
    return render_template("settings/edit-settings-page.html",
                            user_info=user_info)

@settings_bp.route("/settings/update", methods=["POST"])
@requires_login
def update_settings():
    user_id = session.get("user_id") 
    users.update_settings_values(user_id, request.form["name"], 
                                 request.form["phone"], request.form["email"], 
                                 request.form["address"], request.form["city"], 
                                 request.form["country"])
    flash(INFORMATION_UPDATED_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/settings")