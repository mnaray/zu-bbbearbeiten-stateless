import helper
from flask import Flask, request, Response, render_template, redirect, url_for

app = Flask(__name__)

# @app.route("{route}") bestimmt was passiert wenn die jeweilige Route in die Suchleiste eingegeben wird. (Routing)


@app.route("/")
def index():
    todos = helper.get_all()
    return render_template(
        "index.html", todos=todos, categories=helper.categories
    )  # Hier wird das index.html mit den Daten in items gerendert.


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    date = request.form.get("date")
    category = request.form.get("category")
    description = request.form.get("description")
    helper.add(text, date, category, description)
    return redirect(
        url_for("index")
    )  # Hier wird index() mit der überarbeiteten Liste neu geladen.


@app.route("/update/<int:index>")
def update(index):
    helper.update(index)
    return redirect(
        url_for("index")
    )  # Hier wird auch index() mit der überarbeiteten Liste neu geladen.


@app.route("/download")
def download():
    return Response(
        helper.get_csv(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; zu-bbbearbeiten.csv"},
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
