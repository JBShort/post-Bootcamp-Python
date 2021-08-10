from flask import Flask, render_template, request, redirect, url_for
from mysqlconnection import connectToMySQL

app = Flask(__name__)


@app.route("/users")
def index():
    mysql = connectToMySQL("users_schema")
    users = mysql.query_db("SELECT id, CONCAT(first_name, ' ', last_name) AS full_name, email, created_at  FROM users;")
    print(users)
    return render_template("index.html", all_users = users)


@app.route('/users/create', methods=['POST'])
def createUser():

    query = "INSERT INTO users (first_name, Last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"],
    }
    new_user = connectToMySQL("users_schema").query_db(query, data)
    print(new_user)

    return redirect(url_for(".show_user", user_id = new_user))


@app.route('/users/new')
def newUser():
    return render_template('create.html')


@app.route('/users/<int:user_id>/edit')
def edit_user_form(user_id):
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        "id": user_id
    }

    user_list = connectToMySQL("users_schema").query_db(query, data)

    return render_template("edit_user.html", user = user_list[0])


@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    query = "UPDATE users SET first_name = %(fname)s, Last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "id": user_id
    }

    result = connectToMySQL("users_schema").query_db(query, data)

    return redirect('/users')


@app.route('/users/<int:user_id>')
def show_user(user_id):
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        "id": user_id
    }
    result  = connectToMySQL('users_schema').query_db(query, data)
    print(result[0])

    return render_template("show_user.html", user = result[0])


@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    query = "DELETE FROM users WHERE id = %(id)s;"
    data = {
        "id": user_id
    }

    result = connectToMySQL('users_schema').query_db(query, data)

    return redirect('/users')


if __name__=="__main__":
    app.run(debug=True)