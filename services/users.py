from db import db
from constant import NAME_DB_KEY, PHONE_DB_KEY, ADDRESS_DB_KEY, EMAIL_DB_KEY, COUNTRY_DB_KEY, CITY_DB_KEY

GET_USERINFO_BY_KEY_QUERY = "SELECT value \
                             FROM   UserInfo \
                             WHERE  user_id = :user_id \
                             AND    key = :key"

UPDATE_USERINFO_BY_KEY_QUERY = "UPDATE UserInfo \
                                SET    value = :new_value \
                                WHERE  user_id = :user_id \
                                AND    key = :key"

def get_userInfo(user_id):
    return {
        'name': get_userInfo_by_key(user_id, NAME_DB_KEY), 
        'phone': get_userInfo_by_key(user_id, PHONE_DB_KEY), 
        'email': get_userInfo_by_key(user_id, EMAIL_DB_KEY), 
        'address': get_userInfo_by_key(user_id, ADDRESS_DB_KEY), 
        'country': get_userInfo_by_key(user_id, COUNTRY_DB_KEY), 
        'city': get_userInfo_by_key(user_id, CITY_DB_KEY) 
    }

def get_userInfo_by_key(user_id, key):
    value = db.session.execute(GET_USERINFO_BY_KEY_QUERY, {"user_id": user_id,
                                                           "key": key}).fetchone()[0]
    return value

# TODO - hardcoded user_id -> fetch it from session
def update_settings_values(name, phone, email, address, city, country):
    if is_valid_input(name):
        update_userInfo_by_key(1, NAME_DB_KEY, name)
    
    if is_valid_input(phone):
        update_userInfo_by_key(1, PHONE_DB_KEY, phone)

    if is_valid_input(email):
        update_userInfo_by_key(1, EMAIL_DB_KEY, email)

    if is_valid_input(address):
        update_userInfo_by_key(1, ADDRESS_DB_KEY, address)

    if is_valid_input(city):
        update_userInfo_by_key(1, CITY_DB_KEY, city)

    if is_valid_input(country):
        update_userInfo_by_key(1, COUNTRY_DB_KEY, country)

## TODO - move to validation module
def is_valid_input(input):
    return input and len(input) < 50 and not input.isspace()

def update_userInfo_by_key(user_id, key, new_value):
    db.session.execute(UPDATE_USERINFO_BY_KEY_QUERY, {"user_id": user_id,
                                                      "key": key,
                                                      "new_value": new_value})
    db.session.commit()