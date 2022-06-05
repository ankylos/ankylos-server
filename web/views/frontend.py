from flask import request, Blueprint, current_app, render_template

frontend = Blueprint("frontend", __name__, url_prefix="/")


@frontend.route("/", methods=["get"])
def index():
    return render_template("index.html")


@frontend.route("/search", methods=["get"])
def search():
    args = request.args

    return render_template("search.html")
