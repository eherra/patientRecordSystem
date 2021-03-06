from flask import redirect, request, render_template, flash, Blueprint
from services import users_service, session_service
from utils.constant import DANGER_CATEGORY, SUCCESS_CATEGORY
from utils.validators.auth_validator import requires_login, requires_session_time_alive
from utils.validators.models.settings_user import SettingsUser

INFORMATION_UPDATED_MESSAGE = "Information updated successfully!"

settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/settings")
@requires_login
@requires_session_time_alive
def settings():
    user_id = session_service.get_user_id()
    user_info = users_service.get_user_info(user_id)
    return render_template("settings/edit-settings-page.html",
                            user_info=user_info)

@settings_bp.route("/settings/update", methods=["POST"])
@requires_login
@requires_session_time_alive
def update_settings():
    user_id = session_service.get_user_id()
    try:
        user_validated = SettingsUser(request.form)
    except ValueError as error:
        flash(str(error), DANGER_CATEGORY)
        return redirect("/settings")

    users_service.update_settings_values(user_id, user_validated)
    flash(INFORMATION_UPDATED_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/settings")
