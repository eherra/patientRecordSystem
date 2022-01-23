from db import db

USER_PRESCRIPTIONS_QUERY = "SELECT prescription_id, visible \
                            FROM   UserPrescriptions \
                            WHERE  user_id = :user_id"

SINGLE_PRESCRIPTION_QUERY = "SELECT name, amount_per_day \
                             FROM   Prescriptions \
                             WHERE  id = :prescription_id"
                
GET_ALL_PRESCRIPTIONS_QUERY = "SELECT name, amount_per_day \
                               FROM Prescriptions"

# get all which user doesnt have?
def get_all_prescriptions():
    return db.session.execute(GET_ALL_PRESCRIPTIONS_QUERY).fetchall()

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