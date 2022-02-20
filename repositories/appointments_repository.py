from database.db import db
from utils.constant import TIME_FORMAT
from sqlalchemy.exc import SQLAlchemyError

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

CHECK_IS_APPOINTMENT_ID_SIGNED_TO_USER_QUERY = "SELECT 1 \
                                                FROM   appointments \
                                                WHERE  patient_id = :user_id \
                                                AND    id = :appointment_id"

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
        return db.session.execute(PATIENT_ALL_APPOINTMENTS_INFO_QUERY,
                                 {"user_id": user_id,
                                  "time_format": TIME_FORMAT}
                                  ).fetchall()
    except SQLAlchemyError:
        # logging the specific error would be done here
        raise

def get_doctor_appointments_info(user_id):
    try:
        return db.session.execute(DOCTOR_ALL_APPOINTMENTS_INFO_QUERY,
                                 {"user_id": user_id,
                                  "time_format": TIME_FORMAT}
                                 ).fetchall()
    except SQLAlchemyError:
        raise

def get_appointment_info_by(user_id, appointment_id):
    try:
        return db.session.execute(APPOINTMENTS_INFO_BY_ID_QUERY,
                                 {"appointment_id": appointment_id,
                                  "time_format": TIME_FORMAT,
                                  "user_id": user_id}
                                 ).fetchone()
    except SQLAlchemyError:
        raise

def update_appointment_symptom(user_id, appo_id, new_symptom):
    try:
        db.session.execute(UPDATE_USERINFO_BY_KEY_QUERY,
                          {"appointment_id": appo_id,
                           "user_id": user_id,
                           "new_symptom": new_symptom})
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False

def add_new_appointment(patient_id, doctor_id, 
                        appointment_type, formatted_time_at):
    try:
        db.session.execute(CREATE_NEW_APPOINTMENT_QUERY,
                          {"patient_id": patient_id,
                           "doctor_id": doctor_id,
                           "appointment_type": appointment_type,
                           "time_at": formatted_time_at})
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False

def delete_appointment(appo_id):
    try:
        db.session.execute(DELETE_APPOINTMENT_QUERY,
                          {"appointment_id": appo_id})
        db.session.commit()
        return True
    except SQLAlchemyError:
        db.session.rollback()
        return False

def is_appointment_signed_to_user(user_id, appointment_id):
    try:
        return db.session.execute(CHECK_IS_APPOINTMENT_ID_SIGNED_TO_USER_QUERY,
                                 {"user_id": user_id,
                                  "appointment_id": appointment_id}
                                 ).fetchone()
    except SQLAlchemyError:
        raise
