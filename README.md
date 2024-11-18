# SISTEMA DE BIBLIOTECA ESCOLAR EM PYTHON
O sistema presente nesse repositório representa um sistema de emprestimo de livros utilizado por uma biblioteca escolar, composto por um conjunto de coleções para representar os emprestimos, sendo elas: __Livros, Alunos e Emprestimos__

## PREPARANDO PARA UTILIZAÇÃO DO SISTEMA

Primeiramente, para funcionamento do sistema, é necessário a instalação de certas bibliotecas através da utilização de um [arquivo que contém as bibliotecas e suas respectivas versões](src/bibliotecas.txt):
``` shell
pip install -r bibliotecas.txt 
```

O sistema produzido exige que as tabelas no banco de dados MySQL existam, pois será a partir dele que as coleções no banco de dados MongoDB serão criadas, portanto antes de rodar o programa principal, é necessário a execução do seguinte script em Python:

``` shell
~$ python criar_tabelas_registros.py
```
Em seguida, para criar efetivamente as coleções e seus documentos, é necessário a execução do seguinte script em Python:

``` shell
~$ python criar_colecoes_documentos.py
```

## INICIANDO O SISTEMA 

Tendo executado os scripts anteriormente mencionado e finalizado a criação das colecoes, junto com os documentos de exemplo, basta executar o script principal do sistema:

