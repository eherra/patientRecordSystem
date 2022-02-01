from flask import session, redirect, request, render_template, flash, Blueprint
from services import auth
import sys 

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def index():
    if session.get("user_id"):
        return redirect("/profile")

    return redirect("/login")

@auth_bp.route("/login")
def login_page():
    return render_template("auth/login-page.html")
 
@auth_bp.route("/login", methods=["POST"])
def process_login():
    logged_user_info = auth.check_login_and_return_info(request.form["username"], 
                                                        request.form["password"])

    if logged_user_info:
        session["user_id"] = logged_user_info[0]
        session["is_doctor"] = logged_user_info[2]
    else: 
        flash("Wrong username or password", "danger")
        return redirect("/login")

    return redirect("/profile")

@auth_bp.route("/logout")
def logout():
    del session["user_id"]
    del session["is_doctor"]
    return redirect("/login")

