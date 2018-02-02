from core import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    confirmation_sent_on = db.Column(db.DateTime, nullable=True, default=None)
    confirmed = db.Column(db.Boolean, nullable=True, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True, default=None)

    def __init__(self, email, confirmation_sent_on):
        self.email = email
        self.confirmation_sent_on = confirmation_sent_on
        self.confirmed = False
        self.confirmed_on = None
        