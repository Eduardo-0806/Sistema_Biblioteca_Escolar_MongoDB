from conexao_bd.mongoDB_queries import MongoDBQueries
from entidades.livros import Livros
import pandas as pd

class ControleLivros:
    """
    Classe 'ControleLivros' - Responsável por controlar as alterações(Inserção, alterção e exclusão de registros) da tabela 'Livros' do sistema por meio de comandos DML
    """
    def __init__(self):
        pass

    def cadastrar_livro(self) -> Livros:
        """
        Método 'cadastrar_livro' - Responsável por realizar o processo de preenchimento dos campos necessários e posteriomente a inserção de um novo documento na colecao 'Livros', valida as respostas do usuário para os campos não serem preenchidos com um valor inválido
        Retorno: Retorna um objeto da classe Livros com os dados do documento cadastrado 
        """
        
        #Cria uma nova conexão
        conexao_inserir = MongoDBQueries()
        conexao_inserir.connect()

        #Solicita ao usuário o id do livro a ser cadastrado
        id_teste: str = input("Insira o id do livro a ser cadastrado: ").strip()

        #Garante que o id passado seja um número
        while not id_teste.isdecimal():
            print("Erro no id digitado")
            id_teste: str = input("Insira outro id para o livro a ser cadastrado(Somente números): ").strip()
        
        #Guarda o id em uma variável int após garantir que não haverá problema na conversão de tipo
        id: int = int(id_teste)

        #Verifica se o id não está cadastrado na tabela 'Livros'
        if(self.pesquisar_id(id)):

            #Solicita ao usuário o nome da obra
            nome_obra: str = input("Digite o nome da obra: ").strip()

            #Garante que o nome não seja vazio
            while (nome_obra == ""):
                print("Erro no nome digitado!")
                nome_obra = input("Digite o nome da obra(Não digite um nome vázio): ").strip()
            
            #Solicita ao usuário o nome do autor da obra
            autor:str = input("Digite o nome do autor da obra: ").strip()

            #Garante que o nome passado não seja vazio
            while (autor == ""):
                print("Erro no nome digitado!")
                autor = input("Digite o nome do autor da obra(Não digite um nome vázio): ").strip()
            
            #Solicita ao usuário a editora da obra
            editora_edicao:str = input("Digite o nome da editora da edição da obra: ").strip()

            #Garante que a editora passada não seja vazia
            while (editora_edicao == ""):
                print("Erro no nome digitado!")
                editora_edicao = input("Digite o nome da editora da edição da obra(Não digite um nome vázio): ").strip()
            
            #Solicita ao usuário o número da edição da obra
            numero_edicao_teste: str = input("Insira o número da edição: ").strip()

            #Garante que o valor passado seja um número
            while not numero_edicao_teste.isdecimal():
                print("Erro no número digitado")
                numero_edicao_teste = input("Insira um número de edição válido: ").strip()

            #Guarda o número em uma variável int após garantir que não haverá problema na conversão de tipo
            numero_edicao = int(numero_edicao_teste)

            #Solicita ao usuário o ano da edição da obra
            ano_edicao_teste:str = input("Digite o ano de lançamento da edição dessa obra(formato YYYY): ").strip()
            
            #Garante que o ano passada seja um número e esteja no formato desejado
            while not ano_edicao_teste.isdecimal()  or (len(ano_edicao_teste) != 4):
                print("Erro no ano passado")
                ano_edicao_teste = input("Digite um ano válido: ").strip()
            
            #Guarda o número em uma variável int após garantir que não haverá problema na conversão de tipo
            ano_edicao:int = int(ano_edicao_teste)

            #Solicita ao usuário a quantidade de exemplares da obra
            quantidade_exemplares_teste: str = input("Insira a quantidade total de exemplares dessa edicao: ").strip()

            #Garante que a quantidade passada seja um número
            while not quantidade_exemplares_teste.isdecimal():
                print("Erro no número digitado")
                quantidade_exemplares_teste = input("Insira um número de exemplares válido: ").strip()

            #Guarda a quantidade em uma variável int após garantir que não haverá problema na conversão de tipo
            quantidade_exemplares = int(quantidade_exemplares_teste)

            #Try-Except para evitar que o ano com valor inválido acabe quebrando o programa
            try:

                #Realiza a inserção do livro na colecao 'Livros' através de código noSQL

                conexao_inserir.db["LIVROS"].insert_one({"id": id, "nome_obra": f"{nome_obra}", "autor":f"{autor}",
                "editora_edicao":f"{editora_edicao}","numero_edicao": numero_edicao, "ano_edicao": ano_edicao,
                "quantidade_exemplares": quantidade_exemplares})

                #Guarda os campos do documento inserido em um DataFrame
                df_resultado = pd.DataFrame(conexao_inserir.db["LIVROS"].find({"id": id}))

                #Cria um objeto da classe Livros para guardar os dados do registro
                livro: Livros = Livros(df_resultado.id.values[0], df_resultado.nome_obra.values[0],
                df_resultado.autor.values[0], df_resultado.editora_edicao.values[0], 
                df_resultado.numero_edicao.values[0], df_resultado.ano_edicao.values[0], 
                df_resultado.quantidade_exemplares.values[0])

                #Informa ao usuário o sucesso da operação e exibe os dados do registro
                print("Livro cadastrado com sucesso")
                print(livro)

                input("Digite Enter para sair")
                
                #Retorna o objeto para uso futuro, se necessário
                return livro

            #Em caso de erro, avisa ao usuário sobre a falha de cadastrar o livro e qual erro ocasionou a falha
            except Exception as e:
                print("Erro ao registrar livro")
                print(e)
                return None
        else:
            print("O id passado já está cadastrado")
            return None
    
    def alterar_livro(self) -> Livros:
        """
        Método 'alterar_livro' - Responsável por realizar o processo de atualização dos dados de um documento da colecao 'Livros', valida as respostas do usuário para os campos não serem preenchidos com um valor inválido
        Retorno: Retorna um objeto da classe Livros com os dados do cadastro atualizado 
        """

        #Cria uma nova conexão
        conexao_atualizacao: MongoDBQueries = MongoDBQueries()
        conexao_atualizacao.connect()

        #Exibe os livros cadastrados na tabela 'Livros'
        print("LIVROS CADASTRADOS")
        print(self.listar_livros())

        #Solicita ao usuário o ID do livro a ser alterado
        id_teste: str = input("Digite o id de um livro cadastrado: ").strip()
        
        #Garante que o ID passado seja um número
        while (not id_teste.isdecimal()):
            print("id não é válido")
            id_teste = input("Digite o id de um livro cadastrado (Somente números): ").strip()

        #Guarda o ID em uma variável int após garantir que não haverá problema na conversão de tipo
        id: int = int(id_teste)

        #Verifica se o ID passado está cadastrado na tabela 'Livros'
        if (not self.pesquisar_id(id)):

            #Solicita ao usuário novo nome da obra
            nome_obra_novo: str = input("Digite o nome da obra (Novo): ").strip()

            #Garante que o nome passado não seja vazio
            while (nome_obra_novo == ""):
                print("Erro no nome digitado!")
                nome_obra_novo = input("Digite o novo nome da obra (Não digite um nome vázio): ").strip()
            
            #Solicita ao usuário o novo nome do autor
            autor_novo:str = input("Digite o nome do autor da obra (novo): ").strip()

            #Garante que o nome passado não seja vazio
            while (autor_novo == ""):
                print("Erro no nome digitado!")
                autor_novo = input("Digite o novo nome do autor da obra(Não digite um nome vázio): ").strip()
            
            #Solicita ao usuário o novo nome da editora da edição
            editora_edicao_nova:str = input("Digite o nome da editora da edição da obra(novo): ").strip()

            #Garante que o nome passado não seja vazio
            while (editora_edicao_nova == ""):
                print("Erro no nome digitado!")
                editora_edicao_nova = input("Digite o novo nome da editora da edição da obra(Não digite um nome vázio): ").strip()
            
            #Solicita ao usuário o novo número da edição
            numero_edicao_novo_teste: str = input("Insira o número da edição(novo): ").strip()

            #Garante que o valor passado seja um número
            while not numero_edicao_novo_teste.isdecimal():
                print("Erro no número digitado")
                numero_edicao_novo_teste = input("Insira um número de edição válido: ").strip()

            #Guarda o numero da edicao em uma variável int após garantir que não haverá problema na conversão de tipo
            numero_edicao_novo = int(numero_edicao_novo_teste)

            #Solicita ao usuário o novo ano da edição
            ano_edicao_novo_teste:str = input("Digite o novo ano de lançamento da edição dessa obra(formato YYYY): ").strip()
            
            #Garante que a data passada seja um número e esteja no formato necessário
            while not ano_edicao_novo_teste.isdecimal()  or (len(ano_edicao_novo_teste) != 4):
                print("Erro no ano passado")
                ano_edicao_novo_teste = input("Digite um ano válido: ").strip()
            
            #Guarda o ano da edicao em uma variável int após garantir que não haverá problema na conversão de tipo
            ano_edicao_novo: int = int(ano_edicao_novo_teste)

            #Solicita ao usuário a nova quantidade de exemplares
            quantidade_exemplares_nova_teste: str = input("Insira a nova quantidade total de exemplares dessa edição: ").strip()

            #Garante que a quantidade passada seja um número
            while not quantidade_exemplares_nova_teste.isdecimal():
                print("Erro no número digitado")
                quantidade_exemplares_nova_teste = input("Insira um número de exemplares válido: ").strip()
            
            #Guarda a quantiade em uma variável int após garantir que não haverá problema na conversão de tipo
            quantidade_exemplares_nova = int(quantidade_exemplares_nova_teste)

            #Try-Except para evitar que o ano com valor inválido acabe quebrando o programa
            try:

                #Realiza a atualização do documento na colecao 'Livros' através de código noSQL
                conexao_atualizacao.db["LIVROS"].update_many({"id": id}, {"$set": {"nome_obra": f"{nome_obra_novo}", 
                "autor":f"{autor_novo}", "editora_edicao":f"{editora_edicao_nova}",
                "numero_edicao": numero_edicao_novo, "ano_edicao": ano_edicao_novo, 
                "quantidade_exemplares": quantidade_exemplares_nova}})

                #Guarda em um DataFrame os campos do documento atualizado
                df_resultado = pd.DataFrame(conexao_atualizacao.db["LIVROS"].find({"id": id}))

                #Cria um objeto da classe Livros para guardar os dados do documento
                livro_novo: Livros = Livros(df_resultado.id.values[0], df_resultado.nome_obra.values[0],
                df_resultado.autor.values[0], df_resultado.editora_edicao.values[0], 
                df_resultado.numero_edicao.values[0], df_resultado.ano_edicao.values[0], 
                df_resultado.quantidade_exemplares.values[0])

                #Informa ao usuário o sucesso da operação, exibindo os dados do documento
                print("Registro de livro alterado com sucesso")
                print(livro_novo)

                input("Digite Enter para sair")

                #Retorna o objeto para qualquer necessidade futura
                return livro_novo

            #Em caso de erro, avisa ao usuário sobre a falha de cadastrar o livro e qual erro ocasionou a falha
            except Exception as e:
                print("Erro ao atualizar registro de livro")
                print(e)
                return None
        else:
            print("O id passado não está cadastrado no sistema")
            return None

    def excluir_livro(self):
        """
        Método 'excluir_livro' - Responsável por realizar o processo de exclusão de um documento da colecao 'Alunos', valida as respostas do usuário para os campos não serem preenchidos com um valor inválido 
        """      

        #Cria uma nova conexão
        conexao_exclusao: MongoDBQueries = MongoDBQueries()
        conexao_exclusao.connect()

        #Exibe os livros cadastrados na tabela 'Alunos'
        print("LIVROS CADASTRADOS")
        print(self.listar_livros())

        #Solicita ao usuário o ID do livro
        id_teste: str = input("Digite o id de um livro cadastrado: ").strip()
        
        #Garante que o ID passado seja um número
        while (not id_teste.isdecimal()):
            print("id não é válido")
            id_teste = input("Digite o id de um livro cadastrado(Somente números): ").strip()

        #Guarda o ID em uma variável int após garantir que não haverá problema na conversão de tipo
        id: int = int(id_teste)

        #Verifica se o ID passado está cadastrado na colecao 'Livros'
        if (not self.pesquisar_id(id)):

            #Guarda em um DataFrame o resultado do método pesquisar_id_emprestimo()
            df_id_emprestimos = self.pesquisar_id_emprestimo(id)

            #Verifica se o ID passado está presente em algum emprestimo da colecao 'Emprestimos'
            if (len(df_id_emprestimos.index) > 0):

                #Se estiver presente, impede a exclusão do mesmo e mostra ao usuário em quais emprestimos ele participa
                print("o id passado está presente nos seguintes registros de empréstimos:")
                print(df_id_emprestimos)
                print("Apague ou modifique esses registros para poder excluir esse id")
                input("Digite ENTER para sair:")
            else:

                #Guarda em um DataFrame os campos do registro a ser excluído
                df_id_excluido = pd.DataFrame(conexao_exclusao.db["LIVROS"].find({"id": id}))

                #Cria um objeto da classe Livros para guardar os dados do registro a ser excluído
                livro_excluido: Livros = Livros(df_id_excluido.id.values[0], df_id_excluido.nome_obra.values[0],
                df_id_excluido.autor.values[0], df_id_excluido.editora_edicao.values[0], df_id_excluido.numero_edicao.values[0],
                df_id_excluido.ano_edicao.values[0], df_id_excluido.quantidade_exemplares.values[0])

                #Exibe para o usuário os dados do livro a ser excluído
                print(livro_excluido)

                #Solicita ao usuário a confirmação para exclusão
                exclusao:str = input("Deseja excluir esse registro do livro(S/N)? ").upper()

                #Garante que a resposta seja um valor valido
                while(exclusao != "S" and exclusao != "N"):
                    exclusao:str = input("Digite uma resposta válida(S/N): ").upper()

                if (exclusao == "S"):
                    #Realiza a exclusao do documento através de comando noSQL
                    conexao_exclusao.db["LIVROS"].delete_many({"id": id})

                    #Informa ao usuário o sucesso da operação
                    print("Livro excluido com sucesso")
                else:
                    print("Exclusão cancelada")
                
        else:
            print("O id passado não está cadastrado no sistema")

    
    def pesquisar_id_emprestimo(self, id:int):
        """
        Método pesquisar_id_emprestimo - Responsável por realizar uma busca do ID passado nos documentos da colecao 'Emprestimos'
        Parâmetros:
        id - ID que se deseja confirmar a presença nos documentos da colecao 'Emprestimos'
        Retorno: Retorna um DataFrame da biblioteca pandas contendo os documentos em que o ID está presente
        """

        #Cria uma nova conexão
        conexao_verificacao: MongoDBQueries = MongoDBQueries()
        conexao_verificacao.connect()

        #Realiza a pesquisa pelo ID do livro na colecao 'EMPRESTIMO', guardando o resultado no DataFrame
        df_resultado = pd.DataFrame(conexao_verificacao.db["EMPRESTIMOS"].find({}, {"ID": "$id",
        "Nome da Obra": "$nome_obra", "Autor da Obra": "$autor", "Editora da Edicao": "$editora_edicao",
        "Numero da Edicao":"$numero_edicao", "Ano da Edicao": "$ano_edicao", 
        "Quantidade de Exemplares":"$quantidade_exemplares","_id": 0}).sort({"nome_obra": 1, "autor": 1}))

        #Retorna o DataFrame
        return df_resultado
    
    def pesquisar_id(self, id: int):
        """
        Método 'pesquisar_id' - Responsável por pesquisar, na colecao 'Livros', um ID passado para confirmar se já foi cadastrado
        Parâmetros:
        id - ID que se deseja confirmar se está cadastrado no banco de dados
        Retorno:
        True - Caso o ID passado nao foi encontrado e nao está cadastrado
        False - Caso o ID passado foi encontrado e está cadastrado
        """
        
        #Cria uma nova conexão
        conexao_verificacao: MongoDBQueries = MongoDBQueries()
        conexao_verificacao.connect()

        #Realiza a pesquisa pelo ID na colecao 'Livros', guardando o resultado no DataFrame
        df_resultado = pd.DataFrame(conexao_verificacao.db["LIVROS"].find({"id": id}))

        #Retorna um boolean referente ao DataFrame estar vazio ou nao
        return df_resultado.empty

    def listar_livros(self):
        """
        Método listar_livros - Responsável por realizar a listagem dos livros cadastrados na colecao 'Livros'
        Retorno: Retorna um DataFrame da biblioteca pandas contendo os livros cadastrados
        """
        #Realiza conexão com o banco de dados
        conexao_listagem: MongoDBQueries = MongoDBQueries()
        conexao_listagem.connect()

        #Armazena em um dataframe o resultado da pesquisa dos documentos na colecao LIVROS
        df_listagem: pd.DataFrame = pd.DataFrame(conexao_listagem.db["LIVROS"].find({}, {"ID": "$id", "Nome da Obra": "$nome_obra", 
        "Autor da Obra": "$autor", "Editora da Edicao":"$editora_edicao", "Numero da Edicao":"$numero_edicao", 
        "Ano da Edicao": "$ano_edicao", "Quantidade de Exemplares":"$quantidade_exemplares", "_id": 0}).sort({"nome_obra": 1, "autor": 1}))
        
        #Retorna um DataFrame contendo a listagem dos livros cadastrados
        return df_listagem
