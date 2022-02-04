from flask import redirect, request, render_template, Blueprint, flash, abort
from services import users
from utils.constant import SUCCESS_CATEGORY, DANGER_CATEGORY
from utils.validators.models.registration_user import RegistrationUser
import sys 

register_bp = Blueprint("register", __name__)

@register_bp.route("/register")
def register_page():
    return render_template("auth/register-page.html")

# TODO - this
@register_bp.route("/register/user", methods=["POST"])
def register_user():
    # the RegistrationUser class handles the validation of the form inputs
    try:
        user_validated = RegistrationUser(request.form)
    except ValueError:
        # print valueError message as a flash, danger category color
        flash("some wrong", DANGER_CATEGORY)
        return redirect("/register") 
    except KeyError:
        abort(500)

    created_user_id = users.create_new_user(user_validated) 
    if created_user_id:
        users.initialize_user_info_values(created_user_id, user_validated)
        flash("New user succesfully registered!", SUCCESS_CATEGORY)
        return redirect("/login") 
    
    flash("Something went wrong!", DANGER_CATEGORY)
    return redirect("/register") 

