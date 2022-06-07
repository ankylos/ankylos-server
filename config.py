class Config(object):
    TESTING = True
    DB_SCHEMA = ''
    DB_USER = ''
    DB_PASSWORD = ''
    DB_HOST = ''
    DB_PORT = ''
    DB_NAME = ''

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return "{}://{}:{}@{}:{}/{}".format(
            self.DB_SCHEMA,
            self.DB_USER,
            self.DB_PASSWORD,
            self.DB_HOST,
            self.DB_PORT,
            self.DB_NAME
        )

class DevelopmentConfig(Config):
    DB_SCHEMA = 'sqlite'
    DB_USER = '/' # for sqlite in memory

class ProductionConfig(Config):
    TESTING = False

class TestingConfig(Config):
    DB_SCHEMA = 'sqlite'
    DB_USER = '/' # for sqlite in memory
