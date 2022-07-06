from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO


app = Flask(__name__)
db = SQLAlchemy(app)

socketio = SocketIO(app, async_mode='threading')
