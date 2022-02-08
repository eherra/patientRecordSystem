from flask import redirect, request, render_template, Blueprint, flash, abort
from services import users
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
        return redirect("/register") 

    created_user_id = users.create_new_user(user_validated) 
    if created_user_id:
        users.initialize_user_info_values(created_user_id, user_validated)
        flash(SUCCESFULLY_USER_REGISTRATION_MESSAGE, SUCCESS_CATEGORY)
        return redirect("/login") 
    
    flash(FAILED_USER_REGISTRATION_MESSAGE, DANGER_CATEGORY)
    return redirect("/register") 

