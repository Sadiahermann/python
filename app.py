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

@app.route("/utilisateurs", methods=["GET", "POST"])
def users():
    return render_template("utilisateurs.html" )

@app.route("/expediteurs", methods=["GET", "POST"])
def expediteurs():
    return render_template("expediteurs.html" )

@app.route("/destinateurs", methods=["GET", "POST"])
def destinateurs():
    return render_template("destinateurs.html" )

@app.route("/services", methods=["GET", "POST"])
def services():
    return render_template("services.html" )

@app.route("/courriers", methods=["GET", "POST"])
def courriers():
    return render_template("courriers.html" )


@app.route("/statuts", methods=["GET", "POST"])
def statuts():
    return render_template("statuts.html" )




@app.errorhandler(404)
def pagenotfind(e):
    return render_template("page.html"), 404

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
