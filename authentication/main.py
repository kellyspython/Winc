import os

from flask import Flask, redirect, render_template, request, session, url_for, flash
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    if not session.get('logged_in'):
        return render_template("index.html", title="Index")
    else:
        return redirect('/dashboard/{user}')


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        users = get_users()
        if request.form['username'] in users:
            password = request.form['password']
            user = request.form['username']
            user_hash_password = hash_password(password)
            
            if user_hash_password == users[user]:
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect('/dashboard/{user}')
            else:
                error = 'Invalid username/password'
                return render_template('login.html', error=error)
                       
    return render_template("login.html", title="Login")


@app.route("/dashboard/{<user>}")
def dashboard(user):
    if 'username' in session:
        s = session['username']  
        return render_template("dashboard.html", name=s)

    return render_template("dashboard.html", title="Dashboard")


@app.route("/logout", methods=["GET", "POST"])
def logout():

    session['logged_in'] = False
    return redirect('/')
