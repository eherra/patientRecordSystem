from werkzeug.security import check_password_hash
from repositories import auth_repository

def check_login_and_return_info(username, password):
    user = auth_repository.check_login_and_return_info(username)
  
    if not user:
        return None
    else:
        hash_value = user.password
        return user if check_password_hash(hash_value, password) else None
