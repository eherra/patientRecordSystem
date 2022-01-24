from db import db
from services import users
from constant import TIME_FORMAT, NAME_DB_KEY

# TODO - add ORDER BY time_at 
APPOINTMENTS_INFO_BY_PATIENT_QUERY = "SELECT id, patient_id, doctor_id, appointment_type, TO_CHAR(time_at, :time_format) AS time_at \
                                      FROM   Appointments \
                                      WHERE  patient_id = :user_id"

APPOINTMENTS_INFO_BY_DOCTOR_QUERY = "SELECT id, patient_id, doctor_id, appointment_type, TO_CHAR(time_at, :time_format) AS time_at \
                                     FROM   Appointments \
                                     WHERE  doctor_id = :user_id"

APPOINTMENTS_INFO_BY_ID_QUERY = "SELECT appointment_type, symptom, TO_CHAR(time_at, :time_format) AS time_at \
                                 FROM   Appointments \
                                 WHERE  patient_id = :user_id \
                                 AND    id = :appointment_id"

UPDATE_USERINFO_BY_KEY_QUERY = "UPDATE Appointments \
                                SET    symptom = :new_symptom \
                                WHERE  patient_id = :user_id \
                                AND    id = :appointment_id"

def get_appointments_info_by_patientId(user_id):
    fetched_appointments = db.session.execute(APPOINTMENTS_INFO_BY_PATIENT_QUERY, {"user_id": user_id, 
                                                                                   "time_format": TIME_FORMAT}).fetchall()
    return format_appointment_data(fetched_appointments)

def get_appointments_info_by_doctorId(user_id):
    fetched_appointments = db.session.execute(APPOINTMENTS_INFO_BY_DOCTOR_QUERY, {"user_id": user_id, 
                                                                                  "time_format": TIME_FORMAT}).fetchall()
    return format_appointment_data(fetched_appointments)

def format_appointment_data(fetched_appointments):
    formatted_appointments = []

    # fetched_appointments has a list of tuple values (doctor_id, appointment_type, time_at)
    for appointment in fetched_appointments:
        patient_name = users.get_userInfo_by_key(appointment[1], NAME_DB_KEY)
        doctor_name = users.get_userInfo_by_key(appointment[2], NAME_DB_KEY)
        formatted_appointments.append({
            "id": appointment[0],
            "patient_id": appointment[1],
            'doctor_name': doctor_name,
            "patient_name": patient_name,
            'appointment_type': appointment[3],
            'time': appointment[4]
        })

    return formatted_appointments

def get_appointment_info_by(appointment_id, user_id):
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
def update_appointment_symptom(appointment_id, user_id, new_symptom):
    if is_valid_symptom_input(new_symptom):
        db.session.execute(UPDATE_USERINFO_BY_KEY_QUERY, {"appointment_id": appointment_id,
                                                          "user_id": user_id,
                                                          "new_symptom": new_symptom})
        db.session.commit()

## TODO - move to validation module
def is_valid_symptom_input(input):
    return input and len(input) < 200 and not input.isspace()