from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, create_session, declarative_base

engine = None
db_session = scoped_session(lambda: create_session(bind=engine))

Base = declarative_base()

def init_engine(uri, **kwargs):
    global engine
    engine = create_engine(uri, **kwargs)
    return engine

def init_db():
    from web.models.Pages import Pages
    Base.metadata.create_all(engine)
