from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route('/home')
def hello():
    return redirect("http://localhost/", 302)

@app.route("/")
def index():
    return b"<title>Index</title>"

@app.route("/about")
def about():
    return b"<title>About</title>"

@app.route("/winc")
def winc():
    return b"<title>Winc</title>"
