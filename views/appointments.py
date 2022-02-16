from flask import redirect, request, render_template, flash, Blueprint
from services import users_service, prescriptions_service, appointments_service
from utils.constant import SUCCESS_CATEGORY, DANGER_CATEGORY
from utils.validators.auth_validator import requires_login, requires_doctor_role, \
    requires_appointment_signed_to_user, requires_session_time_alive

SYMPTOM_UPDATE_MESSAGE = "Symptom updated successfully"
BOOKED_APPOINTMENT_MESSAGE = "Appointment booked successfully!"
DELETED_APPOINTMENT_MESSAGE = "Appointment deleted successfully!"
INVALID_APPOINTMENT_MESSAGE = "Invalid appointment inputs!"

appointments_bp = Blueprint("appointments", __name__)

@appointments_bp.route("/appointment/<int:appo_id>/patient/<int:patient_id>")
@requires_login
@requires_session_time_alive
@requires_appointment_signed_to_user
def appointment(appo_id, patient_id):
    patient_info = users_service.get_user_info(patient_id)

    # prescriptions which patient doenst have signed to
    not_signed_prescriptions = prescriptions_service.get_all_not_signed_prescription(patient_id)

    signed_prescriptions = prescriptions_service.get_user_prescriptions(patient_id)

    appointments_info = appointments_service.get_appointment_info_by(patient_id, appo_id)

    return render_template("appointment/appointment-page.html",
                            patient_info=patient_info,
                            all_prescriptions=not_signed_prescriptions,
                            current_prescriptions=signed_prescriptions["current_prescriptions"],
                            appointment=appointments_info)

@appointments_bp.route("/appointment/<int:appo_id>/symptom/<int:user_id>", methods=["POST"])
@requires_doctor_role
@requires_session_time_alive
def update_symptom(appo_id, user_id):
    appointments_service.update_appointment_symptom(user_id, appo_id, request.form["symptom"])
    flash(SYMPTOM_UPDATE_MESSAGE, SUCCESS_CATEGORY)
    return redirect(f"/appointment/{appo_id}/patient/{user_id}")

@appointments_bp.route("/appointment/book/<int:doctor_id>", methods=["POST"])
@requires_doctor_role
@requires_session_time_alive
def book_appointment(doctor_id):
    is_success = appointments_service.add_new_appointment(request.form["patient_id"],
                                                  doctor_id,
                                                  request.form["appointment_type"],
                                                  request.form["appointment_date"])
    if is_success:
        flash(BOOKED_APPOINTMENT_MESSAGE, SUCCESS_CATEGORY)
    else:
        flash(INVALID_APPOINTMENT_MESSAGE, DANGER_CATEGORY)
    return redirect("/profile")

@appointments_bp.route("/appointment/<int:appo_id>", methods=["POST"])
@requires_doctor_role
@requires_session_time_alive
def delete_appointment(appo_id):
    appointments_service.delete_appointment(appo_id)
    flash(DELETED_APPOINTMENT_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/profile")
