from flask import render_template, redirect, request, session, flash

from flask_app import app
from ..models.user import User


@app.route("/users")
def index():
    users = User.get_all_users()

    return render_template("index.html", all_users = users)


@app.route('/users/new')
def newUser():
    return render_template('create.html')


@app.route('/users/create', methods=['POST'])
def createUser():
    new_user = User.create

    return redirect(url_for(".show_user", user_id = new_user))


@app.route('/users/<int:user_id>/edit')
def edit_user_form(user_id):
    user_list = User.get_one_user(user_id)

    return render_template("edit_user.html", user = user_list)


@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    result = User.update_user(user_id)

    return redirect('/show_user')


@app.route('/users/<int:user_id>')
def show_user(user_id):
    result = User.get_one_user(user_id)

    return render_template("show_user.html", user = result)


@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    User.delete_user({"id": user_id})

    return redirect('/users')