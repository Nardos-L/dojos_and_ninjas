from flask import render_template, request, redirect
from flask_app import app

from flask_app.models.model_ninjas import Ninja

from flask_app.models.model_dojos import Dojo

@app.route("/add/new")
def add_ninja():
    dojos = Dojo.get_all()
    
    return render_template("create.html", all_dojos = dojos)


@app.route("/create/ninja", methods=["POST"])
def create_ninja():
    Ninja.save(request.form)

    return redirect("/")  

