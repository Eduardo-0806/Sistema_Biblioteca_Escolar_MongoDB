import pymongo

class MongoDBQueries:
    def __init__(self):
        self.host = "localhost"
        self.port = 27017
        self.service_name = 'labdatabase'

        with open("conexao_bd/autenticador/autenticador_mondoDB.txt") as f:
            self.usuario, self.senha = f.read().split(",")
    
    def __del__(self):
        if hasattr(self, "mongo_client"):
            self.close()

    def connect(self):
        self.mongo_client = pymongo.MongoClient(f"mongodb://{self.usuario}:{self.senha}@localhost:27017/")
        self.db = self.mongo_client["labdatabase"]

    def close(self):
        self.mongo_client.close()
    
