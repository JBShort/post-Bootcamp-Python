from flask import render_template, redirect, request, session, flash

from flask_app import app
from ..models.dojo import Dojo


@app.route("/dojos")
def index():
    dojos = Dojo.get_all_dojos()

    return render_template("index.html", dojos = dojos)


@app.route("/dojos/<int:dojo_id>")
def show_dojo(dojo_id):
    one_dojo = Dojo.get_dojo_with_ninjas({"id": dojo_id})

    return render_template("dojo_show.html", dojo = one_dojo)


@app.route("/dojos/create", methods = ['POST'])
def create_dojo():
    Dojo.create_dojos(request.form)

    return redirect("/dojos")