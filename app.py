from flask import Flask

app = Flask(__name__)

import routes.messages, routes.profile