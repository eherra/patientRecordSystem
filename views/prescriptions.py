from flask import redirect, request, session, abort, flash, Blueprint
from services import prescriptions

prescriptions_bp = Blueprint("prescriptions", __name__)

@prescriptions_bp.route("/add-prescription", methods=["POST"])
def add_prescription():
    if not session.get("is_doctor"):
        abort(401, description = "Not authorized call")

    prescriptions.create_new_prescription(request.form["prescription_name"], 
                                          request.form["amount_per_day"])
    flash("New prescription added successfully!", "success")                              
    return redirect("/profile")

@prescriptions_bp.route("/appointment/<int:appli_id>/prescription/<int:prescription_id>/patient/<int:user_id>", methods=["POST"])
def update_user_prescription(appli_id, prescription_id, user_id):
    if not session.get("is_doctor"):
        abort(401, description = "Not authorized call")

    isVisible = request.form["isVisible"] == "True"
    prescriptions.update_prescription_from_user(user_id, prescription_id, isVisible)
    
    if isVisible:
        flash("Prescription added to patient successfully!", "success")                              
    else: 
        flash("Prescription removed from patient successfully!", "success")                              
    return redirect(f"/appointment/{appli_id}/patient/{user_id}")