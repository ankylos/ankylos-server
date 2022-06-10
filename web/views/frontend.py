from sqlalchemy import select
from flask import request, Blueprint, render_template, url_for, redirect
from web.models.pages import Pages
from web.database import db_session

frontend = Blueprint("frontend", __name__, url_prefix="/")


@frontend.route("/", methods=["get"])
def index():
    return render_template("index.html")


@frontend.route("/search", methods=["get"])
def search():
    args = request.args

    if not args.get("q", default="", type=str):
        return redirect(url_for("frontend.index"))

    # Handle get search term
    stmt = select(Pages).where(Pages.name == args.get("q"))
    results = db_session.execute(stmt)

    # return results
    return render_template("search.html", q_results=results)
