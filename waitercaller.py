from flask import Flask
from flask import render_template
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask import redirect
from flask import url_for
from flask import request

#import classes from helper files
from mockdbhelper import MockDBHelper as DBHelper
from user import User



app = Flask(__name__)
login_manager = LoginManager(app)
app.secret_key = 'tPXJY3X37Qybz4QykV+hOyUxVQeEXf1Ao2C8upz+fGQXKsM'

DB = DBHelper()

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    stored_user = DB.get_user(email)
    if stored_user and PH.validate_password(password, stored_user['salt'], stored_user['hashed']):
        user = User(email)
        login_user(user, remember=True)
        return redirect(url_for('account'))
    return home()



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/account")
@login_required

def account():
    return "you are logged in"




if __name__ == '__main__':
    app.run(port = 5000, debug = True)