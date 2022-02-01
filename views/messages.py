from flask import redirect, request, session, flash, Blueprint
from services import messages
from utils.constant import SUCCESS_CATEGORY
from utils.auth_validator import requires_login

SUCCESS_SENT_MESSAGE = "Message sent successfully!"

messages_bp = Blueprint('message', __name__)

@messages_bp.route("/send-message", methods=["POST"])
@requires_login
def send_message():
    sender_id = session["user_id"]
    content = request.form["content"]
    receiver_id = request.form["receiverId"]
    messages.add_new_message(content, int(sender_id), int(receiver_id))
    flash(SUCCESS_SENT_MESSAGE, SUCCESS_CATEGORY)
    return redirect("/profile")