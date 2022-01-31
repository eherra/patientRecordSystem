from flask import render_template, jsonify
from app import app

@app.errorhandler(401)
def user_not_authorized(error):
    return jsonify(error=str(error)), 401

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error-pages/404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error-pages/500.html'), 500