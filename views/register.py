from flask import redirect, request, render_template, Blueprint, flash, session
from services import users_service
from views import auth
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
        initialize_failed_registering_attempt_data(request.form)
        return redirect("/register")

    created_user_id = users_service.create_new_user(user_validated)
    if not created_user_id:
        flash(FAILED_USER_REGISTRATION_MESSAGE, DANGER_CATEGORY)
        return redirect("/register")
        
    users_service.initialize_user_info_values(created_user_id, user_validated)
    auth.initialize_session(created_user_id, user_validated.is_doctor)
    delete_failed_registration_attempt_data()
    flash(SUCCESFULLY_USER_REGISTRATION_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/profile")

def initialize_failed_registering_attempt_data(form):
    """If registration has failed with incorrect data, filled input fields saved to session"""
    session["register_username"] = form["username"]
    session["register_password"] = form["password"]
    session["register_name"] = form["name"]
    session["register_email"] = form["email"]
    session["register_phone"] = form["phone"]
    session["register_address"] = form["address"]
    session["register_city"] = form["city"]
    session["register_country"] = form["country"]

def delete_failed_registration_attempt_data():
    """Deleting information saved from failed registration attempts after registration succeeded"""
    session.pop("register_username", None)
    session.pop("register_password")
    session.pop("register_name", None)
    session.pop("register_email", None)
    session.pop("register_phone", None)
    session.pop("register_address", None)
    session.pop("register_city", None)
    session.pop("register_country", None)
    