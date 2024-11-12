from conexao_bd.mySQL_queries import MySQLQueries
from utilitarios import menus

class SplashScreen:
    """
    Classe SplashScreen - Responsável por controlar a tela inicial do sistema, tal como os dados que ela exibe e a sua exibição conforme o fluxo do programa
    """
    def __init__(self):

        #Guarda a consulta de quantidade de registros da tabela Alunos em um tributo da classe
        self.query_total_alunos: str = menus.QUERY_COUNT.format(tabela="ALUNOS")

        #Guarda a consulta de quantidade de registros da tabela Livros em um tributo da classe
        self.query_total_livros: str = menus.QUERY_COUNT.format(tabela="LIVROS")

        #Guarda a consulta de quantidade de registros da tabela Emprestimos em um tributo da classe
        self.query_total_emprestimos: str = menus.QUERY_COUNT.format(tabela="EMPRESTIMOS")

        #Guarda o nome dos responsáveis pelo projeto em um tributo da classe
        self.autores: str = ["Arthur Salume Sobral", "Eduardo Lopes da Victória Scota Almeida", 
        "Henrique Risciere", "Matheus Amorin Domingues"]

        #Guarda o nome da disciplina do projeto em um tributo da classe
        self.disciplina: str = "Banco de Dados"

        #Guarda o nome do professor da disciplina do projeto em um tributo da classe
        self.professor: str = "Prof. M.Sc. Howard Roatti"

        #Guarda o semestra em que a disciplina está sendo cursada em um tributo da classe
        self.semestre: str = "2024/2"
    
    def get_total_alunos(self):

        #Cria uma nova conexão com o banco de dados
        conexao_bd: MySQLQueries = MySQLQueries()
        conexao_bd.connect()

        #Retorna a quantidade de registros cadastrados na tabela Alunos
        return conexao_bd.execute_query_dataframe(self.query_total_alunos)["total_ALUNOS_registros"].values[0]

    def get_total_livros(self):

        #Cria uma nova conexão com o banco de dados
        conexao_bd: MySQLQueries = MySQLQueries()
        conexao_bd.connect()

        #Retorna a quantidade de registros cadastrados na tabela Livros
        return conexao_bd.execute_query_dataframe(self.query_total_livros)["total_LIVROS_registros"].values[0]

    def get_total_emprestimos(self):

        #Cria uma nova conexão com o banco de dados
        conexao_bd: MySQLQueries = MySQLQueries()
        conexao_bd.connect()

        #Retorna a quantidade de registros cadastrados na tabela Emprestimos
        return conexao_bd.execute_query_dataframe(self.query_total_emprestimos)["total_EMPRESTIMOS_registros"].values[0]

    def tela_inicial(self):
        """
        Método tela_inicial - Responsável por construir a tela inicial do sistema com seus dados
        Retorno: A tela inicial do sistema
        """

        return f"""
        ************************************************************
        *               SISTEMA DE BIBLIOTECA ESCOLAR
        *
        *   TOTAL DE REGISTROS:
        *       1 - LIVROS: {self.get_total_livros()}
        *       2 - ALUNOS: {self.get_total_alunos()}
        *       3 - EMPRESTIMOS: {self.get_total_emprestimos()}
        *
        *               INFORMAÇÕES DE CRIAÇÃO DO SISTEMA
        *
        *   CRIADORES: {self.autores[0]};
        *              {self.autores[1]};
        *              {self.autores[2]};
        *              {self.autores[3]}
        *
        *   DISCIPLINA: {self.disciplina}
        *   PROFESSOR: {self.professor}
        *   SEMESTRE: {self.semestre}
        ************************************************************
        """