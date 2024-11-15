from conexao_bd.mongoDB_queries import MongoDBQueries
from entidades.emprestimos import Emprestimos
from controle.controle_alunos import ControleAlunos
from controle.controle_livros import ControleLivros
from entidades.alunos import Alunos
from entidades.livros import Livros
from datetime import date
from datetime import timedelta
import pandas as pd


class ControleEmprestimos:
    """
    Classe 'ControleEmprestimos' - Responsável por controlar as alterações(Inserção, alterção e exclusão de registros) da tabela 'Emprestimos' do sistema por meio de comandos DML
    """
    def __init__(self):
        self.controlador_livros = ControleLivros()
        self.controlador_alunos = ControleAlunos()
        pass
    
    def cadastrar_emprestimo(self) -> Emprestimos:
        """
        Método 'cadastrar_emprestimo' - Responsável por realizar o processo de preenchimento dos campos necessários e posteriomente a inserção de um novo documento na colecao 'Emprestimos', valida as respostas do usuário para os campos não serem preenchidos com um valor inválido
        Retorno: Retorna um objeto da classe Emprestimo com os dados do documento criado 
        """
        #Cria uma nova conexão
        conexao_inserir = MongoDBQueries()
        conexao_inserir.connect()

        #Solicita ao usuário o código do emprestimo a ser cadastrado
        codigo_teste: str = input("Insira o codigo do emprestimo a ser cadastrado: ").strip()

        #Garante que o emprestimo passado seja um número
        while not codigo_teste.isdecimal():
            print("Erro no código digitado")
            codigo_teste: str = input("Insira outro codigo para o emprestimo a ser cadastrado: ").strip()
        
        #Guarda o código em uma variável int após garantir que não haverá problema na conversão de tipo
        codigo: int = int(codigo_teste)

        #Verifica se o código passado já não está cadastrado no sistema
        if (self.pesquisar_codigo(codigo)):

            #Cria uma variavel flag para controlar o preenchimento do campos
            flag: bool = False

            #Exibe para o usuário os livros cadastrados na tabela 'Livros'
            print("LIVROS CADASTRADOS")
            print(self.controlador_livros.listar_livros())

            #Garante que o código passado seja um válido
            while (not flag):

                #Solicita ao usuário o código do livro
                codigo_livro_teste: str = input("Insira o codigo do livro emprestado: ").strip()

                #Garante que o valor passado seja um número
                while not codigo_livro_teste.isdecimal():
                    print("Erro no código digitado")
                    codigo_livro_teste: str = input("Insira um código válido(Somente números): ").strip()
                
                #Guarda o resultado do método pesquisar_id na variável flag
                flag = not self.controlador_livros.pesquisar_id(int(codigo_livro_teste))
                if (not flag):

                    #Informa ao usuário se o código passado não está cadastrado no sistema
                    print("Código de livro passado não está cadastrado no sistema")
                else:

                    #Guarda na variavel flag o resultado do método pesquisar_disponibilidade
                    flag = self.pesquisar_disponibilidade(int(codigo_livro_teste))
                    if (not flag):

                        #Informa ao usuário se não houver mais exemplares disponíveis do código do livro passado
                        print("Não há mais exemplares disponíveis do código passado, todos já estão emprestados")

            #Guarda o código em uma variável int após garantir que não haverá problema na conversão de tipo
            codigo_livro = int(codigo_livro_teste)

            #Cria um objeto da classe Livros baseado no código passado pelo usuário
            livro = self.criar_livro(codigo_livro)

            #Cria uma variavel flag para controlar o preenchimento do campos
            flag = False

            #Exibe para o usuário os alunos cadastrados na tabela 'Alunos'
            print("ALUNOS CADASTRADOS")
            print(self.controlador_alunos.listar_alunos())

            #Garante que o código do aluno passado seja válido
            while (not flag):

                #Solicita ao usuário o código do aluno
                print("OBS: Cada aluno só pode ter 3 livros emprestados em sua posse ao mesmo tempo, \nsendo necessário devolver algum dos 3 caso queira realizar mais 1 empréstimo")
                codigo_aluno_teste: str = input("Insira a matrícula do aluno que realizou o empréstimo: ").strip()

                #Garante que o codigo passado seja um número
                while not codigo_aluno_teste.isdecimal():
                    print("Erro na matrícula digitada")
                    codigo_aluno_teste: str = input("Insira uma matrícula válida(Somente números): ").strip()
                
                #Guarda o resultado do método pesquisar_matricula na variável flag
                flag = not self.controlador_alunos.pesquisar_matricula(int(codigo_aluno_teste))
                if (not flag):

                    #Informa ao usuário se o código passado não está cadastrado no sistema
                    print("Matrícula passada não está cadastrada no sistema")
                else:
                    
                    #Guarda em uma variável o resultado do método pesquisar_matricula_emprestimo
                    df_matricula_emprestimos = self.controlador_alunos.pesquisar_matricula_emprestimo(int(codigo_aluno_teste))

                    #Verifica se a matrícula passada já atingiu o limite de emprestimos
                    if(len(df_matricula_emprestimos.index) >= 3):
                        flag = False
                        print("O aluno já está em posse de 3 livros")
                        print(df_matricula_emprestimos)
                        print("Devolva um dos emprestimos para poder pegar outro livro")
                    else:
                        flag = True

            #Guarda o código em uma variável int após garantir que não haverá problema na conversão de tipo
            codigo_aluno:int = int(codigo_aluno_teste)

            #Cria um objeto da classe Alunos baseado no código passado pelo usuário
            aluno = self.criar_aluno(codigo_aluno)

            #Informa ao usuário sobre o prazo de emprestimo padrão
            print("O emprestimo seguirá o prazo padrão, devendo ser devolvido em 14 dias após seu cadastro")

            #Cria a data de devolução do emprestimo
            data_devolucao: date = date.today() + timedelta(days=14)

            #Realiza a inserção do emprestimo na tabela 'Emprestimos' através de código noSQL
            conexao_inserir.db["EMPRESTIMOS"].insert_one({"codigo": codigo, "codigo_livro": codigo_livro, 
            "codigo_aluno": codigo_aluno, "data_devolucao": data_devolucao.strftime("%Y-%m-%d")})
        
            #Guarda em uma variável DataFrame os campos do registro do emprestimo
            df_resultado = pd.DataFrame(conexao_inserir.db["EMPRESTIMOS"].find({"codigo": codigo}))

            #Extrai as informacoes da data de devolucao e cria um objeto date baseade nelas
            elementos_data: list = df_resultado.data_devolucao.values[0].split("-")
            data = date(int(elementos_data[0]), int(elementos_data[1]), int(elementos_data[2]))

            #Cria um objeto da classe Emprestimos com os dados do emprestimos
            emprestimo: Emprestimos = Emprestimos(df_resultado.codigo.values[0], livro, aluno, data)
            print("Emprestimo cadastrado com sucesso")

            #Exibe na tela os dados do objeto emprestimo
            print(emprestimo)
            input("Digite Enter para sair")

            #Retorna o objeto para qualquer necessidade futura
            return emprestimo

        else:
            print("Código passado já foi cadastrado no sistema")
            return None

    def alterar_emprestimo(self) -> Emprestimos:
        """
        Método 'alterar_emprestimo' - Responsável por realizar o processo de atualização dos dados de um documento da colecao 'Emprestimos', valida as respostas do usuário para os campos não serem preenchidos com um valor inválido
        Retorno: Retorna um objeto da classe Emprestimos com os dados do documento atualizado 
        """  

        #Cria uma nova conexão
        conexao_alteracao = MongoDBQueries()
        conexao_alteracao.connect()

        #Exibe para o usuário os emprestimos cadastrados na tabela 'Emprestimos'
        print("EMPRESTIMOS CADASTRADOS")
        print(self.listar_emprestimos())
        
        #Solicita ao usuário o código do emprestimo a ser modificado
        codigo_teste: str = input("Insira um codigo de emprestimo já cadastrado: ").strip()

        #Garante que o codigo passado seja um número
        while not codigo_teste.isdecimal():
            print("Erro no código digitado")
            codigo_teste: str = input("Insira outro codigo para um emprestimo já cadastrado: ").strip()
        
        #Guarda o código em uma variável int após garantir que não haverá problema na conversão de tipo
        codigo: int = int(codigo_teste)

        #Verifica se o codigo passado já está cadastrado na tabela 'Emprestimos'
        if (not self.pesquisar_codigo(codigo)):

            #Cria uma variavel flag para controlar o preenchimento do campos
            flag: bool = False

            #Exibe para o usuário os livros cadastrados na tabela 'Livros'
            print("LIVROS CADASTRADOS")
            print(self.controlador_livros.listar_livros())

            #Garante que o código do livro passado seja válido
            while (not flag):

                #Solicita ao usuário o novo codigo do livro
                codigo_livro_novo_teste: str = input("Insira o codigo do livro emprestado(novo): ").strip()

                #Garante que o código passado seja m número
                while not  codigo_livro_novo_teste.isdecimal():
                    print("Erro no código digitado")
                    codigo_livro_novo_teste: str = input("Insira um novo código válido(Somente números): ").strip()
                
                #Guarda o resultado do método pesquisar_id na variável flag
                flag = not self.controlador_livros.pesquisar_id(int(codigo_livro_novo_teste))
                
                #Informa ao usuário se o codigo passado não estiver cadastrado na tabela 'Livros'
                if (not flag):
                    print("Código de livro passado não está cadastrado no sistema")
                else:

                    #Guarda o resultado do método pesquisar_disponibilidade na variável flag
                    flag = self.pesquisar_disponibilidade(int(codigo_livro_novo_teste))

                    #Informa ao usuário se não existir mais exemplares disponíveis do código de livro passado
                    if (not flag):
                        print("Não há mais exemplares disponíveis do código passado, todos já estão emprestados")

            #Guarda o código em uma variável int após garantir que não haverá problema na conversão de tipo
            codigo_livro_novo = int(codigo_livro_novo_teste)

            #Cria um objeto da classe Alunos baseado no código passado pelo usuário
            livro_novo = self.criar_livro(codigo_livro_novo)
            
            flag = False

            #Exibe para o usuário os alunos cadastrados na tabela 'Alunos'
            print("ALUNOS CADASTRADOS")
            print(self.controlador_alunos.listar_alunos())


            #Garante que o código do aluno passado seja válido
            while (not flag):

                #Solicita ao usuário o novo código do aluno
                codigo_aluno_novo_teste: str = input("Insira a matrícula do aluno que realizou o empréstimo(nova): ").strip()

                #Garante que o código passado seja um número
                while not codigo_aluno_novo_teste.isdecimal():
                    print("Erro na matrícula digitada")
                    codigo_aluno_novo_teste: str = input("Insira uma nova matrícula válida(Somente números): ").strip()
                
                #Guarda na variável flag o resultado do método pesquisar_matricula
                flag = not self.controlador_alunos.pesquisar_matricula(int(codigo_aluno_novo_teste))

                #Informa ao usuário se a matrícula não estiver cadastrada na tabela 'Alunos'
                if (not flag):
                    print("Matrícula passada não está cadastrada no sistema")
                else:
                    
                    #Guarda em uma variável o resultado do método pesquisar_matricula_emprestimo
                    df_matricula_emprestimos = self.controlador_alunos.pesquisar_matricula_emprestimo(int(codigo_aluno_novo_teste))

                    #Verifica se a matrícula passada já atingiu o limite de emprestimos
                    if(len(df_matricula_emprestimos.index) >= 3):
                        flag = False
                        print("O aluno já está em posse de 3 livros")
                        print(df_matricula_emprestimos)
                        print("Devolva um dos emprestimos para poder pegar outro livro")
                    else:
                        flag = True

            #Guarda o código em uma variável int após garantir que não haverá problema na conversão de tipo
            codigo_aluno_novo:int = int(codigo_aluno_novo_teste)

            #Cria um objeto da classe Alunos baseado no código passado pelo usuário
            aluno_novo = self.criar_aluno(codigo_aluno_novo)

            #Informa ao usuário sobre o prazo de emprestimo padrão
            print("O emprestimo seguirá o prazo padrão, devendo ser devolvido em 14 dias após seu cadastro")

            #Cria a data de devolução do emprestimo
            data_devolucao_nova: date = date.today() + timedelta(days=14)

            #Realiza a alteração dos campos do documento desejado através de comando noSQL
            conexao_alteracao.db["EMPRESTIMOS"].update_one({"codigo": codigo}, {"$set": 
            {"codigo_livro": codigo_livro_novo, "codigo_aluno": codigo_aluno_novo, 
            "data_devolucao": data_devolucao_nova.strftime("%Y-%m-%d")}})
            
            #Guarda os campos do documento alterado em um DataFrame
            df_resultado = pd.DataFrame(conexao_alteracao.db["EMPRESTIMOS"].find({"codigo": codigo}))

            #Retira oas informacoes da data da devolucao e cria um objeto da classe date com essas informacoes
            elementos_data: list = df_resultado.data_devolucao.values[0].split("-")
            data_nova: date = date(int(elementos_data[0]), int(elementos_data[1]), int(elementos_data[2]))
            
            #Cria um objeto da classe Emprestimos para guardar os dados do documento
            emprestimo = Emprestimos(df_resultado.codigo.values[0], livro_novo, aluno_novo, data_nova)

            #Informa ao usuário o sucesso em atualizar os dados do documento, exibindo esses dados
            print("Registro de emprestimo alterado com sucesso")
            print(emprestimo)

            input("Digite Enter para sair")
            
            #Retorna o objeto Emprestimos para qualquer uso futuro
            return emprestimo

        else:
            print("Código passado não está cadastrado no sistema")
            return None

    def excluir_emprestimo(self):
        """
        Método 'excluir_emprestimo' - Responsável por realizar o processo de exclusão de um documento da colecao 'Emprestimos', valida as respostas do usuário para os campos não serem preenchidos com um valor inválido 
        """  

        #Cria uma nova conexão
        conexao_exclusao = MongoDBQueries()
        conexao_exclusao.connect()

        #Exibe para o usuário os emprestimos cadastrados na colecao 'Emprestimos'
        print("EMPRESTIMOS CADASTRADOS")
        print(self.listar_emprestimos())

        #Solicita ao usuário o codigo do emprestimo
        codigo_teste: str = input("Digite o codigo do emprestimo: ").strip()
        
        #Garante que o codigo passado seja um número
        while (not codigo_teste.isdecimal()):
            print("codigo não é válido")
            codigo_teste = input("Digite o código do emprestimo: ").strip()

        #Guarda o código em uma variável int após garantir que não haverá problema na conversão de tipo
        codigo: int = int(codigo_teste)

        #Verifica se o código passado está cadastrado na tabela 'Emprestimos'
        if (not self.pesquisar_codigo(codigo)):

                #Guarda em um DataFrame os campos do documento a ser excluído
                df_codigo_excluido = pd.DataFrame(conexao_exclusao.db["EMPRESTIMOS"].find({"codigo": codigo}))
                print(df_codigo_excluido.codigo_livro.values[0])
                #Cria respectivamente objetos da classe Livros, Alunos e date
                livro: Livros = self.criar_livro(df_codigo_excluido.codigo_livro.values[0])
                aluno: Alunos = self.criar_aluno(df_codigo_excluido.codigo_aluno.values[0])
                elementos_data: list = df_codigo_excluido.data_devolucao.values[0].split("-")
                data: date = date(int(elementos_data[0]), int(elementos_data[1]), int(elementos_data[2]))

                #Guarda em um objeto da classe Emprestimos os dados do regdcoumentoistro a ser excluído
                emprestimo_excluido: Emprestimos = Emprestimos(df_codigo_excluido.codigo.values[0], livro, aluno, data)
                print(emprestimo_excluido)

                #Solicita ao usuário a confirmação para exclusão
                exclusao:str = input("Deseja excluir esse registro do Emprestimo(S/N)? ").upper()

                #Garante que a resposta seja um valor valido
                while(exclusao != "S" and exclusao != "N"):
                    exclusao:str = input("Digite uma resposta válida(S/N): ").upper()

                if (exclusao == "S"):
                    
                    #Realiza a exclusão do registro por meio de comando SQL
                    conexao_exclusao.db["EMPRESTIMOS"].delete_one({"codigo": codigo})

                    #Informa ao usuário o sucesso na operação,
                    print("Emprestimo excluido com sucesso")
                else:
                    print("Exclusão cancelada")
                
        else:
            print("O código passado não está cadastrado no sistema")


    def pesquisar_codigo(self, codigo:int) -> bool:
        """
        Método 'pesquisar_codigo' - Responsável por pesquisar, na colecao 'Emprestimos', um codigo passado para confirmar se já foi cadastrado
        Parâmetros:
        codigo - Código que se deseja confirmar se está cadastrado no banco de dados
        Retorno:
        True - Caso o codigo passado nao foi encontrado e nao está cadastrado
        False - Caso o codigo passado foi encontrado e está cadastrado
        """
        
        #Realiza conexão com o banco de dados
        conexao_verificacao: MongoDBQueries = MongoDBQueries()
        conexao_verificacao.connect()

        #Realiza a pesquisa pelo codigo na colecao 'Emprestimos', guardando o resultado em um DataFrame
        resultado = pd.DataFrame(conexao_verificacao.db["EMPRESTIMOS"].find({"codigo": codigo}))
    
        #Retorna se o DataFrame gerado pela pesquisa esta vazio
        return resultado.empty
    

    def pesquisar_disponibilidade(self, codigo:int) -> bool:
        """
        Método 'pesquisar_disponibilidade' - Responsável por pesquisar, na tabela 'Livros', a quantidade de exemplares do código de livro passado
        Parâmetros:
        codigo - Código do livro que se deseja confirmar a quantidade de exemplares em estoque
        Retorno:
        True - Caso tenha exemplares disponíveis para empréstimos
        False - Caso não tenha exemplares disponíveis para empréstimos
        """
        
        #Realiza conexão com o banco de dados
        conexao_verificacao: MongoDBQueries = MongoDBQueries()
        conexao_verificacao.connect()

        #Realiza a pesquisa da quantidade de participação do código na colecao 'Emprestimos', guardando a quantidade em uma variável
        quantidade_emprestada:int = conexao_verificacao.db["EMPRESTIMOS"].count_documents({"codigo_livro": codigo})
        
        #Realiza a pesquisa pela quantidade de exemplares do codigo na colecao 'Livros', guardando a quantidade em uma variável
        df_qtd_diponivel: pd.DataFrame = pd.DataFrame(conexao_verificacao.db["LIVROS"].find({"id": codigo}, 
        {"quantidade_exemplares": 1, "_id": 0}))
        quantidade_disponivel: int = df_qtd_diponivel.quantidade_exemplares.values[0]
        
        #Realiza a comparação entre variáveis, retornando False se não houver mais exemplares disponíveis, True caso contrário
        if (quantidade_emprestada >= quantidade_disponivel):
            return False
        else:
            return True

    def criar_aluno(self, matricula: int) -> Alunos:
        """
        Método 'criar_aluno' - Responsável por criar um objeto da colecao Alunos a partir de uma matrícula já cadastrada na colecao 'Alunos'
        Parâmetros:
        matricula - Matricula do aluno que se deseja transformar em objeto
        Retorno: Um objeto da classe Aluno com os dados do registro onde a matricula passada está inserida
        """
        #Realiza conexão com o banco de dados
        conexao_criacao: MongoDBQueries = MongoDBQueries()
        conexao_criacao.connect()

        #Realiza a pesquisa pela matrícula na colecao 'Alunos', guardando o resultado no DataFrame
        df_resultado = pd.DataFrame(conexao_criacao.db["ALUNOS"].find({"matricula": int(matricula)}))

        #Salva os dados do aluno em um objeto da classe Alunos
        aluno = Alunos(df_resultado.matricula.values[0], df_resultado.nome.values[0],df_resultado.email.values[0])

        #Retorna o objeto criado
        return aluno

    def criar_livro(self, id: int) -> Livros:
        """
        Método 'criar_livro' - Responsavel por criar um objeto da classe Livros a partir de um ID já cadastrado na colecao 'Alunos'
        Parâmetros:
        id - ID do livro que se deseja transformar em objeto
        Retorno: Um objeto da classe Livros com os dados do documento onde o ID passado está inserido
        """
        #Realiza conexão com o banco de dados
        conexao_criacao: MongoDBQueries = MongoDBQueries()
        conexao_criacao.connect()

        #Realiza a pesquisa pelo ID na colecao 'Livros', guardando o resultado no DataFrame
        df_resultado = pd.DataFrame(conexao_criacao.db["LIVROS"].find({"id": int(id)}))

        #Salva os dados do livro em um objeto da colecao Livros
        livro: Livros = Livros(df_resultado.id.values[0], df_resultado.nome_obra.values[0],
        df_resultado.autor.values[0], df_resultado.editora_edicao.values[0], df_resultado.numero_edicao.values[0],
        df_resultado.ano_edicao.values[0], df_resultado.quantidade_exemplares.values[0])

        #Retorna o objeto criado
        return livro
    
    def listar_emprestimos(self):
        """
        Método listar_emprestimos - Responsável por realizar a listagem dos emprestimos cadastrados na colecao 'Emprestimos'
        Retorno: Retorna um DataFrame da biblioteca pandas contendo os emprestimos cadastrados
        """

        #Realiza conexão com o banco de dados
        conexao_listagem: MongoDBQueries = MongoDBQueries()
        conexao_listagem.connect()

        #Realiza a listagem dos emprestimos cadastrados no banco de dados
        df_listagem: pd.DataFrame = pd.DataFrame(conexao_listagem.db["EMPRESTIMOS"].aggregate([
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
])
        )
        
        #Retorna um DataFrame contendo a listagem dos emprestimos cadastrados
        return df_listagem
    