from flask import render_template, request, redirect, session
from flask_app import app
import babel
from ..models.tv_show import TV_show
from ..models.user import User


@app.route("/new")
def new_show():
    if 'uuid' not in session:
        return redirect("/")
    

    return render_template("new_show.html", user = User.get_by_id({"id": session['uuid']}))

@app.route("/create", methods = ['POST'])
def create_show():
    if not TV_show.validator(request.form):
        return redirect("/new")

    data = {
        "user_id": session['uuid'],
        "title": request.form['title'],
        "network": request.form['network'],
        "release_date": request.form['release_date'],
        "description": request.form['description']
    }
    TV_show.create(data)

    return redirect("/dashboard")


@app.route("/show/<int:tv_show_id>")
def show_tv_show(tv_show_id):
    if 'uuid' not in session:
        return redirect("/")

    return render_template("/display_show.html", tv_show = TV_show.get_one({"id": tv_show_id}))


@app.route("/edit/<int:tv_show_id>")
def edit_tv_show(tv_show_id):
    if 'uuid' not in session:
        return redirect("/")

    

    return render_template("/edit_show.html", tv_show = TV_show.get_one({"id": tv_show_id}), user = User.get_by_id({"id": session['uuid']}))

@app.route("/update/<int:tv_show_id>", methods = ['POST'])
def update(tv_show_id):
    if not TV_show.validator(request.form):
        return redirect(f"/update/{tv_show_id}")

    data = {
        "title": request.form['title'],
        "network": request.form['network'],
        "release_date": request.form['release_date'],
        "description": request.form['description'],
        "id": tv_show_id
    }
    TV_show.update_tv_show(data)

    return redirect("/dashboard")


@app.route("/delete/show/<int:tv_show_id>")
def delete_show(tv_show_id):
    TV_show.delete({"id": tv_show_id})

    return redirect("/dashboard")



@app.template_filter()
def format_datetime(value, format='medium'):
    if format == 'full':
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format="EE dd.MM.y HH:mm"
    return babel.dates.format_datetime(value, format)