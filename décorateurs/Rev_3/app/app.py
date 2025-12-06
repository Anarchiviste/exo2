from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
import json  # besoin de url_for pour générer des urls dynamiques

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    error = ""
    result = ""
    data_input = ""
    list_key = []
    if request.methods == "POST":
        try:
            data_input = request.form["input"]
            result = json.loads(data_input)[0]
            list_key = list(result.keys())
        except json.JSONDecodeError as e:
            error = f"Invalid Json input"
        except Exception as e:
            error = f"Unexpected Error"
    return render_template(
        "templates/index.html",
        error=error,
        data=data_input,
        result=result,
        key=list_key,
    )
