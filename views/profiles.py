from datetime import datetime
from flask import request, render_template, session, Blueprint
from services import prescriptions_service, users_service, appointments_service, messages_service
from utils.constant import PERSONAL_DOCTOR_ID_DB_KEY, DOCTOR_AVATAR_URL, PATIENT_AVATAR_URL
from utils.validators.auth_validator import requires_login, requires_session_time_alive

profiles_bp = Blueprint("profiles", __name__)

@profiles_bp.route("/profile")
@requires_login
@requires_session_time_alive
def profile():
    # checks if is_doctor value is boolean True in session
    if session.get("is_doctor"):
        return render_doctor_profile()
    return render_patient_profile()

def render_doctor_profile():
    user_id = session["user_id"]
    sent_messages = messages_service.get_sent_messages(user_id)
    received_messages = messages_service.get_received_messages(user_id)
    user_info = users_service.get_user_info(user_id)
    appointments_info = appointments_service.get_doctor_appointments_info(user_id)
    doctor_patients = users_service.get_doctor_patients(user_id)
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
    sent_messages = messages_service.get_sent_messages(user_id)
    received_messages = messages_service.get_received_messages(user_id)
    doctor_id = users_service.get_user_info_by_key(user_id, PERSONAL_DOCTOR_ID_DB_KEY)

    # if doctor_id is none, personal doctor not yet signed to patient
    if doctor_id:
        doctor_info = users_service.get_user_personal_doctor_info(doctor_id)
        all_doctors = None
    else:
        all_doctors = users_service.get_all_doctors()
        doctor_info = None

    # fetching history and current prescriptions list
    prescription_lists = prescriptions_service.get_user_prescriptions(user_id)
    user_info = users_service.get_user_info(user_id)
    appointments_info = appointments_service.get_patient_appointments_info(user_id)

    return render_template("profile/patient-profile-page.html",
                            sent_messages=sent_messages,
                            doctor_info=doctor_info,
                            received_messages=received_messages,
                            prescriptions=prescription_lists,
                            user_info=user_info,
                            appointments_list=appointments_info,
                            all_doctors=all_doctors,
                            avatar_url=PATIENT_AVATAR_URL,
                            doctor_avatar_url=DOCTOR_AVATAR_URL)

@profiles_bp.route("/profile/sign-doctor", methods=["POST"])
@requires_login
@requires_session_time_alive
def sign_personal_doctor():
    user_id = session["user_id"]
    doctor_signed_id = request.form["signed_doctor_id"]
    users_service.update_user_info_by_key(user_id, 
                                          PERSONAL_DOCTOR_ID_DB_KEY, 
                                          doctor_signed_id)
    return render_patient_profile()
    