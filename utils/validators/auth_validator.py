from flask import session, redirect, flash, abort
from functools import wraps
from utils.constant import DANGER_CATEGORY

MUST_SIGN_IN_MESSAGE = "No access to the page! Please sign in."
NOT_AUTHORIZED_CALL_MESSAGE = "Not authorized call."

def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            flash(MUST_SIGN_IN_MESSAGE, DANGER_CATEGORY)
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def requires_doctor_role(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("is_doctor"):
            abort(401, description = NOT_AUTHORIZED_CALL_MESSAGE)
        return f(*args, **kwargs)
    return requires_login(decorated_function)
