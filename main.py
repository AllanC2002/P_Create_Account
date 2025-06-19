from flask import Flask, request, jsonify
from services.funtions import create_user

app = Flask(__name__)

@app.route("/create_account", methods=["POST"])
def create_account():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload received"}), 400
    return create_user(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
