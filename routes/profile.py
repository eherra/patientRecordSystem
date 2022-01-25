from app import app
from flask import render_template
from services import prescriptions, users, appointments, messages
from constant import NAME_DB_KEY, PHONE_DB_KEY

#TODO - hardcoded userID values on method calls -> get ID from session
@app.route("/profile")
def profile():
    # check if is_doctor value in session
    if True:
        return render_doctor_profile()
    else:
        return render_patient_profile()

def render_patient_profile():
    # fetching sent messages of user
    sent_messages = messages.get_sent_messages()

    # fetching received messages of user
    received_messages = messages.get_received_messages(1)

    # fetching name of doctor
    doctor_name = users.get_user_info_by_key(2, NAME_DB_KEY)
    doctor_phone = users.get_user_info_by_key(2, PHONE_DB_KEY)

    # TODO - refactor
    prescription_lists = prescriptions.get_user_prescriptions(1)

    # fetching User Info
    user_info = users.get_user_info(1)

    # Fetching appointments info 
    appointments_info = appointments.get_patient_appointments_info(1)

    return render_template("profile-page.html",
                            sent_messages=sent_messages, 
                            doctor_info=(doctor_name, doctor_phone),
                            received_messages=received_messages,
                            current_prescriptions=prescription_lists['current_prescriptions'],
                            history_prescriptions=prescription_lists['history_prescriptions'],
                            user_info=user_info,
                            appointments_list=appointments_info)

#TODO - hardcoded userID values on method calls -> get ID from session
def render_doctor_profile():
    # fetching sent messages of user
    sent_messages = messages.get_sent_messages(2)

    # fetching received messages of user
    received_messages = messages.get_received_messages(2)

    # fetching User Info
    user_info = users.get_user_info(2)

    # Fetching appointments info 
    appointments_info = appointments.get_doctor_appointments_info(2)

    return render_template("doctor-profile-page.html",
                            sentMessages=sent_messages, 
                            receivedMessages=received_messages,
                            user_info=user_info,
                            appointments_list=appointments_info)