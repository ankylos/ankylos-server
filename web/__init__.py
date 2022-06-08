from flask import Flask, app
from web.database import init_engine, init_db


def create_app(config: object) -> app.Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    init_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    init_db()

    from web.views.frontend import frontend

    app.register_blueprint(frontend)

    return app
