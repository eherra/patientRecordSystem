from db import db
import sys

USER_PRESCRIPTIONS_QUERY = "SELECT prescription_id, visible \
                            FROM   UserPrescriptions \
                            WHERE  user_id = :user_id"

SINGLE_PRESCRIPTION_QUERY = "SELECT id, name, amount_per_day \
                             FROM   Prescriptions \
                             WHERE  id = :prescription_id"
                
GET_ALL_NOT_SIGNED_PRESCRIPTIONS_QUERY = "SELECT id, name, amount_per_day \
                                          FROM Prescriptions \
                                          WHERE id NOT IN \
                                                  (SELECT prescription_id \
                                                   FROM   UserPrescriptions \
                                                   WHERE  user_id = :user_id \
                                                   AND    visible = TRUE)"

UPDATE_USER_PRESCRIPTION = "UPDATE UserPrescriptions \
                            SET    visible = :visible \
                            WHERE  user_id = :user_id \
                            AND    prescription_id = :prescription_id"

ADD_USER_PRESCRIPTION = "INSERT INTO UserPrescriptions (prescription_id, user_id) \
                         VALUES (:prescription_id, :user_id);"

CREATE_NEW_PRESCRIPTION = "INSERT INTO Prescriptions (name, amount_per_day) \
                           VALUES (:name, :amount_per_day);"

def get_all_not_signed_prescription(user_id):
    """Fetching all prescriptions which User doesn't have yet signed to"""
    return db.session.execute(GET_ALL_NOT_SIGNED_PRESCRIPTIONS_QUERY, {"user_id": user_id}).fetchall()

def get_user_prescriptions(user_id):
    fetched_prescriptions = db.session.execute(USER_PRESCRIPTIONS_QUERY, {"user_id": user_id}).fetchall()
    return format_precription_lists(fetched_prescriptions)

def format_precription_lists(fetched_prescriptions):
    current_prescriptions, history_prescriptions = [], []
    # fetched_prescriptions has list of tuple values (prescription_id, visible)
    for prescription in fetched_prescriptions:
        prescription_info = get_prescription_info_by_id(prescription[0])

        if prescription[1]:
            current_prescriptions.append(prescription_info)
        else:
            history_prescriptions.append(prescription_info)

    return {
        'current_prescriptions': current_prescriptions, 
        'history_prescriptions': history_prescriptions
        }

def get_prescription_info_by_id(prescription_id):
    return db.session.execute(SINGLE_PRESCRIPTION_QUERY, {"prescription_id": prescription_id}).fetchone()

def update_prescription_from_user(user_id, prescription_id, bool_value):
    """Changing UserPrescription "visible" value to given parameter (bool_value)
       If update rowcount = 0, no connection made on UserPrescription table for the user for the prescription before"""
    isSuccess = db.session.execute(UPDATE_USER_PRESCRIPTION, {"user_id": user_id, 
                                                              "prescription_id": prescription_id,
                                                              "visible": bool_value})
    if not isSuccess.rowcount:
        add_new_prescription_to(user_id, prescription_id)

    db.session.commit()

def add_new_prescription_to(user_id, prescription_id):
    db.session.execute(ADD_USER_PRESCRIPTION, {"user_id": user_id, 
                                               "prescription_id": prescription_id})

def create_new_prescription(prescription_name, amount_per_day):
    db.session.execute(CREATE_NEW_PRESCRIPTION, {"name": prescription_name, 
                                                 "amount_per_day": amount_per_day})
    db.session.commit()
