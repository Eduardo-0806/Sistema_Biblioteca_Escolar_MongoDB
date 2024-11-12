from conexao_bd.mySQL_queries import MySQLQueries

class Relatorio:
    """Classe Relatorio - Responsável por controla a leitura dos arquivos contendo o código SQL e exibição dos relatórios produzido pelo código"""

    def __init__(self):

        #Abre o arquivo contendo o código SQL para gerar o relatório de alunos cadastrados e guarda em um atributo da classe
        with open("sql_relatorios/relatorio_de_alunos_cadastrados.sql") as f:
            self.relatorio_alunos_cadastrados = f.read()
        
        #Abre o arquivo contendo o código SQL para gerar o relatório de alunos devedores e guarda em um atributo da classe
        with open("sql_relatorios/relatorio_alunos_devedores.sql") as f:
            self.relatorio_alunos_devedores = f.read()

        #Abre o arquivo contendo o código SQL para gerar o relatório da quantidade de emprestimos por alunos e guarda em um atributo da classe
        with open("sql_relatorios/relatorio_alunos_quantidade_emprestimos.sql") as f:
            self.relatorio_alunos_quantidade_emprestimos = f.read()

        #Abre o arquivo contendo o código SQL para gerar o relatório de livros no acervo e guarda em um atributo da classe
        with open("sql_relatorios/relatorio_de_livros_acervos.sql") as f:
            self.relatorio_de_livros_acervos = f.read()

        #Abre o arquivo contendo o código SQL para gerar o relatório do estoque de livros emprestados e guarda em um atributo da classe
        with open("sql_relatorios/relatorio_de_estoque_livros_emprestados.sql") as f:
            self.relatorio_de_estoque_livros = f.read()
        
        #Abre o arquivo contendo o código SQL para gerar o relatório de emprestimos cadastrados e guarda em um atributo da classe
        with open("sql_relatorios/relatorio_de_emprestimos_cadastrados.sql") as f:
            self.relatorio_de_emprestimo_cadastrados = f.read()
        
        #Abre o arquivo contendo o código SQL para gerar o relatório de emprestimos atrasados e guarda em um atributo da classe
        with open("sql_relatorios/relatorio_de_emprestimos_atrasados.sql") as f:
            self.relatorio_de_emprestimos_atrasados = f.read()

    def get_relatorio_alunos_cadastrados(self):
        """Método get_relatorio_alunos_cadastrados - Responsável por converter o código SQL do relatório de Alunos Cadastrados em um arquivo DataFrame e exibir na tela"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MySQLQueries = MySQLQueries()
        conexao_relatorio.connect()

        #Tranforma os dados do Código SQL em um DataFrame e exibe na tela
        print(conexao_relatorio.execute_query_dataframe(self.relatorio_alunos_cadastrados))
        input("Pressione ENTER para poder sair")
    
    def get_relatorio_alunos_devedores(self):
        """Método get_relatorio_alunos_devedores - Responsável por converter o código SQL do relatório de alunos devedores em um arquivo DataFrame e exibir na tela"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MySQLQueries = MySQLQueries()
        conexao_relatorio.connect()

        #Tranforma os dados do Código SQL em um DataFrame e exibe na tela
        print(conexao_relatorio.execute_query_dataframe(self.relatorio_alunos_devedores))
        input("Pressione ENTER para poder sair")

    def get_relatorio_alunos_quantidade_emprestimos(self):
        """Método get_relatorio_alunos_quantidade_emprestimos - Responsável por converter o código SQL do relatório de quantidade de emprestimos por aluno em um arquivo DataFrame e exibir na tela"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MySQLQueries = MySQLQueries()
        conexao_relatorio.connect()

        #Tranforma os dados do Código SQL em um DataFrame e exibe na tela
        print(conexao_relatorio.execute_query_dataframe(self.relatorio_alunos_quantidade_emprestimos))
        input("Pressione ENTER para poder sair")

    def get_relatorio_de_livros_acervos(self):
        """Método get_relatorio_livros_acervos - Responsável por converter o código SQL do relatório de livros no acervo em um arquivo DataFrame e exibir na tela"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MySQLQueries = MySQLQueries()
        conexao_relatorio.connect()

        #Tranforma os dados do Código SQL em um DataFrame e exibe na tela
        print(conexao_relatorio.execute_query_dataframe(self.relatorio_de_livros_acervos))
        input("Pressione ENTER para poder sair")

    def get_relatorio_de_estoque_livros(self):
        """Método get_relatorio_de_estoque_livros - Responsável por converter o código SQL do relatório de estoque de livros emprestados no acervo em um arquivo DataFrame e exibir na tela"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MySQLQueries = MySQLQueries()
        conexao_relatorio.connect()

        #Tranforma os dados do Código SQL em um DataFrame e exibe na tela
        print(conexao_relatorio.execute_query_dataframe(self.relatorio_de_estoque_livros))
        input("Pressione ENTER para poder sair")

    def get_relatorio_de_emprestimo_cadastrados(self):
        """Método get_relatorio_de_emprestimo_cadastrados - Responsável por converter o código SQL do relatório de emprestimos cadastrados em um arquivo DataFrame e exibir na tela"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MySQLQueries = MySQLQueries()
        conexao_relatorio.connect()

        #Tranforma os dados do Código SQL em um DataFrame e exibe na tela
        print(conexao_relatorio.execute_query_dataframe(self.relatorio_de_emprestimo_cadastrados))
        input("Pressione ENTER para poder sair")
    
    def get_relatorio_de_emprestimos_atrasados(self):
        """Método get_relatorio_de_emprestimos_atrasados - Responsável por converter o código SQL do relatório de emprestimos atrasados em um arquivo DataFrame e exibir na tela"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MySQLQueries = MySQLQueries()
        conexao_relatorio.connect()

        #Tranforma os dados do Código SQL em um DataFrame e exibe na tela
        print(conexao_relatorio.execute_query_dataframe(self.relatorio_de_emprestimos_atrasados))
        input("Pressione ENTER para poder sair")