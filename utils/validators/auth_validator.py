from datetime import datetime, timezone
from functools import wraps
from flask import session, redirect, flash, abort
from utils.constant import DANGER_CATEGORY
from services.appointments import is_appointment_signed_to_user

MUST_SIGN_IN_MESSAGE = "No access to the page! Please log in."
SESSION_EXPIRED_MESSAGE = "Your session has expired! Please log in again."
NOT_AUTHORIZED_CALL_MESSAGE = "Not authorized call."
NOT_AUTHORIZED_TO_THE_APPOINTMENT_PAGE ="Got lost? Nothing there for you."

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

def requires_session_time_alive(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if has_session_expired():
            flash(SESSION_EXPIRED_MESSAGE, DANGER_CATEGORY)
            del session["user_id"]
            del session["is_doctor"]
            del session["session_end_time"]
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def has_session_expired():
    return session.get("session_end_time") < datetime.now(timezone.utc)

def requires_appointment_signed_to_user(f):
    """Validates that appointment id belonging to user and session user_id matching
       to patient_id given as url parameter.
       For doctor role these checks are not executed"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("is_doctor"):
            if has_no_access(kwargs):
                flash(NOT_AUTHORIZED_TO_THE_APPOINTMENT_PAGE, DANGER_CATEGORY)
                return redirect("/profile")
        return f(*args, **kwargs)
    return decorated_function

def has_no_access(kwargs):
    appointment_id = int(kwargs["appo_id"])
    patient_id = int(kwargs["patient_id"])
    return not (session["user_id"] == patient_id
                and is_appointment_signed_to_user(patient_id, appointment_id))
