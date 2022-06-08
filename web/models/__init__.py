# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from flask import current_app

# engine = create_engine(
# current_app.config["SQLALCHEMY_DATABASE_URI"],
# connect_args={"check_same_thread": False},
# )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base(bind=engine)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
