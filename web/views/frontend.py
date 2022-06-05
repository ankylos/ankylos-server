from flask import (request, Blueprint, current_app, render_template, url_for, redirect)

frontend = Blueprint("frontend", __name__, url_prefix="/")


@frontend.route("/", methods=["get"])
def index():
    return render_template("index.html")


@frontend.route("/search", methods=["get"])
def search():
    args = request.args

    if not args.get('q', default='', type=str):
        return redirect(url_for('frontend.index'))
        
    # Handle get search term

    # return results
    return render_template("search.html")
