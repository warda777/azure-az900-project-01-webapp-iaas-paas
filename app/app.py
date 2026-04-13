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
    
@app.route("/api/products")
def products():
    data = [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Maus"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)