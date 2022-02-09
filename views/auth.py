from flask import session, redirect, request, render_template, flash, Blueprint
from services import auth
from utils.constant import DANGER_CATEGORY, SUCCESS_CATEGORY
from utils.validators.auth_validator import requires_login

LOGIN_ERROR_MESSAGE = "Wrong username or password!"
LOGIN_SUCCESSFULLY_MESSAGE = "You have successfully logged in!"
LOGGED_OUT_SUCCESSFULLY_MESSAGE = "You have successfully logged out!"

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
@auth_bp.route("/login")
def login_page():
    if session.get("user_id"):
        return redirect("/profile")

    return render_template("auth/login-page.html")
 
@auth_bp.route("/login", methods=["POST"])
def process_login():
    logged_user_info = auth.check_login_and_return_info(request.form["username"], 
                                                        request.form["password"])
    if logged_user_info:
        session["user_id"] = logged_user_info.id
        session["is_doctor"] = logged_user_info.is_doctor
        flash(LOGIN_SUCCESSFULLY_MESSAGE, SUCCESS_CATEGORY)
        return redirect("/profile")

    flash(LOGIN_ERROR_MESSAGE, DANGER_CATEGORY)
    return redirect("/login")

@auth_bp.route("/logout", methods=["POST"])
@requires_login
def logout():
    del session["user_id"]
    del session["is_doctor"]
    flash(LOGGED_OUT_SUCCESSFULLY_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/login")