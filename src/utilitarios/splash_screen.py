from conexao_bd.mySQL_queries import MySQLQueries
from utilitarios import menus

class SplashScreen:
    """
    Classe SplashScreen - Responsável por controlar a tela inicial do sistema, tal como os dados que ela exibe e a sua exibição conforme o fluxo do programa
    """
    def __init__(self):

        #Guarda o nome dos responsáveis pelo projeto em um tributo da classe
        self.autores: str = ["Arthur Salume Sobral", "Eduardo Lopes da Victória Scota Almeida", 
        "Henrique Risciere", "Matheus Amorin Domingues"]

        #Guarda o nome da disciplina do projeto em um tributo da classe
        self.disciplina: str = "Banco de Dados"

        #Guarda o nome do professor da disciplina do projeto em um tributo da classe
        self.professor: str = "Prof. M.Sc. Howard Roatti"

        #Guarda o semestra em que a disciplina está sendo cursada em um tributo da classe
        self.semestre: str = "2024/2"
    
    def get_total_documentos(self, nome_colecao:str) -> int:
        """
        Realiza a chamada do metodo responsavel por contar a quantidade de documentos presentes na colecao passada
        Parametros:
        nome_colecao - Nome da colecao a ser pesquisada a quantidade de documentos
        Retorno: A quantidade de documentos da colecao
        """
        return menus.query_count(nome_colecao)[f"total_documentos_{nome_colecao}"].values[0]

    def tela_inicial(self):
        """
        Método tela_inicial - Responsável por construir a tela inicial do sistema com seus dados
        Retorno: A tela inicial do sistema
        """

        return f"""
        ************************************************************
        *               SISTEMA DE BIBLIOTECA ESCOLAR
        *
        *   TOTAL DE DOCUMENTOS:
        *       1 - LIVROS: {self.get_total_documentos('LIVROS')}
        *       2 - ALUNOS: {self.get_total_documentos("ALUNOS")}
        *       3 - EMPRESTIMOS: {self.get_total_documentos("EMPRESTIMOS")}
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