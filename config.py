import os


class Config(object):
    TESTING = True
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return self._database_uri


class DevelopmentConfig(Config):
    def __init__(self):
        self._database_uri = "sqlite:///{}".format(
            os.path.join(self.BASE_PATH, "dev.sqlite")
        )


class ProductionConfig(Config):
    TESTING = False


class TestingConfig(Config):
    def __init__(self):
        self._database_uri = "sqlite://"
