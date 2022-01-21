from app import app
from flask import redirect, render_template, request
from db import db
from services import prescriptions, users, appointments, messages
import sys
#TODO - refactor to use services

#TODO - hardcoded userID values on method calls -> get ID from session
@app.route("/")
def index():
    # fetching sent messages of user
    sentMessages = messages.get_sent_messages(1)

    # fetching received messages of user
    receivedMessages = messages.get_received_messages(1)

    # fetching name of doctor
    doctorResult = db.session.execute("SELECT value FROM UserInfo WHERE user_id = 2 AND key='name'")
    doctorName = doctorResult.fetchone()[0]
    print(f'doctor name: {doctorName}', file=sys.stdout)

    # TODO - refactor
    prescription_lists = prescriptions.get_user_prescriptions(1)
    print(prescription_lists['current_prescriptions'], file=sys.stdout)

    # fetching User Info
    userInfo = users.get_userInfo(1)
    print(userInfo, file=sys.stdout)

    # Fetching appointments info 
    appointmentsInfo = appointments.get_appointments_info(1)

    return render_template("profile-page.html",
                            sentMessages=sentMessages, 
                            doctorName=doctorName,
                            receivedMessages=receivedMessages,
                            current_prescriptions=prescription_lists['current_prescriptions'],
                            history_prescriptions=prescription_lists['history_prescriptions'],
                            user_info=userInfo,
                            appointments_list=appointmentsInfo)