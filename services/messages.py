from db import db
from constant import TIME_FORMAT

# TODO - add ORDER BY sent_at 
SENT_MESSAGES_QUERY = "SELECT content, TO_CHAR(sent_at, :time_format) AS sent_at \
                       FROM   messages \
                       WHERE  user1_id = :user_id"

RECEIVED_MESSAGES_QUERY = "SELECT content, TO_CHAR(sent_at, :time_format) AS sent_at \
                           FROM   messages \
                           WHERE  user2_id = :user_id"

ADD_NEW_MESSAGE_QUERY = "INSERT INTO messages (user1_id, user2_id, content, sent_at) \
                         VALUES (:sender_user_id, :receiver_user_id, :content, NOW())"

#TODO - set receiver name for each message
def get_sent_messages(user_id):
    sentMessages = db.session.execute(SENT_MESSAGES_QUERY, {"user_id": user_id,
                                                            "time_format": TIME_FORMAT}).fetchall()
    return sentMessages

#TODO - set sender name for each message
def get_received_messages(user_id):
    receivedMessages = db.session.execute(RECEIVED_MESSAGES_QUERY, {"user_id": user_id,
                                                                    "time_format": TIME_FORMAT}).fetchall()
    return receivedMessages

## TODO - add validation for content
def add_new_message(content, sender_user_id, receiver_user_id):
    db.session.execute(ADD_NEW_MESSAGE_QUERY, {"content": content, 
                                               "sender_user_id": sender_user_id, 
                                               "receiver_user_id": receiver_user_id})
    db.session.commit()
