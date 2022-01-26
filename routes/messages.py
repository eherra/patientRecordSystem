from app import app
from flask import redirect, request
from services import messages

#TODO - hard coded sender and receiver -> get userId from sesion
@app.route("/send-message", methods=["POST"])
def send_message():
    sender_id = 1
    content = request.form["content"]
    receiver_id = request.form["receiverId"]
    messages.add_new_message(content, sender_id, receiver_id)
    return redirect("/profile")