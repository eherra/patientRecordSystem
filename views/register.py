from flask import redirect, request, render_template, Blueprint, flash
from services import users_service, session_service
from utils.constant import SUCCESS_CATEGORY, DANGER_CATEGORY
from utils.validators.models.registration_user import RegistrationUser

FAILED_USER_REGISTRATION_MESSAGE = "Something went wrong!"
SUCCESFULLY_USER_REGISTRATION_MESSAGE = "New user succesfully registered!"

register_bp = Blueprint("register", __name__)

@register_bp.route("/register")
def register_page():
    return render_template("auth/register-page.html")

@register_bp.route("/register/user", methods=["POST"])
def register_user():
    # the RegistrationUser class handles the validation of the form inputs
    try:
        user_validated = RegistrationUser(request.form)
    except ValueError as error:
        flash(str(error), DANGER_CATEGORY)
        session_service.initialize_failed_registering_attempt_data(request.form)
        return redirect("/register")

    created_user_id = users_service.create_new_user(user_validated)
    if not created_user_id:
        flash(FAILED_USER_REGISTRATION_MESSAGE, DANGER_CATEGORY)
        return redirect("/register")
        
    users_service.initialize_user_info_values(created_user_id, user_validated)
    session_service.initialize_session(created_user_id, user_validated.is_doctor)
    session_service.delete_failed_registration_attempt_data()
    flash(SUCCESFULLY_USER_REGISTRATION_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/profile")