``` shell
~$ python principal.py
```
Para uma explicação prática do funcionamento do sistema, acesse o vídeo gravado pelos componentes:
- [Video](https://youtu.be/B0yFLeq7exc)

## ORGANIZAÇÃO REPOSITÓRIO

- [Diagrama](Diagrama): Nesse diretório está contido o [diagrama relacional](Diagrama/DIAGRAMA_RELACIONAL_SISTEMA_BIBLIOTECA_ESCOLAR.pdf) do sistema, com suas entidades e relacionamentos.
  * As entidades representadas no diagrama são: ALUNOS, EMPRESTIMOS E LIVROS
- [sql_tabelas](sql_tabelas): Nesse diretório estão contidos os scripts SQL responsáveis pela criação das tabelas e da inserção de registros fictícios nessas tabelas, necessarias para a criação das coleções e documentos de exemplo do sistema
  * [criar_tabelas_biblioteca_escolar.sql](sql_tabelas/criar_tabelas_biblioteca_escolar.sql): Script SQL responsável pela criação das tabelas utilizadas, tal como os seus relacionamentos;
  *  [inserir_dados_tabelas_biblioteca_escolar.sql](sql_tabelas/inserir_dados_tabelas_biblioteca_escolar.sql): Script SQL responsável por inserir registros de exemplos nas tabelas.
- [src](src): Nesse diretório estão guardados os scripts responsáveis pelo funcionamento do sistema
  * [conexao_bd](src/conexao_bd) - Nesse diretório estão guardadas as classes responsaveis por realizarem a conexão do sistema com o banco de dados mySQL e mongoDB, tal como os arquivos responsaveis por guardar dados úteis para autentificação do usuário
    - [mySQL_queries.py](src/conexao_bd/mySQL_queries.py) - Classe responsável por realizar a conexão com o banco de dados mySQL, também realizando os comandos DML(como inserção, alteração ou exclusão de registros) e DDL(como a criação, alteração ou exclusão de tabelas), além das querys para os relatórios.
       + Exemplo da sua utilização para uma consulta simples:
         ``` python
         def gerar_registros(query:str):
         """
         Função gerar_registros - Responsável pela inserção de registros de exemplos nas tabelas para facilitar a experiência do usuário
         Parâmetros:
         query - Código SQL para inserção dos registros nas tabelas
         """
     
         #Guarda em uma variável o código SQL de inserção de registros, separando as linhas de comando por meio do ';'
         lista_comandos = query.split(';')
     
         #Cria uma nova conexão com o banco de dados
         mySQL_connector = MySQLQueries(can_write=True)
         mySQL_connector.connect()
     
         #Percorre cada uma das linhas de comando, tentando exercuta-la e informando ao usuário do sucesso ou não da operação
         for comando in lista_comandos:
             if len(comando) > 0:
                 mySQL_connector.write(comando)
                 print(f"Comando '{comando}' executado")
         ```
    - [MongoDBQueries.py](src/conexao_bd/mongoDB_queries.py) - Classe responsável por realizar a conexão com o banco de dados mongoDB, também realizando os comandos DML(como inserção, alteração ou exclusão de documento) e DDL(como a criação, alteração ou exclusão de coleções), além das querys para os relatórios.
       + Exemplo da sua utilização para uma consulta simples:
         ``` python
         def listar_alunos(self):
          """
          Método listar_alunos - Responsável por realizar a listagem dos alunos cadastrados na colecao 'Alunos'
          Retorno: Retorna um DataFrame da biblioteca pandas contendo os alunos cadastrados
          """
          #Realiza conexão com o banco de dados
          conexao_listagem: MongoDBQueries = MongoDBQueries()
          conexao_listagem.connect()
  
          #Realiza a pesquisa pelos alunos cadastrados e guarda o resultado em um DataFrame Pandas
          df_listagem = pd.DataFrame(conexao_listagem.db["ALUNOS"].find({}, {"Matricula do Aluno": "$matricula", "Nome Aluno": "$nome", "Email Aluno": "$email", "_id": 0}).sort({"nome": 1}))
          
          #Retorna um DataFrame contendo a listagem dos alunos cadastrados
          return df_listagem
         ```
    - [autenticador_mySQL](src/conexao_bd/autenticador/autenticador_mySQL.txt) - Arquivo contendo informações para conexão com o banco de dados MYSQL, sendo respectivamente o nome do banco de dados, o usuário do banco de dados e a senha do banco de dados.
    - [autenticador_mongoDB](src/conexao_bd/autenticador/autenticador_mongoDB.txt) - Arquivo contendo informações para conexão com o banco de dados mongoDB, sendo respectivamente o usuário do banco de dados e a senha do banco de dados.
  * [controle](src/controle): Diretório onde estão contidas as classes responsáveis por controlar as operações de inserção, alteração e exclusão de cada coleção.
    - [controle_alunos.py](src/controle/controle_alunos.py): Classe responsável por controlar o processo de inserção, remoção e alteração de documentos na coleção ALUNOS.
    - [contole_emprestimos.py](src/controle/controle_emprestimos.py): Classe responsável por controlar o processo de inserção, remoção e alteração de rdocumentos na coleção EMPRESTIMOS.
    - [controle_livros.py](src/controle/controle_livros.py): Classe responsável por controla o processo de inserção, remoção e alteração de documentos na coleção LIVROS.
  * [entidades](src/entidades): Direstório onde estão contidas as classes que representam as entidades descritas no [diagrama relacional](Diagrama/DIAGRAMA_RELACIONAL_SISTEMA_BIBLIOTECA_ESCOLAR.pdf).
    - [alunos.py](src/entidades/alunos.py): Classe responsável por representar a colecao ALUNOS com seus campos e tipos condizentes com o diagrama relacional
    - [emprestimos.py](src/entidades/emprestimos.py): Classe responsável por representar a colecao EMPRESTIMOS com seus campos e tipos condizentes com o diagrama relacional
    - [livros.py](src/entidades/livros.py): Classe responsável por representar a colecao LIVROS com seus campos e tipos condizentes com o diagrama relacional
  * [relatorio](src/relatorio): Diretório onde está contida a classe responsável por controlar e realizar os relatórios do sistema.
    - [relatorio.py](src/relatorio/relatorio.py): Classe responsável por realizar as consultas no banco de dados para geração de relatório e exibir o DataFrame Pandas gerado a partir da consulta. 
  * [utilitarios](src/utilitarios): Diretórios onde estão contidas as classes responsáveis pela criação da Splash Screen e Menus exibidos ao decorrer do funcionamento do sistema.
    - [menus.py](src/utilitarios/menus.py): Classe responsável por conter os menus utilizados no sistema.
    - [splash_screen.py](src/utilitarios/splash_screen.py): Classe responsável por gerar a tela 'Splash Screen' contendo informações como os integrante do projeto, quantidade de documentos de cada coleção, disciplina do projeto, professor da disciplina e semestre da disciplina
  * [bibliotecas.txt](src/bibliotecas.txt): Arquivo de texto contendo as bibliotecas e suas respectivas versões utilizadas para o funcionamento do sistema.
  * [criar_tabelas_registros.py](src/criar_tabelas_registros.py): Script Python responsável pela criação das tabelas com seus relacionamentos, além de registros de exemplos.
  * [criar_colecoes_documentos.py](src/criar_colecoes_documentos.py): Script Python responsável pela criação das colecoes com seus relacionamentos, além de documentos de exemplos.
  * [principal.py](src/principal.py): Script python responsável por ser a interface entre o usuário e os módulos de acesso ao Banco de Dados MongoDB. Deve ser executado após a criação das tabelas e coleções.
