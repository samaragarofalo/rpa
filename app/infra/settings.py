import os
from pymongo import MongoClient

# Se a variável de ambiente MONGO_URI não estiver definida, assume "mongodb://mongo:27017/" para o docker,
# ou "mongodb://localhost:27017/" para execução local.
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/")

client = MongoClient(MONGO_URI)
db = client["turivius_challenge"]
collection = db["scraping_data"]
