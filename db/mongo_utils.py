from pymongo import MongoClient


class MongoDB:
    def __init__(self, uri):
        self.client = MongoClient(uri)

    def get_collection(self, db_name, collection_name):
        db = self.client[db_name]
        collection = db[collection_name]
        return collection

    def insert_one(self, db_name, collection_name, document):
        collection = self.get_collection(db_name, collection_name)
        return collection.insert_one(document)

    def insert_many(self, db_name, collection_name, documents):
        collection = self.get_collection(db_name, collection_name)
        return collection.insert_many(documents)

    def find_one(self, db_name, collection_name, query):
        collection = self.get_collection(db_name, collection_name)
        return collection.find_one(query)

    def find_many(self, db_name, collection_name, query):
        collection = self.get_collection(db_name, collection_name)
        return collection.find(query)

    def update_one(self, db_name, collection_name, query, update):
        collection = self.get_collection(db_name, collection_name)
        return collection.update_one(query, update)

    def update_many(self, db_name, collection_name, query, update):
        collection = self.get_collection(db_name, collection_name)
        return collection.update_many(query, update)

    def delete_one(self, db_name, collection_name, query):
        collection = self.get_collection(db_name, collection_name)
        return collection.delete_one(query)

    def delete_many(self, db_name, collection_name, query):
        collection = self.get_collection(db_name, collection_name)
        return collection.delete_many(query)
