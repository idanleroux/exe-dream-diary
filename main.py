import flask
from flask import render_template

app = flask.Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/login")
def login():
    return render_template("login.html")

@app.get("/upload_dream")
def upload_dream():
    return render_template("upload_dream.html")

@app.get("/view_public")
def view_public():
    return render_template("view_public.html")

@app.get("/view_private")
def view_private():
    return render_template("view_private.html")

@app.get("/profile")
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)