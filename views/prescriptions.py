from flask import redirect, request, flash, Blueprint
from services import prescriptions_service
from utils.constant import SUCCESS_CATEGORY
from utils.validators.auth_validator import requires_doctor_role, requires_session_time_alive

NEW_PRESCRIPTION_ADDED_MESSAGE = "New prescription added successfully!"
ADDED_PRESCRIPTION_TO_PATIENT_MESSAGE = "Prescription added to patient successfully!"
DELETED_PRESCRIPTION_FROM_PATIENT_MESSAGE = "Prescription removed from patient successfully!"

prescriptions_bp = Blueprint("prescriptions", __name__)

@prescriptions_bp.route("/create-prescription", methods=["POST"])
@requires_doctor_role
@requires_session_time_alive
def create_prescription():
    prescriptions_service.create_new_prescription(request.form["prescription_name"],
                                                  request.form["amount_per_day"])
    flash(NEW_PRESCRIPTION_ADDED_MESSAGE, SUCCESS_CATEGORY)               
    return redirect("/profile")

@prescriptions_bp.route("/appointment/<int:appli_id>/prescription/<int:prescription_id>/patient/<int:user_id>", methods=["POST"])
@requires_doctor_role
@requires_session_time_alive
def update_user_prescription(appli_id, prescription_id, user_id):
    is_visible = request.form["is_visible"] == "True"
    prescriptions_service.update_prescription_from_user(user_id,
                                                        prescription_id,
                                                        is_visible)
    if is_visible:
        flash(ADDED_PRESCRIPTION_TO_PATIENT_MESSAGE, SUCCESS_CATEGORY)                       
    else:
        flash(DELETED_PRESCRIPTION_FROM_PATIENT_MESSAGE, SUCCESS_CATEGORY)                       
    return redirect(f"/appointment/{appli_id}/patient/{user_id}")
