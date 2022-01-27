from db import db
from utils.constant import TIME_FORMAT, NAME_DB_KEY
from services import users

SENT_MESSAGES_QUERY = "SELECT   user2_id, content, TO_CHAR(sent_at, :time_format) \
                       FROM     messages \
                       WHERE    user1_id = :user_id \
                       ORDER BY sent_at DESC"

RECEIVED_MESSAGES_QUERY = "SELECT   user1_id, content, TO_CHAR(sent_at, :time_format) \
                           FROM     messages \
                           WHERE    user2_id = :user_id \
                           ORDER BY sent_at DESC"

ADD_NEW_MESSAGE_QUERY = "INSERT INTO messages (user1_id, user2_id, content, sent_at) \
                         VALUES (:sender_user_id, :receiver_user_id, :content, NOW())"

def get_sent_messages(user_id):
    sent_messages = db.session.execute(SENT_MESSAGES_QUERY, {"user_id": user_id,
                                                            "time_format": TIME_FORMAT}).fetchall()
    return format_messages(sent_messages)

def get_received_messages(user_id):
    received_messages = db.session.execute(RECEIVED_MESSAGES_QUERY, {"user_id": user_id,
                                                                    "time_format": TIME_FORMAT}).fetchall()
    return format_messages(received_messages)

def format_messages(messages_list):
    formatted_messages = []
    # message is a tuple value of (user_id, content, sent_at)
    for message in messages_list:
        formatted_messages.append({
            "toOrfrom": users.get_user_info_by_key(message[0], NAME_DB_KEY),
            "content": message[1],
            "sent_at": message[2]
        })
    return formatted_messages

## TODO - add validation for content
def add_new_message(content, sender_user_id, receiver_user_id):
    db.session.execute(ADD_NEW_MESSAGE_QUERY, {"content": content, 
                                               "sender_user_id": sender_user_id, 
                                               "receiver_user_id": receiver_user_id})
    db.session.commit()
