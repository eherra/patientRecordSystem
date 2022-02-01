from flask import render_template, jsonify, Blueprint

errors_bp = Blueprint("error", __name__)

@errors_bp.app_errorhandler(401)
def user_not_authorized(error):
    return jsonify(error=str(error)), 401

@errors_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('error/404.html'), 404

@errors_bp.app_errorhandler(500)
def internal_server_error(error):
    return render_template('error/500.html'), 500