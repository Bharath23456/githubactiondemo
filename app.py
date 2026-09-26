from flask import Flask, jsonify

app = Flask(__name__)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


@app.route("/")
def home():
    return "My DevOps CI/CD Application is Running!"


@app.route("/add/<int:a>/<int:b>")
def addition(a, b):
    return jsonify({
        "operation": "addition",
        "a": a,
        "b": b,
        "result": add(a, b)
    })


@app.route("/subtract/<int:a>/<int:b>")
def subtraction(a, b):
    return jsonify({
        "operation": "subtraction",
        "a": a,
        "b": b,
        "result": subtract(a, b)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)