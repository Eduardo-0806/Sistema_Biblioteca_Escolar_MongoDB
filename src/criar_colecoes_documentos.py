from conexao_bd.mySQL_queries import MySQLQueries
from conexao_bd.mongoDB_queries import MongoDBQueries
import json

LISTA_COLECOES = ['ALUNOS', 'LIVROS', 'EMPRESTIMOS']
mongoDB_connector = MongoDBQueries()

def criar_colecoes(sobreescrever: bool = False):
    mongoDB_connector.connect()
    colecoes_existentes = mongoDB_connector.db.list_collection_names()

    for colecao in LISTA_COLECOES:
        if (colecao in colecoes_existentes):
            if (sobreescrever):
                mongoDB_connector.db.drop_collection(colecao)
        
        mongoDB_connector.db.create_collection(colecao)
    
    mongoDB_connector.close()

def extrair_inserir_dados():
    mySQL_connector = MySQLQueries()
    mySQL_connector.connect()
    mongoDB_connector.connect()
    querie_sql: str = "select * from {tabela}"
    for colecao in LISTA_COLECOES:
        df = mySQL_connector.execute_query_dataframe(querie_sql.format(tabela=colecao))
        if (colecao == "EMPRESTIMOS"):
            for c in range(len(df)):
                df.iat[c,3] = df["data_devolucao"][c].strftime("%Y-%m-%d")
        dados = json.loads(df.T.to_json()).values()
        mongoDB_connector.db[colecao].insert_many(dados)
    
    mongoDB_connector.close()

if __name__ == "__main__":
    criar_colecoes(True)
    extrair_inserir_dados()
    print("Coleções e Documentos criados com sucesso")
