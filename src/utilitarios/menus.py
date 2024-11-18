#Constante responsável por armezar o menu_principal do sistema, contendo as operações possíveis
MENU_PRINCIPAL = """Menu Principal
1 - Inserir Documentos
2 - Atualizar Documentos
3 - Deletar Documentos
4 - Gerar Relatórios
5 - Sair"""

#Constante responsável por armazenar a lista de entidades/colecoes do banco de dados
MENU_ENTIDADES = """Entidades
1 - Alunos
2 - Livros
3 - Emprestimos"""

#Constante responsável por armazenar as opções de relatórios possíveis
MENU_RELATORIOS = """Relatórios
1 - Relatório de Livros No Arcevo
2 - Relatório de Controle de Estoque de Livros Emprestados
3 - Relatório de Alunos Cadastrados
4 - Relatório de Alunos Devedores
5 - Relatório de Empréstimos por Aluno
6 - Relatório de Emprestimos
7 - Relatórios de Emprestimos Atrasados"""

def query_count(nome_colecao:str):
    """
    Funcao query_count - Realiza a contagem de documentos do nome da colecao passada na chamada da funcao
    Parametros:
    nome_colecao = Nome da colecao a ser verificada a quantidade de documentos
    Retorno: Dataframe Pandas contendo a quantidade de documentos da colecao
    """
    import pandas as pd
    from conexao_bd.mongoDB_queries import MongoDBQueries

    #Realiza a conexao ao banco de dados mongoDB
    conexao_contagem:MongoDBQueries = MongoDBQueries()
    conexao_contagem.connect()

    #Guarda em uma variavel resultado da contagem dos documentos da colecao passada
    total_documentos: int = conexao_contagem.db[nome_colecao].count_documents({})

    #Armaeza a variavel em um DataFrame da biblioteca Pandas
    df_resultado: pd.DataFrame = pd.DataFrame({f"total_documentos_{nome_colecao}": [total_documentos]})

    #Retorna o DataFrame
    return df_resultado

def limpar_console(tempo_pausa: int = 3):
    """
    Função limpar_console - Responsável por limpar a tela do terminal após um determinado tempo determinado na chamada da função
    Parâmetros:
    tempo_pausa = O tempo, em segundos, que será esperado, após a chamada da função, para realizar a limpeza da tela, por padrão será esperado 3 segundos
    """
    import os
    from time import sleep
    sleep(tempo_pausa)
    os.system('clear')