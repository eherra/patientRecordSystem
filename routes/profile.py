from app import app
from flask import render_template
from services import prescriptions, users, appointments, messages
from constant import NAME_DB_KEY, PHONE_DB_KEY

#TODO - hardcoded userID values on method calls -> get ID from session
@app.route("/patient-profile")
def patient():
    # fetching sent messages of user
    sent_messages = messages.get_sent_messages()

    # fetching received messages of user
    received_messages = messages.get_received_messages(1)

    # fetching name of doctor
    doctor_name = users.get_userInfo_by_key(2, NAME_DB_KEY)
    doctor_phone = users.get_userInfo_by_key(2, PHONE_DB_KEY)

    # TODO - refactor
    prescription_lists = prescriptions.get_user_prescriptions(1)

    # fetching User Info
    user_info = users.get_userInfo(1)

    # Fetching appointments info 
    appointments_info = appointments.get_appointments_info_by_patientId(1)

    return render_template("profile-page.html",
                            sentMessages=sent_messages, 
                            doctorInfo=(doctor_name, doctor_phone),
                            receivedMessages=received_messages,
                            current_prescriptions=prescription_lists['current_prescriptions'],
                            history_prescriptions=prescription_lists['history_prescriptions'],
                            user_info=user_info,
                            appointments_list=appointments_info)

#TODO - hardcoded userID values on method calls -> get ID from session
@app.route("/doctor-profile")
def doctor():
    # fetching sent messages of user
    sent_messages = messages.get_sent_messages(2)

    # fetching received messages of user
    received_messages = messages.get_received_messages(2)

    # fetching User Info
    user_info = users.get_userInfo(2)

    # Fetching appointments info 
    appointments_info = appointments.get_appointments_info_by_doctorId(2)

    return render_template("doctor-profile-page.html",
                            sentMessages=sent_messages, 
                            receivedMessages=received_messages,
                            user_info=user_info,
                            appointments_list=appointments_info)