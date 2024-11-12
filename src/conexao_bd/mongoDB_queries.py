import pymongo

class MongoDBQueries:
    def __init__(self):
        self.host = "localhost"
        self.port = "27017"
    
    def __del__(self):
        if hasattr(self, "mongo_client"):
            self.close()

    def connect(self):
        self.mongo_client = pymongo.MongoClient(f"mongodb://{self.host}:{self.port}/")
        self.db = self.mongo_client["Sistema_Escolar_Biblioteca"]

    def close(self):
        self.mongo_client.close()
    
