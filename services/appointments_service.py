from datetime import datetime
from flask import abort
from services import users_service
from repositories import appointments_repository
from utils.constant import NAME_DB_KEY, APPOINTMENT_TYPE_LENGTH_MAX
from utils.validators.input_validator import is_valid_input, is_valid_future_date

def get_patient_appointments_info(user_id):
    fetched_appointments = appointments_repository.get_patient_appointments_info(user_id)
    return format_appointment_data(fetched_appointments)

def get_doctor_appointments_info(user_id):
    fetched_appointments = appointments_repository.get_doctor_appointments_info(user_id)
    return format_appointment_data(fetched_appointments)

def format_appointment_data(fetched_appointments):
    formatted_appointments = []

    for appointment in fetched_appointments:
        patient_name = users_service.get_user_info_by_key(appointment.patient_id, NAME_DB_KEY)
        doctor_name = users_service.get_user_info_by_key(appointment.doctor_id, NAME_DB_KEY)
        formatted_appointments.append({
            "id": appointment.id,
            "patient_id": appointment.patient_id,
            "doctor_name": doctor_name,
            "patient_name": patient_name,
            "appointment_type": appointment.appointment_type,
            "time": appointment.time,
            "bg_color": get_bg_color_according_date_past(appointment.time)
        })

    return formatted_appointments

def get_appointment_info_by(user_id, appointment_id):
    appointment = appointments_repository.get_appointment_info_by(user_id, appointment_id)

    if not appointment:
        abort(404)

    return {
        "id": appointment_id,
        "patient_id": user_id,
        "appointment_type": appointment.appointment_type,
        "symptom": appointment.symptom,
        "time_at": appointment.time_at,
    }

def update_appointment_symptom(user_id, appo_id, new_symptom):
    return appointments_repository.update_appointment_symptom(user_id, 
                                                              appo_id, 
                                                              new_symptom)

def add_new_appointment(patient_id, doctor_id, appointment_type, time_at):
    formatted_time_at = time_at.replace("T", " ")
    if is_valid_future_date(formatted_time_at) \
        and is_valid_input(appointment_type, APPOINTMENT_TYPE_LENGTH_MAX):
            return appointments_repository.add_new_appointment(patient_id,
                                                               doctor_id,
                                                               appointment_type,
                                                               formatted_time_at)
    return False

def delete_appointment(appo_id):
    return appointments_repository.delete_appointment(appo_id)

def is_appointment_signed_to_user(user_id, appointment_id):
    is_signed = appointments_repository.is_appointment_signed_to_user(user_id, appointment_id)
    return is_signed

def get_bg_color_according_date_past(date):
    """Checks if parameter (date) has past and return hex-color according to it"""
    date_formatted = datetime.strptime(date, "%d-%m-%Y %H:%M")
    if date_formatted > datetime.now():
        return "#B2D2A4"
    return "#B8B8B8"
