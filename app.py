
from app import app,socketio

socketio.run(app,host='127.0.0.1',debug=True,port=5000)
