from relatorio.relatorio import Relatorio
from utilitarios.splash_screen import SplashScreen
from utilitarios import menus
from controle.controle_alunos import ControleAlunos
from controle.controle_emprestimos import ControleEmprestimos
from controle.controle_livros import ControleLivros

#Cria variáveis para armazenar classes/módulos necessários para funcionamento do projeto
gerador_relatorio = Relatorio()
tela_inicial = SplashScreen()
controlador_aluno = ControleAlunos()
controlador_emprestimo = ControleEmprestimos()
controlador_livro = ControleLivros()


def exibir_relatorio(opcao_relatorio: int = 0):
    """
    Função exibir_relatorio - Responsável por controlar a exibição dos relatórios conforme a opção escolhida pelo usuário
    Parâmetros:
    opcao_relatorio - Opção de relatório escolhida pelo usuário
    """

    #Relatório de Livros no Acervo
    if opcao_relatorio == 1:
        gerador_relatorio.get_relatorio_de_livros_acervos()
    
    #Relatório de Estoque de Livros Emprestados
    elif opcao_relatorio == 2:
        gerador_relatorio.get_relatorio_de_estoque_livros()

    #Relatório de Alunos Cadastrados
    elif opcao_relatorio == 3:
        gerador_relatorio.get_relatorio_alunos_cadastrados()

    #Relatório de Alunos Devedores
    elif opcao_relatorio == 4:
        gerador_relatorio.get_relatorio_alunos_devedores()

    #Relatório de Quantidade Emprestimos por Aluno
    elif opcao_relatorio == 5:
        gerador_relatorio.get_relatorio_alunos_quantidade_emprestimos()

    #Relatório de Emprestimos Cadastrados
    elif opcao_relatorio == 6:
        gerador_relatorio.get_relatorio_de_emprestimo_cadastrados()

    #Relatório de Emprestimos Atrasados
    elif opcao_relatorio == 7:
        gerador_relatorio.get_relatorio_de_emprestimos_atrasados()

    #Caso seja passada uma opção que não existe
    else:
        print("Opção digitada não é válida")

def inserir_documento(opcao_inserir: int = 0):
    """
    Função inserir_documento - Responsável por controlar a inserção de documentos conforme a opção escolhida 
    pelo usuário
    Parâmetros:
    opcao_inserir - Opção de inserção escolhida pelo usuário
    """

    #Insercao de documento na colecao Alunos
    if opcao_inserir == 1:
        controlador_aluno.cadastrar_aluno()

    #Insercao de documento na colecao Livros
    elif opcao_inserir == 2:
        controlador_livro.cadastrar_livro()

    #Insercao de documento na colecao Emprestimos
    elif opcao_inserir == 3:
        controlador_emprestimo.cadastrar_emprestimo()

    #Caso seja passada uma opção que não existe
    else:
        print("Opção digitada não é válida")

def alterar_documento(opcao_alterar: int = 0):
    """
    Função alterar_documento - Responsável por controlar a alteração de documentos conforme a opção escolhida pelo usuário
    Parâmetros:
    opcao_alterar - Opção de alteração escolhida pelo usuário
    """

    #Alteracao de documento na colecao Alunos
    if opcao_alterar == 1:
        controlador_aluno.alterar_aluno()
    
    #Alteracao de documento na colecao Livros
    elif opcao_alterar == 2:
        controlador_livro.alterar_livro()

    #Alteracao de documento na colecao Emprestimos
    elif opcao_alterar == 3:
        controlador_emprestimo.alterar_emprestimo()

    #Caso seja passada uma opção que não existe
    else:
        print("Opção digitada não é válida")

