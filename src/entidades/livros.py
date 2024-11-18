class Livros:
    """Classe 'Livros' - Responsável por representar a colecao 'Livros' e seus campos, contendo métodos para editar e retorná-los"""
    def __init__(self, id:int, nome_obra:str, autor:str, editora_edicao:str, numero_edicao:int,ano_edicao:int, quantidade_exemplares:int):
        self.id = id
        self.nome_obra = nome_obra
        self.autor = autor
        self.editora_edicao = editora_edicao
        self.numero_edicao = numero_edicao
        self.ano_edicao = ano_edicao
        self.quantidade_exemplares = quantidade_exemplares

    def get_id(self) -> int:
        return self.id 
    
    def set_id(self, id:int):
        self.id = id

    def get_nome_obra(self) -> str:
        return self.nome_obra
    
    def set_nome_obra(self, nome_obra:str):
        self.nome_obra = nome_obra

    def get_autor(self) -> str:
        return self.autor
    
    def set_autor(self, autor:str):
        self.autor = autor

    def get_editora_edicao(self) -> str:
        return self.editora_edicao
    
    def set_editora_edicao(self, editora_edicao:str):
        self.editora_edicao = editora_edicao

    def get_numero_edicao(self) -> int:
        return self.numero_edicao
    
    def set_numero_edicao(self, numero_edicao:int):
        self.numero_edicao = numero_edicao
    
    def get_ano_edicao(self) -> int:
        return self.ano_edicao
    
    def set_ano_edicao(self, ano_edicao:int):
        self.ano_edicao = ano_edicao

    def get_quantidade_exemplares(self) -> int:
        return self.quantidade_exemplares
    
    def set_quantidade_exemplares(self, quantidade_exemplares:int):
        self.quantidade_exemplares = quantidade_exemplares

    def __str__(self):
        return (f"Id Obra: {self.get_id()} - Título Obra: {self.get_nome_obra()} - Autor Obra: {self.get_autor()}\n" 
        + f"Editora da Edição: {self.get_editora_edicao()} - Número da Edição: {self.get_numero_edicao()} - Ano da Edição: {self.get_ano_edicao()}\n" 
        + f"Quantidade Total de Exemplares: {self.get_quantidade_exemplares()}")