from flask import Flask, app


def create_app(config: object) -> app.Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    # associate db object with flask app
    from web.models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from web.views.frontend import frontend

    app.register_blueprint(frontend)

    return app
