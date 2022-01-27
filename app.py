from flask import Flask
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes.messages, routes.profiles, routes.login, \
       routes.settings, routes.appointments, routes.prescriptions, \
       routes.register
