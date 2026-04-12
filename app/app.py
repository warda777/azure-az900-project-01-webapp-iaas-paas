from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API läuft!"

@app.route("/api/users")
def users():
    data = [
        {"id": 1, "name": "Andreas"},
        {"id": 2, "name": "Max"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)