def excluir_documento(opcao_excluir: int = 0):
    """
    Função excluir_documento - Responsável por controlar a exclusão de documentos conforme a opção escolhida 
    pelo usuário
    Parâmetros:
    opcao_excluir - Opção de exclusão escolhida pelo usuário
    """

    #Exclusão de documento na colecao Alunos
    if opcao_excluir == 1:
        controlador_aluno.excluir_aluno()

    #Exclusão de documento na colecao Livros
    elif opcao_excluir == 2:
        controlador_livro.excluir_livro()
    
    #Exclusão de documento na colecao Emprestimos
    elif opcao_excluir == 3:
        controlador_emprestimo.excluir_emprestimo()

    else:
        print("Opção digitada não é válida")
    
def run():
    """
    função run - Responsável por executar todo o algoritmo para funcionamento do projeto
    """

    #Exibe a tela inicial
    print(tela_inicial.tela_inicial())
    menus.limpar_console()
    opcao_menu_principal: int = 0

    #Entra no menu de operação
    while (opcao_menu_principal!= 5):

        #Exibe o menu principal
        print(menus.MENU_PRINCIPAL)

        #Solicita ao usuário a operação desejada do menu principal 
        opcao_menu_principal_teste: str =input("Digite o número da operação desejada:")

        #Guarante que a resposta do usuário seja um número
        while not opcao_menu_principal_teste.isdecimal():
            print("Erro na opção escolhida!")
            opcao_menu_principal_teste = input("Digite uma opção válida(Somente números): ")
        
        #Guarda a opção em uma variável int após garantir que não haverá problema na conversão de tipo
        opcao_menu_principal = int(opcao_menu_principal_teste)
        menus.limpar_console(1)

        #Inserir documento
        if opcao_menu_principal == 1:
            continuar: str = "S"

            #Garante o usuário estará no menu inserção de documentos até escolher a opção de sair
            while (continuar == "S"):

                #Exibe o menu de entidades
                print(menus.MENU_ENTIDADES)

                #Solicita ao usuário a opção de entidade
                opcao_inserir_teste = input("Digite a opção de colecao para inserir um documento: ")
                
                #Garante que o valor passado seja um número
                while (not opcao_inserir_teste.isdecimal()):
                    print("Erro na opção escolhida!")
                    opcao_inserir_teste = input("Digite uma opção válida(Somente números): ")
                
                #Guarda a opção em uma variável int após garantir que não haverá problema na conversão de tipo
                opcao_inserir: str = int(opcao_inserir_teste)
                menus.limpar_console(1)

                #Tenta realizar o processo de inserção de documento na colecao desejada
                inserir_documento(opcao_inserir)
                menus.limpar_console(2)

                #Exibe a tela inicial após a operação realizada
                print(tela_inicial.tela_inicial())
                menus.limpar_console(2)

                #Solicita ao usuário se deseja continuar inserindo documento
                continuar = input("Deseja continuar criando registros(S/N)? ").upper()

                #Garante que a resposta esteja dentro dos valores esperados
                while(continuar != "S" and continuar != "N"):
                    continuar = input("Digite uma resposta válida(S ou N): ").upper()

                #Informa ao usuário da sáida do menu, caso não deseje continuar
                if (continuar == "N"):
                    print("Saindo do menu de inserção")
                menus.limpar_console(1)
        
        #Alterar documento
        elif opcao_menu_principal == 2:
            continuar: str = "S"

            #Garante o usuário estará no menu de alteração de documento até escolher a opção de sair
            while (continuar == "S"):

                #Exibe o menu de entidades
                print(menus.MENU_ENTIDADES)

                #Solicita ao usuário a opção de entidade
                opcao_atualizar_teste = input("Digite a opção de colecao para atualizar um documento: ")
                
                #Garante que o valor passado seja um número
                while (not opcao_atualizar_teste.isdecimal()):
                    print("Erro na opção escolhida!")
                    opcao_atualizar_teste = input("Digite uma opção válida(Somente números): ")
                
                #Guarda a opção em uma variável int após garantir que não haverá problema na conversão de tipo
                opcao_atualizar: int = int(opcao_atualizar_teste)
                menus.limpar_console(1)

                #Tenta realizar o processo de alteração de documento na colecao desejada
                alterar_documento(opcao_atualizar)
                menus.limpar_console(2)

                #Exibe a tela inicial após a operação realizada
                print(tela_inicial.tela_inicial())
                menus.limpar_console(2)

                #Solicita ao usuário se deseja continuar atualizando documentos
                continuar = input("Deseja continuar atualizando docmentos(S/N)? ").upper()

                #Garante que a resposta esteja dentro dos valores esperados
                while(continuar != "S" and continuar != "N"):
                    continuar = input("Digite uma resposta válida(S ou N): ").upper()

                #Informa ao usuário da sáida do menu, caso não deseje continuar
                if (continuar == "N"):
                    print("Saindo do menu de atualização")
                menus.limpar_console(1)

        #Excluir documento
        elif opcao_menu_principal == 3:
            continuar: str = "S"

            #Garante o usuário estará no menu de exclusão de documentos até escolher a opção de sair
            while (continuar == "S"):

                #Exibe o menu de entidades
                print(menus.MENU_ENTIDADES)

                #Solicita ao usuário a opção de entidade
                opcao_excluir_teste = input("Digite a opção de colecao para excluir um documentos: ")
                
                #Garante que o valor passado seja um número
                while (not opcao_excluir_teste.isdecimal()):
                    print("Erro na opção escolhida!")
                    opcao_excluir_teste = input("Digite uma opção válida(Somente números): ")
                
                #Guarda a opção em uma variável int após garantir que não haverá problema na conversão de tipo
                opcao_excluir: int = int(opcao_excluir_teste)
                menus.limpar_console(1)

                #Tenta realizar o processo de exclusão de documento na colecao desejada
                excluir_documento(opcao_excluir)
                menus.limpar_console(2)

                #Exibe a tela inicial após a operação realizada
                print(tela_inicial.tela_inicial())
                menus.limpar_console(2)

                continuar = input("Deseja continuar excluindo documentos(S/N)? ").upper()
                while(continuar != "S" and continuar != "N"):
                    continuar = input("Digite uma resposta válida(S ou N): ").upper()

                if (continuar == "N"):
                    print("Saindo do menu de Exclusão")

                menus.limpar_console(1)
            
            
        
        #Exibir relatórios
        elif opcao_menu_principal == 4:
            continuar: str = "S"

            #Garante o usuário estará no menu de relatórios até escolher a opção de sair
            while (continuar == "S"):

                #Exibe o menu de relatórios
                print(menus.MENU_RELATORIOS)

                #Solicita ao usuário a opção de relatório
                opcao_relatorio_teste = input("Digite a opção de relatorio para ser exibido: ")
                
                #Garante que o valor passado seja um número
                while (not opcao_relatorio_teste.isdecimal()):
                    print("Erro na opção escolhida!")
                    opcao_relatorio_teste = input("Digite uma opção válida(Somente números): ")
                
                #Guarda a opção em uma variável int após garantir que não haverá problema na conversão de tipo
                opcao_relatorio: int = int(opcao_relatorio_teste)
                menus.limpar_console(1)

                #Tenta realizar o processo de exibição do relatório desejado
                exibir_relatorio(opcao_relatorio)
                menus.limpar_console(1)

                continuar = input("Deseja exibir outro relatório(S/N)? ").upper()
                while(continuar != "S" and continuar != "N"):
                    continuar = input("Digite uma resposta válida(S ou N): ").upper()

                if (continuar == "N"):
                    print("Saindo do menu de relatórios")

                menus.limpar_console(1)

        #Sair do Sistema
        elif opcao_menu_principal == 5:
            print("Obrigado por utilizar o sistema")
            menus.limpar_console(2)
        
        #Caso seja passado uma opção não disponível
        else:
            print("Opção digitada não está disponível")
            menus.limpar_console(2)

if __name__ == '__main__':
    run()
                


