from db import db

def get_userInfo(user_id):
    name = get_userInfo_by_key(user_id, 'name')
    phone = get_userInfo_by_key(user_id, 'phone')
    email = get_userInfo_by_key(user_id, 'email')
    address = get_userInfo_by_key(user_id, 'address')
    country = get_userInfo_by_key(user_id, 'country')
    city = get_userInfo_by_key(user_id, 'city')
    return {
        'name': name, 
        'phone': phone, 
        'email': email, 
        'address': address, 
        'country': country, 
        'city': city 
    }

def get_userInfo_by_key(user_id, key):
    sql =  "SELECT value \
            FROM UserInfo \
            WHERE user_id = :user_id \
            AND key = :key"
            
    value = db.session.execute(sql, {"user_id": user_id, "key": key}, ).fetchone()[0]
    return value