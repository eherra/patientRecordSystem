from app import app
from flask import session, redirect, request, render_template
from services import login, users
import sys 


@app.route("/")
def index():
    if session["user_id"]:
        return redirect("/profile")
        
    return redirect("login.html")

@app.route("/login")
def login_page():
    return render_template("login-page.html")
 
@app.route("/login", methods=["POST"])
def process_login():
    username = request.form["username"]
    password = request.form["password"]
    logged_user_info = login.check_login_and_return_info(username, password)

    if logged_user_info:
        session["user_id"] = logged_user_info[0]
        session["is_doctor"] = logged_user_info[2]
    else: 
        return redirect("/login")

    return redirect("/profile")

@app.route("/logout")
def logout():
    del session["user_id"]
    del session["is_doctor"]
    return redirect("/login")

