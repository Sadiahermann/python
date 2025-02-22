#Flask : Framework web pour créer des applications web en Python.
#render_template : Permet d'afficher des pages HTML en utilisant des templates.
#request : Gère les requêtes HTTP (GET, POST, etc.).
#redirect, url_for : Permettent de rediriger l’utilisateur vers une autre route de l’application.

from flask import Flask, render_template, request, redirect, url_for
#db : Instance de SQLAlchemy pour la gestion de la base de données.
from models import db
#Produit : Modèle de données qui représente un produit (probablement défini dans models/produit_model.py).
from models.produit_model import Produit

#Flask(name) : Initialise l’application Flask.
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)  # Initialise SQLAlchemy avec l'application Flask

@app.route("/", methods=["GET", "POST"])
def home():
    produits = Produit.query.all()
    return render_template("index.html", produits=produits)

@app.route("/ajouter", methods=["GET", "POST"])
def ajouter():
    if request.method == "POST":
        nom = request.form["name"]
        description = request.form["inscription"]
        nouveau_produit = Produit(name=nom, inscription=description)
        db.session.add(nouveau_produit)
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("ajouter.html")



@app.route("/modifier/<int:id>", methods=["GET", "POST"])
def modifier(id):
    produit=Produit.query.get_or_404(id)
    if request.method == "POST":
        produit.name = request.form["name"]
        produit.inscription = request.form["inscription"]
             
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("modifier.html", produit=produit)




@app.errorhandler(404)
def pagenotfind(e):
    return render_template("page.html"), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
