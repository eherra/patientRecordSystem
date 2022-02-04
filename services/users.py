from db import db
from flask import abort
from utils.constant import NAME_DB_KEY, PHONE_DB_KEY, ADDRESS_DB_KEY, EMAIL_DB_KEY, \
     COUNTRY_DB_KEY, CITY_DB_KEY, PERSONAL_DOCTOR_ID_DB_KEY
from werkzeug.security import generate_password_hash

GET_USERINFO_BY_KEY_QUERY = "SELECT value \
                             FROM   user_info \
                             WHERE  user_id = :user_id \
                             AND    key = :key"

GET_DOCTOR_PATIENTS_QUERY = "SELECT user_id \
                             FROM   user_info \
                             WHERE  key = :key \
                             AND    value = :doctor_id"

CHECK_IS_USERNAME_UNIQUE_QUERY = "SELECT 1 \
                                  FROM   users \
                                  WHERE  username = :username"

UPDATE_USERINFO_BY_KEY_QUERY = "UPDATE user_info \
                                SET    value = :new_value \
                                WHERE  user_id = :user_id \
                                AND    key = :key"

CREATE_NEW_USER_QUERY = "INSERT INTO users (username, password, is_doctor) \
                         VALUES (:username, :password, :is_doctor) \
                         RETURNING id"

CREATE_USER_INFO_QUERY = "INSERT INTO user_info (user_id, key, value) \
                          VALUES (:user_id, :key, :value)"

def get_user_info(user_id):
    return {
        'name': get_user_info_by_key(user_id, NAME_DB_KEY), 
        'phone': get_user_info_by_key(user_id, PHONE_DB_KEY), 
        'email': get_user_info_by_key(user_id, EMAIL_DB_KEY), 
        'address': get_user_info_by_key(user_id, ADDRESS_DB_KEY), 
        'country': get_user_info_by_key(user_id, COUNTRY_DB_KEY), 
        'city': get_user_info_by_key(user_id, CITY_DB_KEY) 
    }

def get_user_personal_doctor_info(doctor_id):
    return {
        'name': get_user_info_by_key(doctor_id, NAME_DB_KEY), 
        'phone': get_user_info_by_key(doctor_id, PHONE_DB_KEY), 
        'id': doctor_id
    }

def get_user_info_by_key(user_id, key):
    try:
        value = db.session.execute(GET_USERINFO_BY_KEY_QUERY,
                                  {"user_id": user_id,
                                   "key": key}
                                   ).fetchone()[0]
        return value
    except:
        abort(500)

def is_username_unique(username):
    try:
        found_username = db.session.execute(CHECK_IS_USERNAME_UNIQUE_QUERY,
                                           {"username": username}
                                           ).fetchone()
        return not found_username
    except:
        abort(500)
    

def get_doctor_patients(doctor_id):
    try:
        fetched_patients = db.session.execute(GET_DOCTOR_PATIENTS_QUERY,
                                             {"key": PERSONAL_DOCTOR_ID_DB_KEY,
                                              "doctor_id": str(doctor_id)})
        return format_doctor_patients(fetched_patients)                                                       
    except:
        abort(500)

def format_doctor_patients(fetched_patients):
    formatted_patients = []
    
    for patient in fetched_patients:
        formatted_patients.append({
            "user_id": patient.user_id,
            "name": get_user_info_by_key(patient.user_id, NAME_DB_KEY)
        })

    return formatted_patients


def update_settings_values(user_id, user):
    "Updates user_info table values if user has filled the input with the request"
    if user.name:
        update_user_info_by_key(user_id, NAME_DB_KEY, user.name)
    
    if user.phone:
        update_user_info_by_key(user_id, PHONE_DB_KEY, user.phone)

    if user.email:
        update_user_info_by_key(user_id, EMAIL_DB_KEY, user.email)

    if user.address:
        update_user_info_by_key(user_id, ADDRESS_DB_KEY, user.address)

    if user.city:
        update_user_info_by_key(user_id, CITY_DB_KEY, user.city)

    if user.country:
        update_user_info_by_key(user_id, COUNTRY_DB_KEY, user.country)

def update_user_info_by_key(user_id, key, new_value):
    try:
        db.session.execute(UPDATE_USERINFO_BY_KEY_QUERY,
                          {"user_id": user_id,
                           "key": key,
                           "new_value": new_value})
        db.session.commit()
    except:
        abort(500)

def create_new_user(user):
    try:
        result = db.session.execute(CREATE_NEW_USER_QUERY,
                                   {"username": user.username,
                                    "password": generate_password_hash(user.password),
                                    "is_doctor": user.is_doctor}).fetchone()
        db.session.commit()
        return result.id
    except:
        abort(500)

def initialize_user_info_values(user_id, user):
    try:
        create_user_info_by_key(user_id, NAME_DB_KEY, user.name)
        create_user_info_by_key(user_id, PHONE_DB_KEY, user.phone)
        create_user_info_by_key(user_id, EMAIL_DB_KEY, user.email)
        create_user_info_by_key(user_id, ADDRESS_DB_KEY, user.address)
        create_user_info_by_key(user_id, CITY_DB_KEY, user.city)
        create_user_info_by_key(user_id, COUNTRY_DB_KEY, user.country)
        db.session.commit()
        return True
    except:
        return False

def create_user_info_by_key(user_id, key, value):
    try:
        db.session.execute(CREATE_USER_INFO_QUERY,
                          {"user_id": user_id,
                           "key": key,
                           "value": value})
    except:
        db.session.rollback()
