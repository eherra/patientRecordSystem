from app import app
from flask import redirect, request
from services import messages

#TODO - hard coded sender and receiver -> get userId from sesion
@app.route("/send-message", methods=["POST"])
def send():
    content = request.form["content"]
    messages.add_new_message(content, 1, 2)
    return redirect("/")