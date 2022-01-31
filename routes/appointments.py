from app import app
from flask import redirect, request, render_template, session, abort, flash
from services import users, prescriptions, appointments
import sys

# TODO - only admin (doctor) can enter this page
@app.route("/appointment/<int:appo_id>/patient/<int:patient_id>")
def appointment(appo_id, patient_id):
    patient_info = users.get_user_info(patient_id)

    # prescriptions which patient doenst have signed to
    not_signed_prescriptions = prescriptions.get_all_not_signed_prescription(patient_id)

    signed_prescriptions = prescriptions.get_user_prescriptions(patient_id)

    appointment = appointments.get_appointment_info_by(patient_id, appo_id)

    return render_template("appointment-page.html",
                            patient_info=patient_info,
                            all_prescriptions=not_signed_prescriptions,
                            current_prescriptions=signed_prescriptions['current_prescriptions'],
                            appointment=appointment)

@app.route("/appointment/<int:appo_id>/symptom/<int:user_id>", methods=["POST"])
def update_symptom(appo_id, user_id):
    if not session.get("is_doctor"):
        abort(401, description = "Not authorized call")

    appointments.update_appointment_symptom(user_id, appo_id, request.form["symptom"])
    flash("Symptom updated successfully", "success")
    return redirect(f"/appointment/{appo_id}/patient/{user_id}")

@app.route("/appointment/book/<int:doctor_id>", methods=["POST"])
def book_appointment(doctor_id):
    if not session.get("is_doctor"):
        abort(401, description = "Not authorized call")

    appointments.add_new_appointment(request.form["patient_id"], doctor_id,
                                     request.form["appointment_type"], request.form["appointment_date"])
    flash("Appointment booked successfully!", "success")
    return redirect("/profile")

@app.route("/appointment/<int:appo_id>/delete")
def delete_appointment(appo_id):
    if not session.get("is_doctor"):
        abort(401, description = "Not authorized call")

    appointments.delete_appointment(appo_id)
    flash("Appointment deleted successfully!", "success")
    return redirect("/profile")