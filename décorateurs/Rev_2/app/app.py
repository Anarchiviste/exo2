from flask import Flask
from flask import request
from flask import url_for

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


@app.route("/")
def home():
    return f"<p> il faut entrer des paramètres dans la barre d'url </p>"


@app.route("/division/<int:a>/<int:b>")
def division(a, b):
    c = a / b
    return f"Le résultat est {c}"
