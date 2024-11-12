#Constante responsável por armezar o menu_principal do sistema, contendo as operações possíveis
MENU_PRINCIPAL = """Menu Principal
1 - Inserir Registros
2 - Atualizar Registros
3 - Deletar Registros
4 - Gerar Relatórios
5 - Sair"""

#Constante responsável por armazenar a lista de entidades/tabelas do banco de dados
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

#Constante responsável por armazenar o molde da consulta de contagem de registro de uma tabela
QUERY_COUNT = 'select count(1) as total_{tabela}_registros from {tabela}'

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