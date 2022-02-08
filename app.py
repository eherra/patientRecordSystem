from flask import Flask, session
from flask_wtf.csrf import CSRFProtect
from os import getenv

app = Flask(__name__)

app.secret_key = getenv("SECRET_KEY")
app.config["FLASK_ENV"] = getenv("FLASK_ENV")
app.config["WTF_CSRF_SECRET_KEY"] = getenv("WTF_CSRF_SECRET_KEY")
csrf = CSRFProtect(app)

from views import appointments, auth, errors, messages, \
       prescriptions, profiles, register, settings

app.register_blueprint(appointments.appointments_bp)
app.register_blueprint(auth.auth_bp)
app.register_blueprint(errors.errors_bp)
app.register_blueprint(messages.messages_bp)
app.register_blueprint(prescriptions.prescriptions_bp)
app.register_blueprint(profiles.profiles_bp)
app.register_blueprint(register.register_bp)
app.register_blueprint(settings.settings_bp)