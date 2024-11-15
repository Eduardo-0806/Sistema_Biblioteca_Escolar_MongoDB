from conexao_bd.mongoDB_queries import MongoDBQueries
from datetime import datetime
import pandas as pd

class Relatorio:
    """Classe Relatorio - Responsável por realizar a construcao dos relatorios desejados"""

    def __init__(self):
        pass

    def get_relatorio_alunos_cadastrados(self):
        """Método get_relatorio_alunos_cadastrados - Responsável por realizar a consulta ao banco de dados e gerar o relatorio de alunos cadastrados"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MongoDBQueries = MongoDBQueries()
        conexao_relatorio.connect()

        #Realiza a consulta no banco de dados e guarda seu resultado num DataFrame Pandas
        df_relatorio = pd.DataFrame(conexao_relatorio.db["ALUNOS"].find({},{"Matricula do Aluno": "$matricula", 
        "Nome Aluno": "$nome", "Email Aluno":"$email", "_id": 0}).sort({"nome": 1}))

        #Exibe o DataFrame para o usuario
        print(df_relatorio)
        input("Pressione ENTER para poder sair")
    
    def get_relatorio_alunos_devedores(self):
        """Método get_relatorio_alunos_devedores - Responsável por realizar a consulta ao banco de dados e gerar o relatorio de alunos devedores"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MongoDBQueries = MongoDBQueries()
        conexao_relatorio.connect()

        #Realiza a pesquisa no banco de dados e guarda o resultado em um DataFrame
        df_relatorio: pd.DataFrame = pd.DataFrame(conexao_relatorio.db["EMPRESTIMOS"].aggregate([
    {
        '$addFields': {
            'date': {
                '$dateFromString': {
                    'dateString': '$data_devolucao'
                }
            }
        }
    }, {
        '$match': {
            'date': {
                '$lt': datetime.utcnow()
            }
        }
    }, {
        '$group': {
            '_id': '$codigo_aluno', 
            'quantidade_elemento': {
                '$sum': 1
            }, 
            'valor_multa': {
                '$sum': {
                    '$multiply': [
                        {
                            '$dateDiff': {
                                'startDate': '$date', 
                                'endDate': datetime.utcnow(), 
                                'unit': 'day'
                            }
                        }, 1.5
                    ]
                }
            }
        }
    }, {
        '$project': {
            'codigo_aluno': '$_id', 
            'quantidade_elemento': 1, 
            'valor_multa': 1, 
            '_id': 0
        }
    }, {
        '$lookup': {
            'from': 'ALUNOS', 
            'localField': 'codigo_aluno', 
            'foreignField': 'matricula', 
            'as': 'aluno'
        }
    }, {
        '$unwind': {
            'path': '$aluno'
        }
    }, {
        '$project': {
            'Matricula Aluno': '$codigo_aluno', 
            'Nome Aluno': '$aluno.nome', 
            'Email Aluno': '$aluno.email', 
            'Quantidade Livros Atrasados': '$quantidade_elemento', 
            'Valor Total Multa(R$)': '$valor_multa'
        }
    }, {
        '$sort': {
            'Nome Aluno': 1
        }
    }
]))
        #Exibe DataFrame para o usuario
        print(df_relatorio)
        input("Pressione ENTER para poder sair")

    def get_relatorio_alunos_quantidade_emprestimos(self):
        """Método get_relatorio_alunos_quantidade_emprestimos - Responsável por realizar a consulta ao banco de dados e gerar o relatorio da quantidade emprestimos por aluno"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MongoDBQueries = MongoDBQueries()
        conexao_relatorio.connect()

        #Realiza a pesquisa no banco de Dados e salva o resultado em um DataFrame
        df_relatorio: pd.DataFrame = pd.DataFrame(conexao_relatorio.db["EMPRESTIMOS"].aggregate([
    {
        '$group': {
            '_id': '$codigo_aluno', 
            'qtd_emprestimos': {
                '$sum': 1
            }
        }
    }, {
        '$project': {
            'matricula': '$_id', 
            'qtd_emprestimos': 1, 
            '_id': 0
        }
    }, {
        '$lookup': {
            'from': 'ALUNOS', 
            'localField': 'matricula', 
            'foreignField': 'matricula', 
            'as': 'aluno'
        }
    }, {
        '$unwind': {
            'path': '$aluno'
        }
    }, {
        '$project': {
            'Matricula Aluno': '$matricula', 
            'Nome Aluno': '$aluno.nome', 
            'Quantidade Emprestimos': '$qtd_emprestimos'
        }
    }, {
        '$sort': {
            'Quantidade Emprestimos': -1
        }
    }
]))

        #Exibe o DataFrame para o usuario
        print(df_relatorio)
        
        input("Pressione ENTER para poder sair")

    def get_relatorio_de_livros_acervos(self):
        """Método get_relatorio_livros_acervos - Responsavel por realizar a consulta ao banco de dados e gerar o relatorio de livros no acervo"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MongoDBQueries = MongoDBQueries()
        conexao_relatorio.connect()

        #Realiza a pesquisa no banco de dados e salva o resultado em um DataFrame
        df_relatorio: pd.DataFrame = pd.DataFrame(conexao_relatorio.db["LIVROS"].find({}, {"ID": "$id",
        "Nome da Obra": "$nome_obra", "Autor da Obra": "$autor", "Editora da Edicao": "$editora_edicao",
        "Numero da Edicao":"$numero_edicao", "Ano da Edicao": "$ano_edicao", 
        "Quantidade de Exemplares":"$quantidade_exemplares","_id": 0}).sort({"nome_obra": 1, "autor": 1}))
        
        #Exibe o DataFrame para o usuario
        print(df_relatorio)
        input("Pressione ENTER para poder sair")

    def get_relatorio_de_estoque_livros(self):
        """Método get_relatorio_de_estoque_livros - Responsavel por realizar a consulta ao banco de dados e gerar o relatorio do estoque de livros emprestados"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MongoDBQueries = MongoDBQueries()
        conexao_relatorio.connect()

        #Realiza a pesquisa no banco de dados e guarda o resultado em um DataFrame
        df_relatorio: pd.DataFrame = pd.DataFrame(conexao_relatorio.db["EMPRESTIMOS"].aggregate([
    {
        '$group': {
            '_id': '$codigo_livro', 
            'qtd_emprestada': {
                '$sum': 1
            }
        }
    }, {
        '$project': {
            'codigo_livro': '$_id', 
            'qtd_emprestada': 1, 
            '_id': 0
        }
    }, {
        '$lookup': {
            'from': 'LIVROS', 
            'localField': 'codigo_livro', 
            'foreignField': 'id', 
            'as': 'livro'
        }
    }, {
        '$unwind': {
            'path': '$livro'
        }
    }, {
        '$project': {
            'codigo_livro': 1, 
            'nome_obra': '$livro.nome_obra', 
            'autor_obra': '$livro.autor', 
            'editora_edicao': '$livro.editora_edicao', 
            'numero_edicao': '$livro.numero_edicao', 
            'quantidade_exemplares': '$livro.quantidade_exemplares', 
            'qtd_emprestada': 1
        }
    }, {
        '$addFields': {
            'quantidade_disponivel': {
                '$subtract': [
                    '$quantidade_exemplares', '$qtd_emprestada'
                ]
            }
        }
    }, {
        '$project': {
            'ID': '$codigo_livro', 
            'Nome da Obra': '$nome_obra', 
            'Autor da Obra': '$autor_obra', 
            'Editora da Edicao': '$editora_edicao', 
            'Numero da Edicao': '$numero_edicao', 
            'Quantidade Total': '$quantidade_exemplares', 
            'Quantidade Emprestada': '$qtd_emprestada', 
            'Quantidade Disponivel': '$quantidade_disponivel'
        }
    }, {
        '$sort': {
            'Nome da Obra': 1, 
            'Autor da Obra': 1
        }
    }
]))

        #Exibe para o usuario o DataFrame
        print(df_relatorio)
        input("Pressione ENTER para poder sair")

    def get_relatorio_de_emprestimo_cadastrados(self):
        """Método get_relatorio_de_emprestimo_cadastrados - Responsavel por realizar a consulta ao banco de dados e gerar o relatorio de emprestimos cadastrados"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MongoDBQueries = MongoDBQueries()
        conexao_relatorio.connect()

        #Realiza a pesquisa no banco de dados e guarda o resultado em um DataFrame
        df_relatorio: pd.DataFrame = pd.DataFrame(conexao_relatorio.db["EMPRESTIMOS"].aggregate([
    {
        '$lookup': {
            'from': 'ALUNOS', 
            'localField': 'codigo_aluno', 
            'foreignField': 'matricula', 
            'as': 'aluno'
        }
    }, {
        '$unwind': {
            'path': '$aluno'
        }
    }, {
        '$project': {
            'codigo': 1, 
            'codigo_livro': 1, 
            'codigo_aluno': 1, 
            'nome_aluno': '$aluno.nome', 
            'email_aluno': '$aluno.email', 
            'data_devolucao': 1
        }
    }, {
        '$lookup': {
            'from': 'LIVROS', 
            'localField': 'codigo_livro', 
            'foreignField': 'id', 
            'as': 'livro'
        }
    }, {
        '$unwind': {
            'path': '$livro'
        }
    }, {
        '$project': {
            'Codigo Emprestimo': '$codigo', 
            'ID Livro': '$codigo_livro', 
            'Nome da Obra': '$livro.nome_obra', 
            'Editora da Edicao': '$livro.editora_edicao', 
            'Numero da Edicao': '$livro.numero_edicao', 
            'Matricula Aluno': '$codigo_aluno', 
            'Nome Aluno': '$nome_aluno', 
            'Email do Aluno': '$email_aluno', 
            'Data de Devolucao': '$data_devolucao',
            '_id': 0
        }
    }, {
        '$sort': {
            'Codigo Emprestimo': 1
        }
    }
]))

        #Exibe o DataFrame para o usuario
        print(df_relatorio)
        input("Pressione ENTER para poder sair")
    
    def get_relatorio_de_emprestimos_atrasados(self):
        """Método get_relatorio_de_emprestimos_atrasados - Responsavel por realizar a consulta ao banco de dados e gerar o relatorio de emprestimos atrasados"""

        #Cria uma nova conexão com o banco de dados
        conexao_relatorio: MongoDBQueries = MongoDBQueries()
        conexao_relatorio.connect()

        #Realiza a pesquisa no banco de dados e guarda o resultado no DataFrame
        df_relatorio: pd.DataFrame = pd.DataFrame(conexao_relatorio.db["EMPRESTIMOS"].aggregate([
    {
        '$addFields': {
            'date': {
                '$dateFromString': {
                    'dateString': '$data_devolucao'
                }
            }
        }
    }, {
        '$match': {
            'date': {
                '$lt': datetime.utcnow()
            }
        }
    }, {
        '$lookup': {
            'from': 'ALUNOS', 
            'localField': 'codigo_aluno', 
            'foreignField': 'matricula', 
            'as': 'aluno'
        }
    }, {
        '$unwind': {
            'path': '$aluno'
        }
    }, {
        '$project': {
            '_id': 0, 
            'codigo': 1, 
            'codigo_livro': 1, 
            'codigo_aluno': 1, 
            'nome': '$aluno.nome', 
            'email': '$aluno.email', 
            'data_devolucao': 1, 
            'date': 1
        }
    }, {
        '$lookup': {
            'from': 'LIVROS', 
            'localField': 'codigo_livro', 
            'foreignField': 'id', 
            'as': 'livro'
        }
    }, {
        '$unwind': {
            'path': '$livro'
        }
    }, {
        '$project': {
            'codigo': 1, 
            'codigo_livro': 1, 
            'nome_obra': '$livro.nome_obra', 
            'codigo_aluno': 1, 
            'nome': 1, 
            'email': 1, 
            'data_devolucao': 1, 
            'date': 1
        }
    }, {
        '$addFields': {
            'diferenca_dias': {
                '$dateDiff': {
                    'startDate': '$date', 
                    'endDate': datetime.utcnow(), 
                    'unit': 'day'
                }
            }
        }
    }, {
        '$project': {
            'codigo': 1, 
            'codigo_livro': 1, 
            'nome_obra': 1, 
            'codigo_aluno': 1, 
            'nome': 1, 
            'email': 1, 
            'data_devolucao': 1, 
            'diferenca_dias': 1
        }
    }, {
        '$addFields': {
            'valor_multa': {
                '$multiply': [
                    '$diferenca_dias', 1.5
                ]
            }
        }
    }, {
        '$project': {
            'Codigo Emprestimo': '$codigo', 
            'ID Livro': '$codigo_livro', 
            'Nome Obra': '$nome_obra', 
            'Codigo Aluno': '$codigo_aluno', 
            'Nome Aluno': '$nome', 
            'Email Aluno': '$email', 
            'Data de Devolucao': '$data_devolucao', 
            'Valor Multa(R$1,50 por dia)': '$valor_multa'
        }
    }, {
        '$sort': {
            'Codigo Emprestimo': 1
        }
    }
]))

        #Exibe o DataFrame para o usuario
        print(df_relatorio)
        input("Pressione ENTER para poder sair")