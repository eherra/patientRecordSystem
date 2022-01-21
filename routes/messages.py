from app import app
from flask import redirect, render_template, request
from db import db

#TODO - hard coded sender and receiver
@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = "INSERT INTO messages (user1_id, user2_id, content, sent_at) VALUES (1, 2, :content, NOW())"
    db.session.execute(sql, {"content": content})
    db.session.commit()
    return redirect("/")