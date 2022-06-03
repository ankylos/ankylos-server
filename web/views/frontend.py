from flask import Blueprint, current_app, render_template

frontend = Blueprint('frontend', __name__, url_prefix='/')

@frontend.route('/')
def index():
    return render_template('index.html')
