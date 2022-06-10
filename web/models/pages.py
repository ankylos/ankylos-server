from sqlalchemy import Column, Integer, String
from web.database import Base


class Pages(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True)
    name = Column(String, default="")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Page {}: {}>".format(self.id, self.name)
