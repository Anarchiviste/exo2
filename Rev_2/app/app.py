from flask import Flask
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route("/")
def home():
    return f"<p> il faut entrer des paramètres dans la barre d'url </p>"


@app.route("/division/<int:a>/<int:b>")
def division(a, b):
    c = a / b
    return f"Le résultat est {c}"
