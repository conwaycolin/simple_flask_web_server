from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/get_number")
def get_number():
    return jsonify({"number": 42})

if __name__ == "__main__":
    app.run(port="8000")