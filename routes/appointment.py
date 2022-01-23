from app import app
from flask import redirect, request, render_template
from services import users, prescriptions, appointments
import sys

# TODO - only admin (doctor) can enter this page
@app.route("/appointment/<int:app_id>/patient/<int:patient_id>")
def appointment(app_id, patient_id):
    patient_info = users.get_userInfo(patient_id)
    print(patient_info, file=sys.stdout)

    all_prescriptions = prescriptions.get_all_prescriptions()
    print(all_prescriptions, file=sys.stdout)

    # hard coded userID
    prescriptions_ = prescriptions.get_user_prescriptions(patient_id)
    print(prescriptions_['current_prescriptions'], file=sys.stdout)

    appointment = appointments.get_appointment_info_by(app_id, patient_id)
    print(appointment, file=sys.stdout)

    return render_template("appointment-page.html",
                            patient_info=patient_info,
                            all_prescriptions=all_prescriptions,
                            current_prescriptions=prescriptions_['current_prescriptions'],
                            appointment=appointment)

# TODO - only admin can call these
@app.route("/appointment/<int:app_id>/symptom/<int:user_id>", methods=["POST"])
def update_symptom(app_id, user_id):
    appointments.update_appointment_symptom(app_id, user_id, request.form["symptom"])
    return redirect(f"/appointment/{app_id}/patient/{user_id}")

# TODO - only admin can call these
@app.route("/appointment/prescription/<int:id>", methods=["POST"])
def update_prescription(id):
    return redirect(f"/patient/{id}")