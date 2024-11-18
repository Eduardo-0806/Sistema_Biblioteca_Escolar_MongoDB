class Alunos:
    """Classe 'Alunos' - Responsável por representar a colecao 'Alunos' e seus campos, contendo métodos para editar e retorná-los"""
    def __init__(self, matricula:str, nome:str, email:str):
        self.matricula = matricula
        self.nome = nome
        self.email = email
    
    def get_matricula (self) -> int:
        return self.matricula
    
    def set_matricula(self, matricula: int):
        self.matricula = matricula
    
    def get_nome (self) -> str:
        return self.nome
    
    def set_nome(self, nome: str):
        self.nome = nome
    
    def get_email (self) -> str:
        return self.email
    
    def set_email(self, email: str):
        self.email = email

    def __str__(self):
        return f"Nome: {self.get_nome()} - Matricula: {self.get_matricula()} - Email: {self.get_email()}"