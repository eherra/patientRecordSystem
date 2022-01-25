from app import app
from flask import render_template, request, redirect
from services import prescriptions, users, appointments, messages
from constant import NAME_DB_KEY, PHONE_DB_KEY
from datetime import datetime
import sys

#TODO - hardcoded userID values on method calls -> get ID from session
@app.route("/profile")
def profile():
    # check if is_doctor value in session
    if True:
        return render_doctor_profile()
    else:
        return render_patient_profile()

def render_patient_profile():
    # TODO - fetch from session
    user_id = 1

    # fetching sent messages of user
    sent_messages = messages.get_sent_messages(user_id)

    # fetching received messages of user
    received_messages = messages.get_received_messages(user_id)

    # fetching name of doctor
    doctor_name = users.get_user_info_by_key(2, NAME_DB_KEY)
    doctor_phone = users.get_user_info_by_key(2, PHONE_DB_KEY)

    # TODO - refactor
    prescription_lists = prescriptions.get_user_prescriptions(user_id)

    # fetching User Info
    user_info = users.get_user_info(user_id)

    # Fetching appointments info 
    appointments_info = appointments.get_patient_appointments_info(user_id)

    return render_template("profile-page.html",
                            sent_messages=sent_messages, 
                            doctor_info=(doctor_name, doctor_phone),
                            received_messages=received_messages,
                            current_prescriptions=prescription_lists['current_prescriptions'],
                            history_prescriptions=prescription_lists['history_prescriptions'],
                            user_info=user_info,
                            appointments_list=appointments_info, 
                            avatar_url="/static/photos/patientAvatar.png")

#TODO - hardcoded userID values on method calls -> get ID from session
def render_doctor_profile():
    # TODO - fetch from session
    user_id = 2
    
    # fetching sent messages of user
    sent_messages = messages.get_sent_messages(user_id)

    # fetching received messages of user
    received_messages = messages.get_received_messages(user_id)

    # fetching User Info
    user_info = users.get_user_info(user_id)

    # Fetching appointments info 
    appointments_info = appointments.get_doctor_appointments_info(user_id)

    time_now = datetime.now().strftime("%Y-%m-%dT%H:%M")
    print(time_now, file=sys.stdout)

    return render_template("doctor-profile-page.html",
                            user_id=user_id,
                            sentMessages=sent_messages, 
                            receivedMessages=received_messages,
                            user_info=user_info,
                            appointments_list=appointments_info,
                            time_now=time_now,
                            avatar_url="/static/photos/doctorAvatar.png")