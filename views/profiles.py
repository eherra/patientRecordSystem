from flask import redirect, render_template, session, Blueprint
from services import prescriptions, users, appointments, messages
from utils.constant import PERSONAL_DOCTOR_ID_DB_KEY, DOCTOR_AVATAR_URL, PATIENT_AVATAR_URL
from utils.auth_validator import requires_login
from datetime import datetime

profiles_bp = Blueprint("profiles", __name__)

@profiles_bp.route("/profile")
@requires_login
def profile():
    # checks if is_doctor value is boolean True in session
    if session.get("is_doctor"):
        return render_doctor_profile()
    
    return render_patient_profile()
    
def render_doctor_profile():
    user_id = session["user_id"]
    
    # fetching sent messages of the user
    sent_messages = messages.get_sent_messages(user_id)

    # fetching received messages of the user
    received_messages = messages.get_received_messages(user_id)

    # fetching User Info (name, phone, email, address)
    user_info = users.get_user_info(user_id)

    # Fetching appointments info of the doctor
    appointments_info = appointments.get_doctor_appointments_info(user_id)
    doctor_patients = users.get_doctor_patients(user_id)

    time_now = datetime.now().strftime("%Y-%m-%dT%H:%M")

    return render_template("profile/doctor-profile-page.html",
                            user_id=user_id,
                            sent_messages=sent_messages, 
                            received_messages=received_messages,
                            doctor_patients=doctor_patients,
                            user_info=user_info,
                            appointments_list=appointments_info,
                            time_now=time_now,
                            avatar_url=DOCTOR_AVATAR_URL)

def render_patient_profile():
    user_id = session["user_id"]

    # fetching sent messages of user
    sent_messages = messages.get_sent_messages(user_id)

    # fetching received messages of user
    received_messages = messages.get_received_messages(user_id)

    # fetching name of doctor
    doctor_id = users.get_user_info_by_key(user_id, PERSONAL_DOCTOR_ID_DB_KEY)
    doctor_info = users.get_user_personal_doctor_info(doctor_id)

    # fetching history and current prescriptions list
    prescription_lists = prescriptions.get_user_prescriptions(user_id)

    # fetching User Info
    user_info = users.get_user_info(user_id)

    # Fetching appointments info 
    appointments_info = appointments.get_patient_appointments_info(user_id)

    return render_template("profile/patient-profile-page.html",
                            sent_messages=sent_messages, 
                            doctor_info=doctor_info,
                            received_messages=received_messages,
                            prescriptions=prescription_lists,
                            user_info=user_info,
                            appointments_list=appointments_info, 
                            avatar_url=PATIENT_AVATAR_URL,
                            doctor_avatar_url=DOCTOR_AVATAR_URL)