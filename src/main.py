# src/main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn

# Charger les variables d'environnement depuis .env (comme dotenv en Rust)
load_dotenv()

# Récupérer le port, valeur par défaut : 3030
PORT = int(os.getenv("PORT", "3030"))

# Créer l'application FastAPI
app = FastAPI()

# Configurer CORS (comme warp.cors().allow_any_origin().allow_methods(["GET"]))
#app.add_middleware(
 #   CORSMiddleware,
 #   allow_origins=["*"],  # toutes origines
#    allow_methods=["GET"],  # seulement GET
#    allow_headers=["*"],  # tous les headers
#)

# Route GET /products
@app.get("/products")
async def get_products():
    return [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]

# Point d'entrée (équivalent à warp::serve)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
