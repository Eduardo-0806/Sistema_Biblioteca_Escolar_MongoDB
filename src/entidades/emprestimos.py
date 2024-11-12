from entidades.alunos import Alunos
from entidades.livros import Livros
from datetime import date

class Emprestimos:
    """Classe 'Emprestimo' - Responsável por representar a tabela 'Emprestimos' e seus campos, contendo métodos para editar e retorná-los"""
    def __init__(self, codigo:int, livro:Livros, aluno:Alunos, data_devolucao:date):
        self.codigo = codigo
        self.livro = livro
        self.aluno = aluno
        self.data_devolucao = data_devolucao
    
    def get_codigo(self) -> int:
        return self.codigo
    
    def set_codigo(self, codigo:int):
        self.codigo = codigo
    
    def get_livro(self) -> Livros:
        return self.livro
    
    def set_livro(self, livro:Livros):
        self.livro = livro

    def get_aluno(self) -> Alunos:
        return self.aluno
    
    def set_aluno(self, aluno:Alunos):
        self.aluno = aluno
    
    def get_data_devolucao(self) -> date:
        return self.data_devolucao
    
    def set_data_devolucao(self, data_devolucao:date):
        self.data_devolucao = data_devolucao
    
    def __str__(self):
        return f"Código: {self.get_codigo()} - Código Aluno: {self.get_aluno().get_matricula()} - Código Livro: {self.get_livro().get_id()}\nData de Devolução: {self.get_data_devolucao()}"