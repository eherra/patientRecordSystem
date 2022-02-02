from flask import redirect, request, render_template, Blueprint, flash
from services import users
from utils.constant import SUCCESS_CATEGORY
import sys 

register_bp = Blueprint("register", __name__)

@register_bp.route("/register")
def register_page():
    return render_template("auth/register-page.html")

# TODO - this
@register_bp.route("/register/user", methods=["POST"])
def register_user():
    # check if over 3 characters and unique
    username = request.form["username"]

    # check if over 5 characters
    password = request.form["password"]
    is_doctor = request.form["options"] == "doctor"
    created_user_id = users.create_new_user(username, password, is_doctor)
    users.initialize_user_info_values(created_user_id, request.form["name"], 
                                      request.form["phone"], request.form["email"],
                                      request.form["address"], request.form["city"],
                                      request.form["country"])
    flash("New user succesfully registered!", SUCCESS_CATEGORY)
    return redirect("/login")  