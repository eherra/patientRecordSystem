from flask import redirect, request, session, flash, Blueprint
from services import messages

messages_bp = Blueprint('message', __name__)

@messages_bp.route("/send-message", methods=["POST"])
def send_message():
    sender_id = session["user_id"]
    content = request.form["content"]
    receiver_id = request.form["receiverId"]
    messages.add_new_message(content, int(sender_id), int(receiver_id))
    flash("Message sent successfully!", "success")
    return redirect("/profile")