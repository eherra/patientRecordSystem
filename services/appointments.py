from db import db
from services import users
from constant import TIME_FORMAT, NAME_DB_KEY

APPOINTMENTS_INFO_QUERY = "SELECT appointment_type, doctor_id, TO_CHAR(time_at, :time_format) AS time_at \
                           FROM   Appointments \
                           WHERE  patient_id = :user_id"

def get_appointments_info(user_id):
    fetched_appointments = db.session.execute(APPOINTMENTS_INFO_QUERY, {"user_id": user_id, 
                                                                        "time_format": TIME_FORMAT}).fetchall()
    return format_appointment_data(fetched_appointments)

def format_appointment_data(fetched_appointments):
    formatted_appointments = []

    for appointment in fetched_appointments:
        doctor_name = users.get_userInfo_by_key(appointment[1], NAME_DB_KEY)
        formatted_appointments.append({
            'doctor_name': doctor_name,
            'appointment_type': appointment[0],
            'time': appointment[2]
        })

    return formatted_appointments

