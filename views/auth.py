from flask import redirect, request, render_template, flash, Blueprint
from services import auth_service, session_service
from utils.constant import DANGER_CATEGORY, SUCCESS_CATEGORY
from utils.validators.auth_validator import requires_login

LOGIN_ERROR_MESSAGE = "Wrong username or password!"
LOGIN_SUCCESSFULLY_MESSAGE = "You have successfully signed in!"
LOGGED_OUT_SUCCESSFULLY_MESSAGE = "You have successfully signed out!"

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def index():
    if session_service.get_user_id():
        return redirect("/profile")
    return redirect("/sign-in")

@auth_bp.route("/sign-in")
def sign_in_page():
    if session_service.get_user_id():
        return redirect("/profile")
    return render_template("auth/sign-in-page.html")

@auth_bp.route("/sign-in", methods=["POST"])
def process_login():
    logged_user_info = auth_service.check_login_and_return_info(request.form["username"],
                                                                request.form["password"])
    if not logged_user_info:
        flash(LOGIN_ERROR_MESSAGE, DANGER_CATEGORY)
        session_service.set_username_after_login_failure(request.form["username"])
        return redirect("/sign-in")

    session_service.initialize_session(logged_user_info.id, 
                                       logged_user_info.is_doctor)
    flash(LOGIN_SUCCESSFULLY_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/profile")

@auth_bp.route("/sign-out", methods=["POST"])
@requires_login
def process_logout():
    session_service.logout_user()
    flash(LOGGED_OUT_SUCCESSFULLY_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/sign-in")
