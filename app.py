if __name__ == '__main__':
    from web import create_app
    from config import DevelopmentConfig


    app = create_app(DevelopmentConfig)
    app.run()
