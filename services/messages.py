from db import db
import sys
from constant import TIME_FORMAT

def get_sent_messages(user_id):
    sql =  "SELECT content, TO_CHAR(sent_at, :time_format) AS sent_at \
            FROM messages \
            WHERE user1_id = :user_id"
    sentMessages = db.session.execute(sql, {"user_id": user_id,
                                            "time_format": TIME_FORMAT}).fetchall()
    return sentMessages

#TODO - set doctor name for each message
def get_received_messages(user_id):
    sql =  "SELECT content, TO_CHAR(sent_at, :time_format) AS sent_at \
            FROM messages \
            WHERE user2_id = :user_id"
    receivedMessages = db.session.execute(sql, {"user_id": user_id,
                                                "time_format": TIME_FORMAT}).fetchall()
    return receivedMessages

def add_new_message(content, sender_user_id, receiver_user_id):
    sql =  "INSERT INTO messages (user1_id, user2_id, content, sent_at) \
            VALUES (:sender_user_id, :receiver_user_id, :content, NOW())"

    db.session.execute(sql, { 
                            "content": content, 
                            "sender_user_id": sender_user_id, 
                            "receiver_user_id": receiver_user_id
                            })
    db.session.commit()
