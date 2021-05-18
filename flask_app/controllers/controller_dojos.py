from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.model_dojos import Dojo

@app.route("/")
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)

@app.route("/create", methods=["POST"])
def create():
    Dojo.save(request.form)
    return redirect("/")

@app.route("/dojo/show/<id>")
def dojo_show(id):
    data = {
        "id":id
    }
    return render_template("show.html",dojo = Dojo.get_dojos_with_ninjas(data))




