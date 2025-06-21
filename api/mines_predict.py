from flask import Flask, request, jsonify
from stake_logic import generate_mines_layout


app = Flask(__name__)

@app.route("/api/mines_predict", methods=["POST"])
def predict():
    data = request.json
    mines = data.get("mines", 3)
    tiles = generate_mines_layout(mines)
    return jsonify({"tiles": tiles})
