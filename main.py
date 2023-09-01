import helper
from flask import Flask, request, Response, render_template, redirect, url_for

app = Flask(__name__)

# @app.route("{route}") bestimmt was passiert wenn die jeweilige Route in die Suchleiste eingegeben wird. (Routing)


@app.route("/")
def index():
    todos = helper.get_all()
    return render_template(
        "index.html", todos=todos
    )  # Hier wird das index.html mit den Daten in items gerendert.


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    date = request.form.get("date")
    helper.add(text, date)
    return redirect(
        url_for("index")
    )  # Hier wird index() mit der überarbeiteten Liste neu geladen.


@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(
        url_for("index")
    )  # Hier wird auch index() mit der überarbeiteten Liste neu geladen.
