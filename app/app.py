from flask import Flask, jsonify
from app.db import get_users

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>API läuft!</h1><br><img src="https://az900storagewarda.blob.core.windows.net/uploads/Bildschirmfoto%202026-04-03%20um%2013.30.22.png?sp=r&st=2026-04-14T06:23:36Z&se=2026-04-14T14:38:36Z&spr=https&sv=2025-11-05&sr=b&sig=FTB9t%2FtnDcLV9XFhMZ6OetQso4gWfVSjc9Yst66egvI%3D" width="300">'

@app.route("/api/users")
def users():
    return jsonify(get_users())

@app.route("/api/products")
def products():
    data = [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Maus"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)