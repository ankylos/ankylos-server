from web.models import db


class Pages(db.Model):
    __tablename__ = "pages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Page {}: {}>".format(self.id, self.name)
