from conexao_bd.mySQL_queries import MySQLQueries

from conexao_bd.mongoDB_queries import MongoDBQueries

import json


LISTA_COLECOES = ['ALUNOS', 'LIVROS', 'EMPRESTIMOS']

mongoDB_connector = MongoDBQueries()


def criar_colecoes(sobreescrever: bool = False):
    """

    Funcao criar_colecoes - Responsavel por criar as colecoes necessarios para o funcionamento do projeto, a partir das 

    tabelas no banco de dados MySQL, no banco de dados MongoDB 
    """


    #Realiza a conexao ao banco de dados
    mongoDB_connector.connect()

    colecoes_existentes = mongoDB_connector.db.list_collection_names()


    #Percorre a lista de nomes das tabelas necessarias para o sistema
    for colecao in LISTA_COLECOES:


        #Sobrescreve a colecao caso ela ja exista e na chamada do metodo esteja sinalizado para tal
        if (colecao in colecoes_existentes):

            if (sobreescrever):

                mongoDB_connector.db.drop_collection(colecao)
        

        #Cria a tabela no mongoDB
        mongoDB_connector.db.create_collection(colecao)
    

    mongoDB_connector.close()


def extrair_inserir_dados():
    """

    Metodo extrair_inserir_dados - Responsavel por extrair os registros das tabelas no banco MySQL e transformar em 

    documentos para as colecoes no banco mongoDB
    """


    #Realiza a conexao ao banco de dados MySQL
    mySQL_connector = MySQLQueries()

    mySQL_connector.connect()


    #Realiza a conexao ao banco de dados mongoDB
    mongoDB_connector.connect()


    #Moolde de query para extrair todos os registros de cada tabela
    query_sql: str = "select * from {tabela}"

    for colecao in LISTA_COLECOES:

        #Extrai os registros da tabela e guarda o resultado em um DataFrame
        df = mySQL_connector.execute_query_dataframe(query_sql.format(tabela=colecao))

        #Transforma o campo data_devolucao da tabela EMPRESTIMOS em um formato valido para criar os documentos
        if (colecao == "EMPRESTIMOS"):

            for c in range(len(df)):

                df.iat[c,3] = df["data_devolucao"][c].strftime("%Y-%m-%d")

        
        #Converte o DataFrame em um arquivo Json
        dados = json.loads(df.T.to_json()).values()

        #Insere os documentos gerados a partir dos registros na tabela no banco de dados MongoDB do projeto
        mongoDB_connector.db[colecao].insert_many(dados)
    

    mongoDB_connector.close()


##Programa a ser rodado quando o arquivo for executado
if __name__ == "__main__":

    criar_colecoes(True)

    extrair_inserir_dados()

    print("Coleções e Documentos criados com sucesso")

