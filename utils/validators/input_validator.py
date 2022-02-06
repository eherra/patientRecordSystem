from datetime import datetime

VALIDATOR_TIME_FORMAT="%Y-%m-%d %H:%M"

def is_valid_input(input, input_max_length):
    return input and len(input) <= input_max_length and not input.isspace()

def is_valid_future_date(date):
    try:
        date = datetime.strptime(date, VALIDATOR_TIME_FORMAT)
        return bool(date) and date > datetime.now()
    except:
        return False        