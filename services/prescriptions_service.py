from repositories import prescriptions_repository
from utils.constant import PRESCRIPTION_NAME_LENGTH_MAX
from utils.validators.input_validator import is_valid_input

def get_all_not_signed_prescription(user_id):
    """Fetching all prescriptions which user doesn't have yet signed to"""
    return prescriptions_repository.get_all_not_signed_prescription(user_id)

def get_user_prescriptions(user_id):
    fetched_prescriptions = prescriptions_repository.get_user_prescriptions(user_id)
    return format_precription_lists(fetched_prescriptions)

def format_precription_lists(fetched_prescriptions):
    current_prescriptions, history_prescriptions = [], []
    for prescription in fetched_prescriptions:
        prescription_info = get_prescription_info_by_id(prescription.prescription_id)

        if prescription.visible:
            current_prescriptions.append(prescription_info)
        else:
            history_prescriptions.append(prescription_info)

    return {
        "current_prescriptions": current_prescriptions,
        "history_prescriptions": history_prescriptions
        }

def get_prescription_info_by_id(prescription_id):
    return prescriptions_repository.get_prescription_info_by_id(prescription_id)

def update_prescription_from_user(user_id, prescription_id, bool_value):
    prescriptions_repository.update_prescription_from_user(user_id, 
                                                           prescription_id, 
                                                           bool_value)

def create_new_prescription(prescription_name, amount_per_day):
    if is_valid_input(prescription_name, PRESCRIPTION_NAME_LENGTH_MAX):
        return prescriptions_repository.create_new_prescription(prescription_name, amount_per_day)
    return False
