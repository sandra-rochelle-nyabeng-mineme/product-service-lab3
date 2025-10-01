import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
 
# Load variables from .env file
load_dotenv()
 
app = Flask(__name__)
CORS(app)

 
@app.get("/products")
def get_products():
    products = [
        {"id": 1, "name": "Dog Food",  "price": 19.99},
        {"id": 2, "name": "Cat Food",  "price": 34.99},
        {"id": 3, "name": "Bird Seeds","price": 10.99},
    ]
    return jsonify(products)
 
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # fallback to 5000 if not set
    app.run(host="0.0.0.0", port=port)