from utils.constant import TIME_FORMAT
from services import users
from datetime import datetime
import sys

VALIDATOR_TIME_FORMAT="%Y-%m-%d %H:%M"

def is_valid_input(input, input_max_length):
    return input and len(input) <= input_max_length and not input.isspace()

def is_valid_date(date):
    try:
        return bool(datetime.strptime(date, VALIDATOR_TIME_FORMAT))
    except:
        return False    

def is_valid_email(email):
    return email and len(email) <= 40 and "@" in email

def is_valid_phone(phone):
    if phone and phone.startswith("+"):
        phone = phone[1:]

    return len(phone) <= 20 and phone.isdecimal()

def is_valid_username(username):
    return len(username) >= 3 and len(username) <= 40 and users.is_username_unique(username)

def is_valid_password(password):
    return len(password) >= 5