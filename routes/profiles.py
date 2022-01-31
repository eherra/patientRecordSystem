from app import app
from flask import redirect, render_template, session
from services import prescriptions, users, appointments, messages
from utils.constant import PERSONAL_DOCTOR_ID_DB_KEY, DOCTOR_AVATAR_URL, PATIENT_AVATAR_URL
from datetime import datetime
import sys

@app.route("/profile")
def profile():
    # checks if is_doctor value is boolean True in session
    if session.get("is_doctor"):
        return render_doctor_profile()
    elif not session.get("user_id") is None:
        return render_patient_profile()
    else:
        return redirect("/login")

def render_patient_profile():
    user_id = session["user_id"]

    # fetching sent messages of user
    sent_messages = messages.get_sent_messages(user_id)

    # fetching received messages of user
    received_messages = messages.get_received_messages(user_id)

    # fetching name of doctor
    doctor_id = users.get_user_info_by_key(user_id, PERSONAL_DOCTOR_ID_DB_KEY)
    doctor_info = users.get_user_personal_doctor_info(doctor_id)

    # TODO - refactor
    prescription_lists = prescriptions.get_user_prescriptions(user_id)

    # fetching User Info
    user_info = users.get_user_info(user_id)

    # Fetching appointments info 
    appointments_info = appointments.get_patient_appointments_info(user_id)

    return render_template("patient-profile-page.html",
                            sent_messages=sent_messages, 
                            doctor_info=doctor_info,
                            received_messages=received_messages,
                            current_prescriptions=prescription_lists['current_prescriptions'],
                            history_prescriptions=prescription_lists['history_prescriptions'],
                            user_info=user_info,
                            appointments_list=appointments_info, 
                            avatar_url=PATIENT_AVATAR_URL,
                            doctor_avatar_url=DOCTOR_AVATAR_URL)

#TODO - hardcoded userID values on method calls -> get ID from session
def render_doctor_profile():
    user_id = session["user_id"]
    
    # fetching sent messages of user
    sent_messages = messages.get_sent_messages(user_id)

    # fetching received messages of user
    received_messages = messages.get_received_messages(user_id)

    # fetching User Info
    user_info = users.get_user_info(user_id)

    # Fetching appointments info 
    appointments_info = appointments.get_doctor_appointments_info(user_id)
    doctor_patients = users.get_doctor_patients(user_id)

    # TODO - refactor
    time_now = datetime.now().strftime("%Y-%m-%dT%H:%M")

    return render_template("doctor-profile-page.html",
                            user_id=user_id,
                            sent_messages=sent_messages, 
                            received_messages=received_messages,
                            doctor_patients=doctor_patients,
                            user_info=user_info,
                            appointments_list=appointments_info,
                            time_now=time_now,
                            avatar_url=DOCTOR_AVATAR_URL)