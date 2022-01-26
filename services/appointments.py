from db import db
from services import users
from constant import TIME_FORMAT, NAME_DB_KEY
from datetime import datetime
import sys

PATIENT_ALL_APPOINTMENTS_INFO_QUERY = "SELECT   id, patient_id, doctor_id, appointment_type, TO_CHAR(time_at, :time_format) \
                                       FROM     Appointments \
                                       WHERE    patient_id = :user_id \
                                       ORDER BY time_at DESC"

DOCTOR_ALL_APPOINTMENTS_INFO_QUERY = "SELECT   id, patient_id, doctor_id, appointment_type, TO_CHAR(time_at, :time_format) \
                                      FROM     Appointments \
                                      WHERE    doctor_id = :user_id \
                                      ORDER BY time_at DESC"

APPOINTMENTS_INFO_BY_ID_QUERY = "SELECT appointment_type, symptom, TO_CHAR(time_at, :time_format) AS time_at \
                                 FROM   Appointments \
                                 WHERE  patient_id = :user_id \
                                 AND    id = :appointment_id"

UPDATE_USERINFO_BY_KEY_QUERY = "UPDATE Appointments \
                                SET    symptom = :new_symptom \
                                WHERE  patient_id = :user_id \
                                AND    id = :appointment_id"

CREATE_NEW_APPOINTMENT_QUERY = "INSERT INTO Appointments (patient_id, doctor_id, appointment_type, time_at) \
                                VALUES (:patient_id, :doctor_id, :appointment_type, (TIMESTAMP :time_at))"

DELETE_APPOINTMENT_QUERY = "DELETE \
                            FROM Appointments \
                            WHERE id = :appointment_id"

def get_patient_appointments_info(user_id):
    fetched_appointments = db.session.execute(PATIENT_ALL_APPOINTMENTS_INFO_QUERY, {"user_id": user_id, 
                                                                                   "time_format": TIME_FORMAT}).fetchall()
    return format_appointment_data(fetched_appointments)

def get_doctor_appointments_info(user_id):
    fetched_appointments = db.session.execute(DOCTOR_ALL_APPOINTMENTS_INFO_QUERY, {"user_id": user_id, 
                                                                                  "time_format": TIME_FORMAT}).fetchall()
    return format_appointment_data(fetched_appointments)

def format_appointment_data(fetched_appointments):
    formatted_appointments = []

    # fetched_appointments has a list of tuple values (doctor_id, appointment_type, time_at)
    for appointment in fetched_appointments:
        patient_name = users.get_user_info_by_key(appointment[1], NAME_DB_KEY)
        doctor_name = users.get_user_info_by_key(appointment[2], NAME_DB_KEY)
        formatted_appointments.append({
            "id": appointment[0],
            "patient_id": appointment[1],
            'doctor_name': doctor_name,
            "patient_name": patient_name,
            'appointment_type': appointment[3],
            'time': appointment[4],
            'bg_color': get_bg_color_according_date_past(appointment[4])
        })

    return formatted_appointments

def get_appointment_info_by(user_id, appointment_id):
    appointment = db.session.execute(APPOINTMENTS_INFO_BY_ID_QUERY, {"appointment_id": appointment_id, 
                                                                     "time_format": TIME_FORMAT,
                                                                     "user_id": user_id }).fetchone()
    return {
        "id": appointment_id,
        "patient_id": user_id,
        "appointment_type": appointment[0],
        "symptom": appointment[1],
        "time_at": appointment[2],
    }

## TODO - proper error handling
def update_appointment_symptom(user_id, appo_id, new_symptom):
    if is_valid_symptom_input(new_symptom):
        db.session.execute(UPDATE_USERINFO_BY_KEY_QUERY, {"appointment_id": appo_id,
                                                          "user_id": user_id,
                                                          "new_symptom": new_symptom})
        db.session.commit()

## TODO - proper error handling
def add_new_appointment(patient_id, doctor_id, appointment_type, time_at):
    formatted_time_at = time_at.replace("T", " ")
    if is_valid_appointment_type_input(appointment_type) and is_valid_date(formatted_time_at):
        db.session.execute(CREATE_NEW_APPOINTMENT_QUERY, {"patient_id": patient_id, 
                                                          "doctor_id": doctor_id,
                                                          "appointment_type": appointment_type,
                                                          "time_at": formatted_time_at})
        db.session.commit()

## TODO - proper error handling
def delete_appointment(appo_id):
    db.session.execute(DELETE_APPOINTMENT_QUERY, {"appointment_id": appo_id})
    db.session.commit()

## TODO - move to validation module
def is_valid_symptom_input(input):
    return input and len(input) < 200 and not input.isspace()

def get_bg_color_according_date_past(date):
    """Checks if parameter (date) has past and return hex-color according to it"""
    date_formatted = datetime.strptime(date, "%d-%m-%Y %H:%M")
    if date_formatted > datetime.now():
        return "#B2D2A4"
    else:
        return "#B8B8B8"

## TODO - add correct date check
def is_valid_date(input):
    return input and not input.isspace()

def is_valid_appointment_type_input(input):
    return input and len(input) < 30 and not input.isspace()