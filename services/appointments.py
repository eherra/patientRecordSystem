from db import db
from services import users

APPOINTMENT_TIME_FORMAT = '%d-%m-%Y %H:%M'

def get_appointments_info(user_id):
    sql = ("SELECT appointment_type, doctor_id, time_at FROM Appointments WHERE patient_id = :user_id")
    fetched_appointments = db.session.execute(sql, {"user_id": user_id}).fetchall()

    return format_appointment_data(fetched_appointments)

def format_appointment_data(fetched_appointments):
    formatted_appointments = []

    for appointment in fetched_appointments:
        doctor_name = users.get_userInfo_by_key(appointment[1], 'name')
        formatted_appointments.append({
            'doctor_name': doctor_name,
            'appointment_type': appointment[0],
            'time': appointment[2].strftime(APPOINTMENT_TIME_FORMAT)
        })

    return formatted_appointments

