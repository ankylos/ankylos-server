from flask import Flask


def create_app(config: object):
    app = Flask(__name__)
    app.config.from_object(config)

    from web.models import db
    with app.app_context():
        db.create_all()

    from web.views.frontend import frontend

    app.register_blueprint(frontend)

    return app
