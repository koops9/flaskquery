from app import db

class Reg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    representative = db.Column(db.String(64), index=True)
    greeting = db.Column(db.Boolean())
    food = db.Column(db.String(500))
    alcohol = db.Column(db.String(10))
    #gambina = db.Column(db.Boolean())
    avec = db.Column(db.String(64))
    free = db.Column(db.String(500))

class OKS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    table = db.Column(db.Boolean(8))
    representative = db.Column(db.String(24))
    discussion = db.Column(db.String(500))
    alcohol = db.Column(db.String(10))
    drink = db.Column(db.String(10))
    food = db.Column(db.String(500))
    wine = db.Column(db.String(10))
    

class KMP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    representative = db.Column(db.String(24))
    place = db.Column(db.String(64))
    
class Humu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    representative = db.Column(db.String(64), index=True)
    food = db.Column(db.String(500))
    alcohol = db.Column(db.String(10))
    drink = db.Column(db.String(10))
    wine = db.Column(db.String(10))
    avec = db.Column(db.String(64))
    free = db.Column(db.String(500))