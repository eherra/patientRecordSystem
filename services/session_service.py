from datetime import timedelta, datetime, timezone
from flask import session
from utils.constant import SESSION_ALIVE_TIME_MINUTES

def get_user_id():
    return session.get("user_id")

def is_doctor():
    return session.get("is_doctor")

def get_session_ending_time():
    return session.get("session_end_time")

def initialize_session(user_id, is_doctor):
    session["user_id"] = user_id
    session["is_doctor"] = is_doctor
    # Initializing session ending time to current time + minutes set as SESSION_ALIVE_TIME_MINUTES
    session["session_end_time"] = datetime.now(timezone.utc) + timedelta(minutes=SESSION_ALIVE_TIME_MINUTES)
    # if there was failed attempts to login, filled username deletion from the session
    session.pop("filled_username", None)

def logout_user():
    session.pop("user_id", None)
    session.pop("is_doctor", None)
    session.pop("session_end_time", None)

def set_username_after_login_failure(username):
    session["filled_username"] = username

def initialize_failed_registering_attempt_data(form):
    """If registration has failed with incorrect data format, filled input fields saved to session"""
    session["register_username"] = form["username"]
    session["register_password"] = form["password"]
    session["register_name"] = form["name"]
    session["register_email"] = form["email"]
    session["register_phone"] = form["phone"]
    session["register_address"] = form["address"]
    session["register_city"] = form["city"]
    session["register_country"] = form["country"]

def delete_failed_registration_attempt_data():
    """Deleting information saved from failed registration attempts after registration succeeded"""
    session.pop("register_username", None)
    session.pop("register_password", None)
    session.pop("register_name", None)
    session.pop("register_email", None)
    session.pop("register_phone", None)
    session.pop("register_address", None)
    session.pop("register_city", None)
    session.pop("register_country", None)
