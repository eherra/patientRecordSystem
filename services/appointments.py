from db import db
from services import users
from flask import abort
from utils.constant import TIME_FORMAT, NAME_DB_KEY, APPOINTMENT_TYPE_LENGTH_MAX, SYMPTOM_LENGTH_MAX
from utils.validators.input_validator import is_valid_input, is_valid_future_date
from datetime import datetime
import sys

APPOINTMENTS_INFO_BY_ID_QUERY = "SELECT appointment_type, symptom, TO_CHAR(time_at, :time_format) AS time_at \
                                 FROM   appointments \
                                 WHERE  patient_id = :user_id \
                                 AND    id = :appointment_id"

DOCTOR_ALL_APPOINTMENTS_INFO_QUERY = "SELECT   id, patient_id, doctor_id, appointment_type, TO_CHAR(time_at, :time_format) AS time \
                                      FROM     appointments \
                                      WHERE    doctor_id = :user_id \
                                      ORDER BY time_at DESC"

PATIENT_ALL_APPOINTMENTS_INFO_QUERY = "SELECT   id, patient_id, doctor_id, appointment_type, TO_CHAR(time_at, :time_format) AS time \
                                       FROM     appointments \
                                       WHERE    patient_id = :user_id \
                                       ORDER BY time_at DESC"

DELETE_APPOINTMENT_QUERY = "DELETE \
                            FROM  appointments \
                            WHERE id = :appointment_id"

UPDATE_USERINFO_BY_KEY_QUERY = "UPDATE appointments \
                                SET    symptom = :new_symptom \
                                WHERE  patient_id = :user_id \
                                AND    id = :appointment_id"

CREATE_NEW_APPOINTMENT_QUERY = "INSERT INTO appointments (patient_id, doctor_id, appointment_type, time_at) \
                                VALUES (:patient_id, :doctor_id, :appointment_type, (TIMESTAMP :time_at))"


def get_patient_appointments_info(user_id):
    try:
        fetched_appointments = db.session.execute(PATIENT_ALL_APPOINTMENTS_INFO_QUERY,
                                                 {"user_id": user_id, 
                                                  "time_format": TIME_FORMAT}
                                                  ).fetchall()
        return format_appointment_data(fetched_appointments)
    except: 
        abort(500)

def get_doctor_appointments_info(user_id):
    try:
        fetched_appointments = db.session.execute(DOCTOR_ALL_APPOINTMENTS_INFO_QUERY,
                                                 {"user_id": user_id, 
                                                  "time_format": TIME_FORMAT}
                                                  ).fetchall()
        return format_appointment_data(fetched_appointments)
    except:
        abort(500)

def format_appointment_data(fetched_appointments):
    formatted_appointments = []

    for appointment in fetched_appointments:
        patient_name = users.get_user_info_by_key(appointment.patient_id, NAME_DB_KEY)
        doctor_name = users.get_user_info_by_key(appointment.doctor_id, NAME_DB_KEY)
        formatted_appointments.append({
            "id": appointment.id,
            "patient_id": appointment.patient_id,
            'doctor_name': doctor_name,
            "patient_name": patient_name,
            'appointment_type': appointment.appointment_type,
            'time': appointment.time,
            'bg_color': get_bg_color_according_date_past(appointment.time)
        })

    return formatted_appointments

def get_appointment_info_by(user_id, appointment_id):
    try: 
        appointment = db.session.execute(APPOINTMENTS_INFO_BY_ID_QUERY,
                                        {"appointment_id": appointment_id, 
                                         "time_format": TIME_FORMAT,
                                         "user_id": user_id}
                                         ).fetchone()                                                                    
    except:
        abort(500)
    
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
    try:
        db.session.execute(UPDATE_USERINFO_BY_KEY_QUERY, 
                            {"appointment_id": appo_id,
                            "user_id": user_id,
                            "new_symptom": new_symptom})
        db.session.commit()
    except:
        abort(500)
        
def add_new_appointment(patient_id, doctor_id, appointment_type, time_at):
    formatted_time_at = time_at.replace("T", " ")
    if is_valid_future_date(formatted_time_at) and is_valid_input(appointment_type, APPOINTMENT_TYPE_LENGTH_MAX):
        try:
            db.session.execute(CREATE_NEW_APPOINTMENT_QUERY, 
                              {"patient_id": patient_id, 
                               "doctor_id": doctor_id,
                               "appointment_type": appointment_type,
                               "time_at": formatted_time_at})
            db.session.commit()
            return True
        except: 
            abort(500)
    return False

def delete_appointment(appo_id):
    try:
        db.session.execute(DELETE_APPOINTMENT_QUERY, 
                          {"appointment_id": appo_id})
        db.session.commit()
    except:
        abort(500)

def get_bg_color_according_date_past(date):
    """Checks if parameter (date) has past and return hex-color according to it"""
    date_formatted = datetime.strptime(date, "%d-%m-%Y %H:%M")
    if date_formatted > datetime.now():
        return "#B2D2A4"
    
    return "#B8B8B8"