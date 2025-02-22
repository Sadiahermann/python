from models import db
class Produit(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)    
    inscription=db.Column(db.String(200), nullable=False)
    
    