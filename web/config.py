class Config(object):
    TESTING = True

    @property
    def DATABASE_URI(self):
        return "{}://{}:{}@{}:{}/{}".format(
            self.DB_SCHEMA,
            self.DB_USER,
            self.DB_PASSWORD,
            self.DB_HOST,
            self.DB_PORT,
            self.DB_NAME
        )

class DevelopmentConfig(Config):
    pass

class ProductionConfig(Config):
    TESTING = False

class TestingConfig(Config):
    DB_SCHEMA = 'sqlite'
    DB_USER = '/' # for sqlite in memory
    DB_PASSWORD = ''
    DB_HOST = ''
    DB_PORT = ''
    DB_NAME = ''

