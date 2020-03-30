from app import db

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    mail = db.Column(db.String(64))
    wine = db.Column(db.String(64))
    specialneeds = db.Column(db.String(500))
    place_wish = db.Column(db.String(64))
    cocktail_who = db.Column(db.String(64))
    avec = db.Column(db.Boolean())
    avec_name = db.Column(db.String(64))
    avec_wine = db.Column(db.String(64))
    avec_specialneeds = db.Column(db.String(500))

    datetime = db.Column(db.DateTime())

