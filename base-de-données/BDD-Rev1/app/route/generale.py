from ..app import app
from flask import render_template

@app.route("/")
def home():
	return "un petit message pour éviter d'avoir pleins d'erreurs"