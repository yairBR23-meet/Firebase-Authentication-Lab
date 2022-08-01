from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

Config = {
  "apiKey": "AIzaSyD0f7tNDBC0QDyUtykeAGuWmiC7zNWDiYo",
  "authDomain": "fir-authentication-lab1.firebaseapp.com",
  "projectId": "fir-authentication-lab1",
  "storageBucket": "fir-authentication-lab1.appspot.com",
  "messagingSenderId": "70194483004",
  "appId": "1:70194483004:web:369b2587e08c8ff1a75839",
  "measurementId": "G-FP302SHZTV",
  "databaseURL": "https://fir-authentication-lab1-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()


app = Flask(__name__)

app.config['SECRET_KEY'] = "Your_secret_string"



app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
        login_session['user'] = auth.sign_in_with_email_and_password(email, password)
        return redirect(url_for('add_tweet'))
       except:
        error = "Authentication failed"
        return render_template("signin.html")
   else:
        return render_template("signin.html")

    


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        return redirect(url_for('add_tweet'))
       except:
        error = "Authentication failed"
        return render_template("signup.html")
   else:
        return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(debug=True)