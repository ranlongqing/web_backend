from flask import render_template
from app import app


@app.route('/login.html')
def index():
    print("你好 ，python")
    return render_template("login.html")




