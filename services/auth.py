from werkzeug.security import check_password_hash, generate_password_hash
from db import db

CHECK_LOGIN_AND_RETURN_INFO_QUERY = "SELECT id, password, is_doctor \
                                     FROM   users \
                                     WHERE  username = :username"

def check_login_and_return_info(username, password):
    user = db.session.execute(CHECK_LOGIN_AND_RETURN_INFO_QUERY, 
                             {"username":username}
                             ).fetchone()
    if not user:
        return None
    else:
        hash_value = user.password
        return user if check_password_hash(hash_value, password) else None
