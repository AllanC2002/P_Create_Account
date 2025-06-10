from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/create_account", methods=["GET"])
def create_account():
    
    return jsonify({'error': 'No se pudo obtener el clima'})



if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
