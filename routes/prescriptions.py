from app import app
from flask import redirect, request
from services import prescriptions

#TODO - hard coded sender and receiver -> get userId from sesion
# only admin can call this function
@app.route("/add-prescription", methods=["POST"])
def add_prescription():
    prescriptions.create_new_prescription(request.form["prescription_name"], 
                                          request.form["amount_per_day"])
    return redirect("/profile")

# TODO - only admin can call these
@app.route("/appointment/<int:appli_id>/prescription/<int:prescription_id>/patient/<int:user_id>", methods=["POST"])
def update_prescription(appli_id, prescription_id, user_id):
    isVisible = request.form["isVisible"] == "True"
    prescriptions.update_prescription_from_user(user_id, prescription_id, isVisible)
    return redirect(f"/appointment/{appli_id}/patient/{user_id}")