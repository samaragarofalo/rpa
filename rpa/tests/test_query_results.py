import unittest
from rpa.app.infra.settings import db


class TestQueryMongoDB(unittest.TestCase):
    def test_query_all_documents(self):
        collection_names = db.list_collection_names()
        self.assertIsInstance(collection_names, list)

        all_documents = {}
        for coll_name in collection_names:
            collection = db[coll_name]
            documents = list(collection.find({}))
            all_documents[coll_name] = documents
            print(f"Collection '{coll_name}' possui {len(documents)} documento(s):")
            for doc in documents:
                print(doc)

        self.assertIsInstance(all_documents, dict)


if __name__ == "__main__":
    unittest.main()
