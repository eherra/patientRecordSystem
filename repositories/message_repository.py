from database.db import db
from utils.constant import TIME_FORMAT
from sqlalchemy.exc import SQLAlchemyError

SENT_MESSAGES_QUERY = "SELECT   user2_id AS user_id, content, TO_CHAR(sent_at, :time_format) AS time \
                       FROM     messages \
                       WHERE    user1_id = :user_id \
                       ORDER BY sent_at DESC"

RECEIVED_MESSAGES_QUERY = "SELECT   user1_id AS user_id, content, TO_CHAR(sent_at, :time_format) AS time \
                           FROM     messages \
                           WHERE    user2_id = :user_id \
                           ORDER BY sent_at DESC"

ADD_NEW_MESSAGE_QUERY = "INSERT INTO messages (user1_id, user2_id, content, sent_at) \
                         VALUES (:sender_user_id, :receiver_user_id, :content, NOW())"

def get_sent_messages(user_id):
    try:
        return db.session.execute(SENT_MESSAGES_QUERY,
                                 {"user_id": user_id,
                                  "time_format": TIME_FORMAT}
                                 ).fetchall()
    except SQLAlchemyError:
        raise

def get_received_messages(user_id):
    try:
        return db.session.execute(RECEIVED_MESSAGES_QUERY,
                                 {"user_id": user_id,
                                  "time_format": TIME_FORMAT}
                                 ).fetchall()
    except SQLAlchemyError:
        raise

def add_new_message(content, sender_user_id, receiver_user_id):
    try:
        is_success = db.session.execute(ADD_NEW_MESSAGE_QUERY,
                                       {"content": content,
                                        "sender_user_id": sender_user_id,
                                        "receiver_user_id": receiver_user_id})
        db.session.commit()
        return is_success
    except SQLAlchemyError:
        db.session.rollback()
        return False
