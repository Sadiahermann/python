from flask import Flask, render_template, request, redirect,url_for
from models import db
from models.produit_model import Produit


app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///ecommerce.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False