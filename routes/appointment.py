from pickle import FALSE
from app import app
from flask import redirect, request, render_template
from services import users, prescriptions, appointments

# TODO - only admin (doctor) can enter this page
@app.route("/appointment/<int:appli_id>/patient/<int:patient_id>")
def appointment(appli_id, patient_id):
    patient_info = users.get_user_info(patient_id)

    # prescriptions which patient doenst have signed to
    not_signed_prescriptions = prescriptions.get_all_not_signed_prescription(patient_id)

    signed_prescriptions = prescriptions.get_user_prescriptions(patient_id)

    appointment = appointments.get_appointment_info_by(patient_id, appli_id)

    return render_template("appointment-page.html",
                            patient_info=patient_info,
                            all_prescriptions=not_signed_prescriptions,
                            current_prescriptions=signed_prescriptions['current_prescriptions'],
                            appointment=appointment)

# TODO - only admin can call these
@app.route("/appointment/<int:appli_id>/symptom/<int:user_id>", methods=["POST"])
def update_symptom(appli_id, user_id):
    appointments.update_appointment_symptom(user_id, appli_id, request.form["symptom"])
    return redirect(f"/appointment/{appli_id}/patient/{user_id}")

# TODO - only admin can call these
@app.route("/appointment/<int:appli_id>/prescription/<int:prescription_id>/patient/<int:user_id>", methods=["POST"])
def update_prescription(appli_id, prescription_id, user_id):
    isVisible = request.form["isVisible"] == "True"
    prescriptions.update_prescription_from_user(user_id, prescription_id, isVisible)
    return redirect(f"/appointment/{appli_id}/patient/{user_id}")