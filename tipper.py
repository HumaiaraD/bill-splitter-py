
from flask import Flask, request, jsonify
from flask_cors import CORS
from calculate_bill import calculate_bill

app = Flask(__name__)

# Allow ALL origins and allow OPTIONS automatically
CORS(app, supports_credentials=True)

@app.route("/calculate", methods=["POST", "OPTIONS"])
@app.route("/calculate/", methods=["POST", "OPTIONS"])
def calculate():
    if request.method == "OPTIONS":
        return jsonify({"status": "OK"}), 200

    data = request.json

    total, per_person = calculate_bill(
        float(data.get("bill", 0)),
        float(data.get("tip", 0)),
        int(data.get("people", 1))
    )

    return jsonify({"total": total, "per_person": per_person})

@app.route("/")
def home():
    return "Bill Calculator Backend is working!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
