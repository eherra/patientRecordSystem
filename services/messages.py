from db import db

def get_sent_messages(user_id):
    sql = "SELECT * FROM messages WHERE user1_id = :user_id"
    sentMessages = db.session.execute(sql, {"user_id": user_id}).fetchall()
    return sentMessages

#TODO - set doctor name for each message
def get_received_messages(user_id):
    sql = "SELECT * FROM messages WHERE user2_id = :user_id"
    receivedMessages = db.session.execute(sql, {"user_id": user_id}).fetchall()
    return receivedMessages