from datetime import datetime, timezone, timedelta
from flask import session, redirect, request, render_template, flash, Blueprint
from services import auth_service
from utils.constant import DANGER_CATEGORY, SUCCESS_CATEGORY, SESSION_ALIVE_TIME_MINUTES
from utils.validators.auth_validator import requires_login

LOGIN_ERROR_MESSAGE = "Wrong username or password!"
LOGIN_SUCCESSFULLY_MESSAGE = "You have successfully signed in!"
LOGGED_OUT_SUCCESSFULLY_MESSAGE = "You have successfully signed out!"

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def index():
    if session.get("user_id"):
        return redirect("/profile")
    return redirect("/sign-in")

@auth_bp.route("/sign-in")
def sign_in_page():
    if session.get("user_id"):
        return redirect("/profile")
    return render_template("auth/sign-in-page.html")

@auth_bp.route("/sign-in", methods=["POST"])
def process_login():
    logged_user_info = auth_service.check_login_and_return_info(request.form["username"],
                                                                request.form["password"])
    if not logged_user_info:
        flash(LOGIN_ERROR_MESSAGE, DANGER_CATEGORY)
        session["filled_username"] = request.form["username"]
        return redirect("/sign-in")

    initialize_session(logged_user_info.id, logged_user_info.is_doctor)
    flash(LOGIN_SUCCESSFULLY_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/profile")

@auth_bp.route("/sign-out", methods=["POST"])
@requires_login
def process_logout():
    del session["user_id"]
    del session["is_doctor"]
    del session["session_end_time"]
    flash(LOGGED_OUT_SUCCESSFULLY_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/sign-in")
    
def initialize_session(user_id, is_doctor):
    session["user_id"] = user_id
    session["is_doctor"] = is_doctor
    # Initializing session ending time to current time + minutes set as SESSION_ALIVE_TIME_MINUTES
    session["session_end_time"] = datetime.now(timezone.utc) + timedelta(minutes=SESSION_ALIVE_TIME_MINUTES)
    # if there was failed attempts to login, filled username deletion from the session
    del session["filled_username"]