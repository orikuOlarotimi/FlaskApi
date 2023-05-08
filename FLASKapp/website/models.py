
from . import db
from flask_login import UserMixin



class Note(db.Document):
    data = db.StringField()


class User(UserMixin, db.Document):
    user_id = db.IntField(primary_key=True, default=True)
    email = db.EmailField(max_lenght=150, unique=True)
    password = db.StringField(max_lenght=150)
    first_name = db.StringField(max_lenght=150)
    # Note = db.StringField()

