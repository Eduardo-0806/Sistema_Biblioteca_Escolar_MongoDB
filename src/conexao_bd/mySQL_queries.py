import mysql.connector
from pandas import DataFrame

class MySQLQueries:
    """
    Classe 'MySQLQueries' - responsável por realizar e controlar a conexão com o banco de dados mySQL, tal como realizar os comandos DDL, inserção de dados/registros e execução de queries com retorno DataFrame da classe pandas
    """
    def __init__(self, can_write:bool = False):
        self.can_write: bool = can_write
        self.host = 'localhost'
        
        with open("conexao_bd/autenticador/autenticador_mySQL.txt") as f:
            self.database, self.user, self.password = f.read().split(',')
    
    def __del__(self):
        if self.cursor:
            self.close()
    
    def connect(self):

        """
        Esse método é responsável por realizar a conexão com o banco de dados mySQL, utilizando dos parâmetros necessários para isso.
        Parâmetros:

        - host: Localização do servidor mySQL;
        - database: Nome dado ao banco de dados, criado pelo usuário, ao qual a classe tentará realizar a conexão;
        - user: Nome do usuário da conexão mySQL criada pelo usuário;
        - password: Senha da conexão mySQL criada pelo usuário.

        Retorno: Um cursor que permite a utilização das funções da classe mysql.connector, por consequência a manipulação do banco de dados e suas tabelas
        """
        
        self.con = mysql.connector.connect(host = self.host, database = self.database, user= self.user, password = self.password) 
        self.cursor = self.con.cursor()
        return self.cursor

    def close(self):

        """
        Esse método é responsável por realizar o fechamento da conexão com o banco de dados, quando a mesma não for mais necessária
        """

        if self.cursor:
            self.cursor.close()

    
    def execute_query_dataframe(self, query:str):

        """
        Esse método é responsável por realizar uma consulta(query) no banco de dados.
        Parâmetros:
        - query: Comando/consulta a ser realizado no banco de dados
        Retorno: Um DataFrame da biblioteca pandas, exibindo os registros obtidos da query realizada.
        """

        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.columns = self.cursor.column_names
        self.dataframe = DataFrame(data=self.result, columns=self.columns)
        return self.dataframe
    
    def execute_DDL(self, query: str):

        """
        Esse método é responsável por realizar um comando DDL(CREATE, ALTER, DROP) no banco de dados.
        Parâmetros:
        - query: Comando DDL a ser realizado no banco de dados
        """

        self.cursor.execute(query)
    
    def write(self, query:str):

        """
        Esse método é responsável por realizar a inserção de dados/registros no banco de dados, caso aquele conexão tenha permissão para tal.
        Parâmetros:
        - query: Comando a ser realizado no banco de dados
        """

        if (not self.can_write):
            print("Essa conexão não tem permissão para inserir registros")
        else:
            self.cursor.execute(query)
            self.con.commit()
