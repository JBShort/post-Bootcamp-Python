from flask import render_template, request, redirect, session
from flask_bcrypt import Bcrypt

from flask_app import app
from ..models.user import User
from ..models.tv_show import TV_show

bcrypt = Bcrypt(app)



@app.route("/")
def index():
    if "uuid" in session:
        return redirect("/dashboard")
    
    return render_template("index.html")


@app.route("/register", methods=['POST'])
def register():
    if not User.register_validator(request.form):
        return redirect("/")
    
    hashywashy = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": hashywashy
    }

    user_id = User.create(data) 

    session['uuid'] = user_id

    return redirect("/dashboard")


@app.route("/login", methods=['POST'])
def login():
    if not User.login_validator(request.form):
        return redirect("/")
    
    user = User.get_by_email({"email": request.form['email']})

    session['uuid'] = user.id

    return redirect("/dashboard")


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")


@app.route("/dashboard")
def success():
    if "uuid" not in session:
        return redirect("/")
    logged_user = User.get_by_id({"id": session['uuid']})

    all_tv_shows = TV_show.get_all_tv_shows()

    return render_template("dashboard.html", user = logged_user, all_tv_shows = all_tv_shows)