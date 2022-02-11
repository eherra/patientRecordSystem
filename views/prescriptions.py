from flask import redirect, request, flash, Blueprint
from services import prescriptions
from utils.constant import SUCCESS_CATEGORY
from utils.validators.auth_validator import requires_doctor_role

NEW_PRESCRIPTION_ADDED_MESSAGE = "New prescription added successfully!"
PRESCRIPTION_ADDED_TO_PATIENT_MESSAGE = "Prescription added to patient successfully!"
PRESCRIPTION_DELETED_FROM_PATIENT_MESSAGE = "Prescription removed from patient successfully!"

prescriptions_bp = Blueprint("prescriptions", __name__)

@prescriptions_bp.route("/add-prescription", methods=["POST"])
@requires_doctor_role
def add_prescription():
    prescriptions.create_new_prescription(request.form["prescription_name"],
                                          request.form["amount_per_day"])
    flash(NEW_PRESCRIPTION_ADDED_MESSAGE, SUCCESS_CATEGORY)               
    return redirect("/profile")

@prescriptions_bp.route("/appointment/<int:appli_id>/prescription/<int:prescription_id>/patient/<int:user_id>", methods=["POST"])
@requires_doctor_role
def update_user_prescription(appli_id, prescription_id, user_id):
    is_visible = request.form["isVisible"] == "True"
    prescriptions.update_prescription_from_user(user_id, prescription_id, is_visible)
    if is_visible:
        flash(PRESCRIPTION_ADDED_TO_PATIENT_MESSAGE, SUCCESS_CATEGORY)                       
    else:
        flash(PRESCRIPTION_DELETED_FROM_PATIENT_MESSAGE, SUCCESS_CATEGORY)                       
    return redirect(f"/appointment/{appli_id}/patient/{user_id}")
