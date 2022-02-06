from flask import redirect, request, session, flash, Blueprint
from services import messages
from utils.constant import SUCCESS_CATEGORY, DANGER_CATEGORY
from utils.validators.auth_validator import requires_login

SUCCESS_SENT_MESSAGE = "Message sent successfully!"
UNSUCCESS_SENT_MESSAGE = "Couldn't deliver that message!"

messages_bp = Blueprint('message', __name__)

@messages_bp.route("/send-message", methods=["POST"])
@requires_login
def send_message():
    sender_id = session["user_id"]
    receiver_id = request.form["receiverId"]
    is_success = messages.add_new_message(request.form["content"], 
                                          int(sender_id), 
                                          int(receiver_id))
    if is_success:
        flash(SUCCESS_SENT_MESSAGE, SUCCESS_CATEGORY)
    else: 
        flash(UNSUCCESS_SENT_MESSAGE, DANGER_CATEGORY)
    return redirect("/profile")