from utils.constant import NAME_DB_KEY, MESSAGE_LENGTH_MAX
from utils.validators.input_validator import is_valid_input
from repositories import message_repository
from services import users_service

def get_sent_messages(user_id):
    sent_messages = message_repository.get_sent_messages(user_id)
    return format_messages(sent_messages)

def get_received_messages(user_id):
    received_messages = message_repository.get_received_messages(user_id)
    return format_messages(received_messages)

def format_messages(messages_list):
    formatted_messages = []
    # message is a tuple value of (user_id, content, time)
    for message in messages_list:
        formatted_messages.append({
            "toOrfrom": users_service.get_user_info_by_key(message.user_id, NAME_DB_KEY),
            "content": message.content,
            "sent_at": message.time
        })
    return formatted_messages

def add_new_message(content, sender_user_id, receiver_user_id):
    if is_valid_input(content, MESSAGE_LENGTH_MAX):
        is_success = message_repository.add_new_message(content, 
                                                        sender_user_id, 
                                                        receiver_user_id)
        return is_success
    return False
