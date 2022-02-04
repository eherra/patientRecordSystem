from datetime import datetime

VALIDATOR_TIME_FORMAT="%Y-%m-%d %H:%M"

def is_valid_input(input, input_max_length):
    return input and len(input) <= input_max_length and not input.isspace()

def is_valid_date(date):
    try:
        return bool(datetime.strptime(date, VALIDATOR_TIME_FORMAT))
    except:
        return False    
