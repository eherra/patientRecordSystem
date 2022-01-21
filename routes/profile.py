from app import app
from flask import render_template
from services import prescriptions, users, appointments, messages
#TODO - refactor to use services

#TODO - hardcoded userID values on method calls -> get ID from session
@app.route("/")
def index():
    # fetching sent messages of user
    sentMessages = messages.get_sent_messages(1)

    # fetching received messages of user
    receivedMessages = messages.get_received_messages(1)

    # fetching name of doctor
    doctor_name = users.get_userInfo_by_key(2, 'name')
    doctor_phone = users.get_userInfo_by_key(2, 'phone')

    # TODO - refactor
    prescription_lists = prescriptions.get_user_prescriptions(1)

    # fetching User Info
    userInfo = users.get_userInfo(1)

    # Fetching appointments info 
    appointmentsInfo = appointments.get_appointments_info(1)

    return render_template("profile-page.html",
                            sentMessages=sentMessages, 
                            doctorInfo=(doctor_name, doctor_phone),
                            receivedMessages=receivedMessages,
                            current_prescriptions=prescription_lists['current_prescriptions'],
                            history_prescriptions=prescription_lists['history_prescriptions'],
                            user_info=userInfo,
                            appointments_list=appointmentsInfo)