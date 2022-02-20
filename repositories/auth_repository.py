from database.db import db
from sqlalchemy.exc import SQLAlchemyError

CHECK_LOGIN_AND_RETURN_INFO_QUERY = "SELECT id, password, is_doctor \
                                     FROM   users \
                                     WHERE  username = :username"

def check_login_and_return_info(username):
    try:
        return db.session.execute(CHECK_LOGIN_AND_RETURN_INFO_QUERY,
                                 {"username":username}
                                 ).fetchone()
    except SQLAlchemyError:
        raise