from conexao_bd.mySQL_queries import MySQLQueries
from entidades.alunos import Alunos


class ControleAlunos:
    """
    Classe 'ControleAlunos' - Responsável por controlar as alterações(Inserção, alterção e exclusão de registros) da tabela 'Alunos' do sistema por meio de comandos DML
    """
    def __init__(self):
        pass

    def cadastrar_aluno(self) -> Alunos:
        """
        Método 'cadastrar_aluno' - Responsável por realizar o processo de preenchimento dos campos necessários e posteriomente a inserção de um novo registro da tabela 'Alunos', valida as respostas do usuário para os campos não serem preenchidos com um valor inválido
        Retorno: Retorna um objeto da classe Alunos com os dados do registro cadastrado 
        """
        
        #Cria uma nova conexão
        conexao_cadastro: MySQLQueries = MySQLQueries(True)
        conexao_cadastro.connect()
        
        #Solicita ao usuário a matrícula do aluno a ser cadastrado
        print("Observação: A matricula é de 8 dígitos, caso digite de 1 até 7 digitos, o sistema irá preencher automaticamente o restante com 0.\nNão garante que não haverá outra matrícula igual já cadastrada")
        matricula_teste: str = input("Digite a matrícula do estudante: ").strip()
        
        #Garante que a matricula passada seja um número
        while (not matricula_teste.isdecimal()):
            print("Mátricula não é válida")
            matricula_teste = input("Digite a matrícula do estudante: ").strip()
        
        #Realiza a padronização da matrícula, garantido que tenha 8 dígitos
        if (len(matricula_teste) < 8):
            diferenca: int = 8 - len(matricula_teste)
            matricula_teste = matricula_teste + ("0" * diferenca)
        
        #Guarda a matrícula em uma variável int após garantir que não haverá problema na conversão de tipo
        matricula: int = int(matricula_teste)

        #Verifica se a matricula passada já não está cadastrada no sistema
        if (not self.pesquisar_matricula(matricula)):

            #Solicita ao usuário o nome do aluno
            nome:str = input("Digite o nome do aluno (Sem acento): ").strip()

            #Garante que não será passado um valor vazio para não quebrar lógica do programa
            while (nome == ""):
                print("Erro no nome passado")
                nome = input("Digite um nome válido para ser cadastrado(Sem resposta vazia): ")
            
            #Solicita ao usuário o email do aluno
            email:str = input("Digite o email do aluno: ").strip()

            #Garante que não será passado um valor vazio para não quebrar lógica do programa
            while (email == ""):
                print("Erro no email passado")
                email = input("Digite um email válido para ser cadastrado(Sem resposta vazia): ")
            
            #Realiza a inserção do aluno na tabela ALUNOS através do comando SQL
            conexao_cadastro.write(f"insert into ALUNOS values({matricula},'{nome}','{email}');")

            #Salva os dados do aluno cadastrado em um DataFrame da biblioteca Bandas
            df_resultado = conexao_cadastro.execute_query_dataframe(f"select * from ALUNOS where matricula = {matricula}")

            #Salva os dados do aluno em um objeto da classe Aluno
            aluno = Alunos(df_resultado.matricula.values[0], df_resultado.nome.values[0],df_resultado.email.values[0])
            
            #Sinaliza ao usuário o sucesso da operação, retornando também os dados do registro cadastrado
            print("Aluno cadastrado com sucesso")
            print(aluno)   

            input("Digite Enter para sair")

            #Retorna o Objeto aluno, caso tenha necessidade futura
            return aluno
        else:
            print("A matricula passada já está cadastrada")
            return None

    def alterar_aluno(self) -> Alunos:
        """
        Método 'alterar_aluno' - Responsável por realizar o processo de atualização dos dados de um registro da tabela 'Alunos', valida as respostas do usuário para os campos não serem preenchidos com um valor inválido
        Retorno: Retorna um objeto da classe Alunos com os dados do registro atualizado 
        """      
        #Cria uma nova conexão
        conexao_atualizacao = MySQLQueries(True)
        conexao_atualizacao.connect()

        #Exibe os alunos cadastrados na tabela 'Alunos'
        print("ALUNOS CADASTRADOS")
        print(self.listar_alunos())

        #Solicita ao usuário a matrícula do aluno a ser cadastrado
        matricula_teste: str = input("Digite a matrícula do estudante a ter os dados alterados: ").strip()
        
        #Garante que a matricula passada seja um número
        while (not matricula_teste.isdecimal()):
            print("Mátricula não é válida")
            matricula_teste = input("Digite a matrícula do estudante a ter os dados alterados(Somente números): ").strip()

        #Guarda a matrícula em uma variável int após garantir que não haverá problema na conversão de tipo
        matricula: int = int(matricula_teste)

        #Verifica se a matricula passada já está cadastrada no sistema
        if (self.pesquisar_matricula(matricula)):

            #Solicita ao usuário o novo nome do aluno
            nome_novo:str = input("Digite o novo nome a ser registrado (Sem acento): ").strip()

            #Garante que não será passado um valor vazio para não quebrar lógica do programa
            while (nome_novo == ""):
                print("Erro no nome passado")
                nome_novo = input("Digite um novo nome válido a ser registrado(Sem resposta vazia): ")

            #Solicita ao usuário o novo email do aluno
            email_novo:str = input("Digite o novo email do aluno: ").strip()
            
            #Garante que não será passado um valor vazio para não quebrar lógica do programa
            while (email_novo == ""):
                print("Erro no email passado")
                email_novo = input("Digite um novo email válido para ser registrado(Sem resposta vazia): ")

            #Realiza a atualização dos dados do aluno na tabela ALUNOS através do comando SQL
            conexao_atualizacao.write(f"update ALUNOS set nome = '{nome_novo}', email = '{email_novo}' where matricula = {matricula};")

            #Salva os dados atualizado do aluno em um DataFrame da biblioteca Bandas
            df_resultado = conexao_atualizacao.execute_query_dataframe(f"select * from ALUNOS where matricula = {matricula}")

            #Salva os dados do aluno em um objeto da classe Aluno
            aluno_atualizado = Alunos(df_resultado.matricula.values[0], df_resultado.nome.values[0],df_resultado.email.values[0])

            #Sinaliza ao usuário o sucesso da operação, retornando também os dados do registro atualizado
            print("Registro do aluno atualizado com sucesso!")
            print(aluno_atualizado)
            
            input("Digite Enter para sair")

            #Retorna o Objeto aluno, caso tenha necessidade futura
            return aluno_atualizado

        else:
            print("A matricula passada não está cadastrada no sistema")
            return None

    def excluir_aluno(self):
        """
        Método 'excluir_aluno' - Responsável por realizar o processo de exclusão de um registro da tabela 'Alunos', valida as respostas do usuário para os campos não serem preenchidos com um valor inválido 
        """  
        #Cria uma nova conexão
        conexao_exclusao = MySQLQueries(True)
        conexao_exclusao.connect()

        #Exibe os alunos cadastrados na tabela 'Alunos'
        print("ALUNOS CADASTRADOS")
        print(self.listar_alunos())

        #Solicita ao usuário a matrícula do aluno a ter o registro excluído
        matricula_teste: str = input("Digite a matrícula do estudante: ").strip()
        
        #Garante que a matricula passada seja um número
        while (not matricula_teste.isdecimal()):
            print("Mátricula não é válida")
            matricula_teste = input("Digite a matrícula do estudante(Somente números): ").strip()

        #Guarda a matrícula em uma variável int após garantir que não haverá problema na conversão de tipo
        matricula: int = int(matricula_teste)

        #Verifica se a matricula passada já está cadastrada no sistema
        if (self.pesquisar_matricula(matricula)):

            #Guarda em um DataFrame o resultado do método pesquisar_matricula_emprestimo()
            df_matricula_emprestimos = self.pesquisar_matricula_emprestimo(matricula)

            #Verifica se a matrícula passada está presente em algum emprestimo da tabela 'Emprestimos'
            if (len(df_matricula_emprestimos.index) > 0):

                #Se estiver presente, impede a exclusão da mesma e mostra ao usuário em quais emprestimos ela participa
                print("A matricula passada está presente nos seguintes registros de empréstimos")
                print(df_matricula_emprestimos)
                print("Apague ou modifique esses registros para poder excluir essa matricula")
                input("Digite ENTER para sair:")
            else:
                
                #Caso não esteja, procede para sua exclusão guardando seus dados em um data frame
                df_matricula_excluida = conexao_exclusao.execute_query_dataframe(f"select * from ALUNOS where matricula = {matricula}")

                #Cria um objeto da classe Alunos com dados do registro a ser excluído
                aluno_excluido: Alunos = Alunos(df_matricula_excluida.matricula.values[0], 
                df_matricula_excluida.nome.values[0], df_matricula_excluida.email.values[0])

                #Mostra na tela os dados do aluno a ser excluído
                print(aluno_excluido)

                #Solicita ao usuário a confirmação para exclusão
                exclusao:str = input("Deseja excluir esse registro do aluno(S/N)? ").upper()

                #Garante que a resposta seja um valor valido
                while(exclusao != "S" and exclusao != "N"):
                    exclusao:str = input("Digite uma resposta válida(S/N): ").upper()

                if(exclusao == "S"):
                    
                    #Realiza a exclusão do registro, sinalizando ao usuário o sucesso da operação
                    conexao_exclusao.write(f"delete from ALUNOS where matricula = {matricula}")
                    print("Aluno excluido com sucesso")
                else:
                    print("Exclusão cancelada")

                
        else:
            print("A matrícula passada não está cadastrada no sistema")

    def pesquisar_matricula(self, matricula:int):
        """
        Método 'pesquisar_matricula' - Responsável por pesquisar, na tabela 'Alunos', uma matrícula passada para confirmar se já foi cadastrada
        Parâmetros:
        matricula - Matricula que se deseja confirmar se está cadastrada no banco de dados
        Retorno:
        True - Caso a matricula passada foi encontrada e está cadastrada
        False - Caso a matricula passada não foi encontrada e não está cadastrada
        """

        #Realiza conexão com o banco de dados
        conexao_verificacao: MySQLQueries = MySQLQueries()
        conexao_verificacao.connect()
        query_verificacao = f'select * from ALUNOS where matricula = {matricula}'

        #Realiza a pesquisa pela matrícula na tabela 'Alunos', guardando o resultado no DataFrame
        df_resultado = conexao_verificacao.execute_query_dataframe(query_verificacao)

        #Realiza a contagem de registros no DataFrame, retornando False se não tiver registros, True caso contrário
        if len(df_resultado.index) == 0:
            return False
        else:
            return True

    def pesquisar_matricula_emprestimo(self, matricula:int):
        """
        Método pesquisar_matricula_emprestimo - Responsável por realizar uma busca da matricula passada nos registros da tabela 'Emprestimos'
        Parâmetros:
        matricula - Matricula que se deseja confirmar a presença nos registros da tabela 'Emprestimos'
        Retorno: Retorna um DataFrame da biblioteca pandas contendo os registros em que a matricula está presente
        """
        
        #Realiza conexão com o banco de dados
        conexao_verificacao: MySQLQueries = MySQLQueries()
        conexao_verificacao.connect()

        #Guarda em uma variavel a query a ser realizada
        query_verificacao = (f"select codigo as 'Codigo Emprestimo', codigo_livro as 'ID livro'," 
        + f"codigo_aluno as 'Matricula Aluno', data_devolucao as 'Data de Devolucao'from EMPRESTIMOS where codigo_aluno = {matricula}")

        #Guarda o resultado da query em um DataFrame e retorna esse data frame
        df_resultado = conexao_verificacao.execute_query_dataframe(query_verificacao)
        return df_resultado

    def listar_alunos(self):
        """
        Método listar_alunos - Responsável por realizar a listagem dos alunos cadastrados na tabela 'Alunos'
        Retorno: Retorna um DataFrame da biblioteca pandas contendo os alunos cadastrados
        """
        #Realiza conexão com o banco de dados
        conexao_listagem: MySQLQueries = MySQLQueries()
        conexao_listagem.connect()

        #Armazena em uma variável o código SQL para listar os alunos cadastrados
        query_verificacao = ("select matricula as 'Matricula do Aluno', nome as 'Nome Aluno', email as 'Email Aluno'" + "from ALUNOS order by nome;")
        
        #Retorna um DataFrame contendo a listagem dos alunos cadastrados
        return conexao_listagem.execute_query_dataframe(query_verificacao)

