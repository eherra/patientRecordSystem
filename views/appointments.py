from flask import redirect, request, render_template, flash, Blueprint
from services import users, prescriptions, appointments
from utils.constant import SUCCESS_CATEGORY
from utils.auth_validator import requires_login, requires_doctor_role

SYMPTOM_UPDATE_MESSAGE = "Symptom updated successfully"
APPOINTMENT_BOOKED_MESSAGE = "Appointment booked successfully!"
APPOINTMENT_DELETED_MESSAGE = "Appointment deleted successfully!"

appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route("/appointment/<int:appo_id>/patient/<int:patient_id>")
@requires_login
def appointment(appo_id, patient_id):
    patient_info = users.get_user_info(patient_id)

    # prescriptions which patient doenst have signed to
    not_signed_prescriptions = prescriptions.get_all_not_signed_prescription(patient_id)

    signed_prescriptions = prescriptions.get_user_prescriptions(patient_id)

    appointment = appointments.get_appointment_info_by(patient_id, appo_id)

    return render_template("appointment/appointment-page.html",
                            patient_info=patient_info,
                            all_prescriptions=not_signed_prescriptions,
                            current_prescriptions=signed_prescriptions['current_prescriptions'],
                            appointment=appointment)

@appointments_bp.route("/appointment/<int:appo_id>/symptom/<int:user_id>", methods=["POST"])
@requires_doctor_role
def update_symptom(appo_id, user_id):
    appointments.update_appointment_symptom(user_id, appo_id, request.form["symptom"])
    flash(SYMPTOM_UPDATE_MESSAGE, SUCCESS_CATEGORY)
    return redirect(f"/appointment/{appo_id}/patient/{user_id}")

@appointments_bp.route("/appointment/book/<int:doctor_id>", methods=["POST"])
@requires_doctor_role
def book_appointment(doctor_id):
    appointments.add_new_appointment(request.form["patient_id"], doctor_id,
                                     request.form["appointment_type"], request.form["appointment_date"])
    flash(APPOINTMENT_BOOKED_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/profile")

@appointments_bp.route("/appointment/<int:appo_id>/delete")
@requires_doctor_role
def delete_appointment(appo_id):
    appointments.delete_appointment(appo_id)
    flash(APPOINTMENT_DELETED_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/profile")