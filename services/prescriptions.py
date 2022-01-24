from db import db

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

def get_all_not_signed_prescription(user_id):
    """Fetching all prescriptions which User doesn't have yet signed to"""
    return db.session.execute(GET_ALL_NOT_SIGNED_PRESCRIPTIONS_QUERY, {"user_id": user_id}).fetchall()

def get_user_prescriptions(user_id):
    fetched_prescripions = db.session.execute(USER_PRESCRIPTIONS_QUERY, {"user_id": user_id}).fetchall()
    return format_precription_lists(fetched_prescripions)

def format_precription_lists(fetched_prescripions):
    current_prescriptions, history_prescriptions = [], []
    # fetched_prescriptions has list of tuple values (prescription_id, visible)
    for prescription in fetched_prescripions:
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
    """Changing UserPrescription "visible" value to given parameter (bool_value) """
    db.session.execute(UPDATE_USER_PRESCRIPTION, {"user_id": user_id, 
                                                  "prescription_id": prescription_id,
                                                  "visible": bool_value})
    db.session.commit()

