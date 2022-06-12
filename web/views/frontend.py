from sqlalchemy import select, column
from flask import request, Blueprint, render_template, url_for, redirect
from web.models.pages import Pages
from web.database import db_session

frontend = Blueprint("frontend", __name__, url_prefix="/")


@frontend.route("/", methods=["get"])
def index():
    return render_template("index.html")


@frontend.route("/search", methods=["get"])
def search():
    search_term = request.args.get('q', default='', type=str)

    if not search_term:
        return redirect(url_for("frontend.index"))

    # Handle get search term
    # stmt = select(Pages).where(Pages.name == args.get("q"))
    # results = db_session.execute(stmt)
    sql_q = db_session.query(Pages).filter(Pages.name.like("%{}%".format(search_term)))
    results = [_.name for _ in sql_q.all()]

    # return results
    return render_template("search.html", q_results=results)
