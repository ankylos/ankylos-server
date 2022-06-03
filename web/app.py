from flask import Flask

def create_app(config: object):
    app = Flask(__name__)
    app.config.from_object(config)

    from views.frontend import frontend

    app.register_blueprint(frontend)

    return app

if __name__ == '__main__':
    from config import TestingConfig
    app = create_app(TestingConfig)
    app.run()
