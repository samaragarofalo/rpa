import os
from pymongo import MongoClient


def is_docker() :
    """
    Retorna True se o código estiver rodando em um container Docker.
    """
    if os.path.exists('/.dockerenv'):
        return True

    return False


MONGO_URI = os.environ.get("MONGO_URI", "mongodb://mongo:27017/" if is_docker() else "mongodb://localhost:27017/")

client = MongoClient(MONGO_URI)
db = client["turivius_challenge"]
collection = db["scraping_data"]
