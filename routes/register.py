from app import app
from flask import session, redirect, request, render_template
import sys 

@app.route("/register")
def register_page():
    return render_template("register-page.html")

@app.route("/register/user")
def register_user():
    # check if over 3 characters and unique
    username = request.form["username"]

    # check if over 5 characters
    password = request.form["password"]

    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    address = request.form["address"]
    city = request.form["city"]
    country = request.form["country"]

    return render_template("/profile")  