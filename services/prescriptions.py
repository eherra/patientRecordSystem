from db import db
import sys

def get_user_prescriptions(user_id):
    sql = ("SELECT prescription_id, visible FROM UserPrescriptions WHERE user_id = :user_id")
    fetched_prescripions = db.session.execute(sql, {"user_id": user_id}).fetchall()

    prescription_lists_as_json = make_prescription_list(fetched_prescripions)
    return prescription_lists_as_json

#TODO - refactor
def make_prescription_list(fetched_prescripions):
    current_prescriptions = []
    history_prescriptions = []
    sql = "SELECT name, amount_per_day FROM Prescriptions WHERE id = :prescription_id"

    # fetched_prescripions has tuple values of (prescription_id, visible)
    for currPrescreption in fetched_prescripions:
        prescription_id = currPrescreption[0]
        prescription_info = db.session.execute(sql, {"prescription_id": prescription_id}).fetchone()

        if currPrescreption[1]:
            current_prescriptions.append(prescription_info)
        else:
            history_prescriptions.append(prescription_info)

    return {
        'current_prescriptions': current_prescriptions, 
        'history_prescriptions': history_prescriptions
    }