from db import db
from flask import abort
from utils.constant import PRESCRIPTION_NAME_LENGTH_MAX
from utils.validators.input_validator import is_valid_input

USER_PRESCRIPTIONS_QUERY = "SELECT prescription_id, visible \
                            FROM   user_prescriptions \
                            WHERE  user_id = :user_id"

SINGLE_PRESCRIPTION_QUERY = "SELECT id, name, amount_per_day \
                             FROM   prescriptions \
                             WHERE  id = :prescription_id"
                
GET_ALL_NOT_SIGNED_PRESCRIPTIONS_QUERY = "SELECT id, name, amount_per_day \
                                          FROM   prescriptions \
                                          WHERE  id NOT IN \
                                                   (SELECT prescription_id \
                                                    FROM   user_prescriptions \
                                                    WHERE  user_id = :user_id \
                                                    AND    visible = TRUE)"

UPDATE_USER_PRESCRIPTION = "UPDATE user_prescriptions \
                            SET    visible = :visible \
                            WHERE  user_id = :user_id \
                            AND    prescription_id = :prescription_id"

ADD_USER_PRESCRIPTION = "INSERT INTO user_prescriptions (prescription_id, user_id) \
                         VALUES (:prescription_id, :user_id);"

CREATE_NEW_PRESCRIPTION = "INSERT INTO prescriptions (name, amount_per_day) \
                           VALUES (:name, :amount_per_day);"

def get_all_not_signed_prescription(user_id):
    """Fetching all prescriptions which User doesn't have yet signed to"""
    try:
        return db.session.execute(GET_ALL_NOT_SIGNED_PRESCRIPTIONS_QUERY,
                                 {"user_id": user_id}
                                 ).fetchall()
    except:
        abort(500)

def get_user_prescriptions(user_id):
    try:
        fetched_prescriptions = db.session.execute(USER_PRESCRIPTIONS_QUERY, 
                                                  {"user_id": user_id}
                                                  ).fetchall()
        return format_precription_lists(fetched_prescriptions)
    except:
        abort(500)

def format_precription_lists(fetched_prescriptions):
    current_prescriptions, history_prescriptions = [], []
    for prescription in fetched_prescriptions:
        prescription_info = get_prescription_info_by_id(prescription.prescription_id)

        if prescription.visible:
            current_prescriptions.append(prescription_info)
        else:
            history_prescriptions.append(prescription_info)

    return {
        'current_prescriptions': current_prescriptions, 
        'history_prescriptions': history_prescriptions
        }

def get_prescription_info_by_id(prescription_id):
    try:
        return db.session.execute(SINGLE_PRESCRIPTION_QUERY,
                                 {"prescription_id": prescription_id}
                                 ).fetchone()
    except:
        abort(500)

def update_prescription_from_user(user_id, prescription_id, bool_value):
    """Changing user_prescription table "visible" value to given parameter (bool_value)"""
    try:
        is_success = db.session.execute(UPDATE_USER_PRESCRIPTION, 
                                       {"user_id": user_id, 
                                       "prescription_id": prescription_id,
                                       "visible": bool_value})
        # if nothing updated, there was not connection on user_prescriptions table earlier                           
        if not is_success.rowcount:
            add_new_prescription_to(user_id, prescription_id)

        db.session.commit()
    except:
        abort(500)

def add_new_prescription_to(user_id, prescription_id):
    try:
        db.session.execute(ADD_USER_PRESCRIPTION, 
                          {"user_id": user_id, 
                           "prescription_id": prescription_id})
    except:
        abort(500)

def create_new_prescription(prescription_name, amount_per_day):
    if is_valid_input(prescription_name, PRESCRIPTION_NAME_LENGTH_MAX):
        try:
            is_success = db.session.execute(CREATE_NEW_PRESCRIPTION,
                                           {"name": prescription_name, 
                                            "amount_per_day": amount_per_day})
            db.session.commit()
            return is_success 
        except:
            abort(500)
    return False