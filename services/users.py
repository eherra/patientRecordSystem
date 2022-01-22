from db import db
from constant import NAME_DB_KEY, PHONE_DB_KEY, ADDRESS_DB_KEY, EMAIL_DB_KEY, COUNTRY_DB_KEY, CITY_DB_KEY

USERINFO_BY_KEY_QUERY = "SELECT value \
                         FROM   UserInfo \
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
    value = db.session.execute(USERINFO_BY_KEY_QUERY, {"user_id": user_id,
                                                       "key": key}).fetchone()[0]
    return value