from app import app
from flask import session, redirect, request, render_template
import sys 

@app.route("/login")
def login():
    return render_template("login-page.html")

@app.route("/login", methods=["POST"])
def process_login():
    #TODO add username password check
    print('toimii', file=sys.stdout)

    return redirect("/")

@app.route("/logout")
def logout():
    return redirect("/")

