from conexao_bd.mySQL_queries import MySQLQueries 

def criar_tabelas(query: str):
    """
    Função criar_tabelas - Responsável pela criação das tabelas necessárias para o funcionamento do projeto
    Parâmetros:
    query - Código SQL para criação das tabelas
    """
    
    #Guarda em uma variável o código SQL de criação da tabela, separando as linhas de comando por meio do ';'
    lista_comandos = query.split(';')

    #Cria uma nova conexão com o banco de dados
    mySQL_connector = MySQLQueries()
    mySQL_connector.connect()

    #Percorre cada uma das linhas de comando, tentando exercuta-la e informando ao usuário do sucesso ou não da operação
    for comando in lista_comandos:
        try:
            mySQL_connector.execute_DDL(comando)
            print(f"comando '{comando}' executado")
        except Exception as e:
            print(f"Falha ao exercutar comando '{comando}'\n{e}")

def gerar_registros(query:str):
    """
    Função gerar_registros - Responsável pela inserção de registros de exemplos nas tabelas para facilitar a experiência do usuário
    Parâmetros:
    query - Código SQL para inserção dos registros nas tabelas
    """

    #Guarda em uma variável o código SQL de inserção de registros, separando as linhas de comando por meio do ';'
    lista_comandos = query.split(';')

    #Cria uma nova conexão com o banco de dados
    mySQL_connector = MySQLQueries(can_write=True)
    mySQL_connector.connect()

    #Percorre cada uma das linhas de comando, tentando exercuta-la e informando ao usuário do sucesso ou não da operação
    for comando in lista_comandos:
        if len(comando) > 0:
            mySQL_connector.write(comando)
            print(f"Comando '{comando}' executado")

def run():
    """
    função run - Responsável por executar todo o algoritmo para a criação das tabelas e inserção de registro quando o arquivo for executado
    """
    
    #Guarda em uma variável o arquivo contendo o código SQL para criação das tabelas
    with open("../sql_tabelas/criar_tabelas_biblioteca_escolar.sql") as f:
        query_criacao = f.read()
    #Realiza a função para criação das tabelas
    print("Criando tabela")
    criar_tabelas(query_criacao)
    print("Tabela criada com sucesso")

    #Guarda em uma variável o arquivo contendo o código SQL para inserção de regisros
    with open("../sql_tabelas/inserir_dados_tabelas_biblioteca_escolar.sql") as f:
        query_registros = f.read()
    
    #Realiza a função para inserção de registros
    print("Inserindo registros na tabela")
    gerar_registros(query_registros)
    print("Registros inseridos com sucesso")
  
if '__main__' == __name__:
    run()


