from flask import Flask, jsonify, render_template
from weather import get_temperature
from weather import get_conditions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get_temperature")
def get_temperature_route():
    temperature = get_temperature()
    return jsonify(temperature)

@app.route("/get_conditions")
def get_conditions_route():
    conditions = get_conditions()
    return jsonify(conditions)

if __name__ == "__main__":
    app.run(port="8000")