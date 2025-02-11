import os
import unittest
from pymongo import MongoClient


class TestMongoConnection(unittest.TestCase):
    def test_connection(self):
        mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
        client = MongoClient(mongo_uri)
        try:
            databases = client.list_database_names()
            self.assertIsInstance(databases, list)
            print("Conectado com sucesso! Bancos de dados disponíveis:", databases)
        except Exception as e:
            self.fail(f"Erro ao conectar no MongoDB: {e}")


if __name__ == "__main__":
    unittest.main()
