from app import app
from flask import redirect, request
from services import prescriptions

#TODO - hard coded sender and receiver -> get userId from sesion
# only admin can call this function
@app.route("/add-prescription", methods=["POST"])
def add_prescription():
    prescriptions.create_new_prescription(request.form["prescription_name"], 
                                          request.form["amount_per_day"])
    return redirect("/doctor-profile")