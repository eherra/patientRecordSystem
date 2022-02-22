from flask import redirect, request, flash, Blueprint
from services import messages_service, session_service
from utils.constant import SUCCESS_CATEGORY, DANGER_CATEGORY
from utils.validators.auth_validator import requires_login, requires_session_time_alive

SUCCESS_SENT_MESSAGE = "Message sent successfully!"
UNSUCCESS_SENT_MESSAGE = "Couldn't deliver that message!"

messages_bp = Blueprint("message", __name__)

@messages_bp.route("/send-message", methods=["POST"])
@requires_login
@requires_session_time_alive
def send_message():
    sender_id = int(session_service.get_user_id())
    receiver_id = int(request.form["receiver_id"])
    is_success = messages_service.add_new_message(request.form["content"],
                                                  sender_id,
                                                  receiver_id)
    if is_success:
        flash(SUCCESS_SENT_MESSAGE, SUCCESS_CATEGORY)
    else:
        flash(UNSUCCESS_SENT_MESSAGE, DANGER_CATEGORY)
    return redirect("/profile")
    