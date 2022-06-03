from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from web.views.frontend import frontend

    app.register_blueprint(frontend)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
