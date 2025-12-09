from ..app import app
from flask import render_template

@app.route("/")
def base():
	return "un petit message pour éviter d'avoir pleins d'erreurs"

@app.route("/home")
def home():
	return "voici la page home"

@app.route("/home/<int:a>/<int:b>")
def calcule(a:int, b:int):
	c = a + b 
	return f"le résultat est {c}"
