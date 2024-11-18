import pymongo

class MongoDBQueries:
    """
    Classe MongoDBQueries - Responsavel por controlar a conexao com o banco de dados MongoDB, permitindo a realizacao
    dos comandos NoSQL no sistema do projeto, manipulando suas colecoes e documentos
    """

    def __init__(self):
        self.host = "localhost"
        self.port = 27017
        self.service_name = 'labdatabase'

        with open("conexao_bd/autenticador/autenticador_mongoDB.txt") as f:
            self.usuario, self.senha = f.read().split(",")
    
    def __del__(self):
        if hasattr(self, "mongo_client"):
            self.close()

    def connect(self):
        """
        Metodo connect - Responsavel pela realizacao da conexao com o banco de dados, utilizando as informacoes de
        usuario e senha para tal
        """    

        self.mongo_client = pymongo.MongoClient(f"mongodb://{self.usuario}:{self.senha}@localhost:27017/")
        self.db = self.mongo_client["labdatabase"]

    def close(self):
        """
        Metodo close - Responsavel por fechar a conexao com o banco de dados MongoDB
        """

        self.mongo_client.close()
    
