# SISTEMA DE BIBLIOTECA ESCOLAR EM PYTHON
O sistema presente nesse repositório representa um sistema de emprestimo de livros utilizado por uma biblioteca escolar, composto por um conjunto de tabelas que para representar os emprestimos, sendo elas: __Livros, Alunos e Emprestimos__

## PREPARANDO PARA UTILIZAÇÃO DO SISTEMA

Primeiramente, para funcionamento do sistema, é necessário a instalação de certas bibliotecas através da utilização de um [arquivo que contém as bibliotecas e suas respectivas versões](src/bibliotecas.txt):
``` shell
pip install -r bibliotecas.txt 
```

O sistema produzido exige que as tabelas já existam, portanto antes de rodar o programa principal, é necessário a execução do seguinte script em Python:

``` shell
~$ python criar_tabelas_registros.py
```

## INICIANDO O SISTEMA 

Tendo executado o script anteriormente mencionado e finalizado a criação das tabelas, junto com os registros de exemplo, basta executar o script principal do sistema:

``` shell
~$ python principal.py
```
Para uma explicação prática do funcionamento do sistema, acesse o vídeo gravado pelos componentes:
- [Video](https://youtu.be/B0yFLeq7exc)

## ORGANIZAÇÃO REPOSITÓRIO

- [Diagrama](Diagrama): Nesse diretório está contido o [diagrama relacional](Diagrama/DIAGRAMA_RELACIONAL_SISTEMA_BIBLIOTECA_ESCOLAR.pdf) do sistema, com suas entidades e relacionamentos.
  * As entidades representadas no diagrama são: ALUNOS, EMPRESTIMOS E LIVROS
- [sql_tabelas](sql_tabelas): Nesse diretório estão contidos os scripts SQL responsáveis pela criação das tabelas do sistema e da inserção de registros fictícios nessas tabelas.
  * [criar_tabelas_biblioteca_escolar.sql](sql_tabelas/criar_tabelas_biblioteca_escolar.sql): Script SQL responsável pela criação das tabelas utilizadas no sistema, tal como os seus relacionamentos;
  *  [inserir_dados_tabelas_biblioteca_escolar.sql](sql_tabelas/inserir_dados_tabelas_biblioteca_escolar.sql): Script SQL responsável por inserir registros de exemplos nas tabelas do sistemas.
- [src](src): Nesse diretório estão guardados os scripts responsáveis pelo funcionamento do sistema
  * [conexao_bd](src/conexao_bd) - Nesse diretório está guardada a classe responsável por realizar a conexão do sistema com o banco de dados mySQL, tal como um arquivo responsável por guardar dados úteis para autentificação do usuário
    - [mySQL_queries.py](src/conexao_bd/mySQL_queries.py) - Classe responsável por realizar a conexão com o banco de dados, também realizando os comandos DML(como inserção, alteração ou exclusão de registros) e DDL(como a criação, alteração ou exclusão de tabelas), além das querys para os relatórios.
       + Exemplo da sua utilização para uma consulta simples:
         ``` python
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
         ```
    - [autenticador_mySQL.](src/conexao_bd/autenticador/autenticador_mySQL.txt) - Arquivo contendo informações para conexão com o banco de dados, sendo respectivamente o nome do banco de dados, o usuário do banco de dados e a senha do banco de dados.
  * [controle](src/controle): Diretório onde estão contidas as classes responsáveis por controlar as operações de inserção, alteração e exclusão de cada tabela.
    - [controle_alunos.py](src/controle/controle_alunos.py): Classe responsável por controlar o processo de inserção, remoção e alteração de registros na tabela ALUNOS.
    - [contole_emprestimos.py](src/controle/controle_emprestimos.py): Classe responsável por controlar o processo de inserção, remoção e alteração de registros na tabela EMPRESTIMOS.
    - [controle_livros.py](src/controle/controle_livros.py): Classe responsável por controla o processo de inserção, remoção e alteração de registros na tabela LIVROS.
  * [entidades](src/entidades): Direstório onde estão contidas as classes que representam as entidades descritas no [diagrama relacional](Diagrama/DIAGRAMA_RELACIONAL_SISTEMA_BIBLIOTECA_ESCOLAR.pdf).
    - [alunos.py](src/entidades/alunos.py): Classe responsável por representar a entidade ALUNOS com seus campos e tipos condizentes com o diagrama relacional
    - [emprestimos.py](src/entidades/emprestimos.py): Classe responsável por representar a entidade EMPRESTIMOS com seus campos e tipos condizentes com o diagrama relacional
    - [livros.py](src/entidades/livros.py): Classe responsável por representar a entidade LIVROS com seus campos e tipos condizentes com o diagrama relacional
  * [relatorio](src/relatorio): Diretório onde está contida a classe responsável por controlar e realizar os relatórios do sistema.
    - [relatorio.py](src/relatorio/relatorio.py): Classe responsável por realizar os scripts SQL para geração de relatório e exibir o DataFrame Pandas gerado a partir da consulta. 
  * [sql_relatorios](src/sql_relatorios): Diretório onde estão contidos os scripts SQL que geram as consultas exibidas nos relatórios.
    - [relatorio_alunos_devedores.sql](src/sql_relatorios/relatorio_alunos_devedores.sql): Script SQL responsável por realizar a consulta de alunos que devem pagar multa por 1 ou mais emprestimos atrasados.
    - [relatorio_alunos_quantidade_emprestimos.sql](src/sql_relatorios/relatorio_alunos_quantidade_emprestimos.sql): Script SQL responsável por realizar a consulta da quantidade de emprestimos realizados por alunos que já pegaram emprestado algum livro.
    - [relatorio_de_alunos_cadastrados.sql](src/sql_relatorios/relatorio_de_alunos_cadastrados.sql): Script SQL responsável por realizar a consulta de alunos registrados.
    - [relatorio_de_emprestimos_atrasados](src/sql_relatorios/relatorio_de_emprestimos_atrasados.sql): Script SQL responsável por realizar a consulta de emprestimos registrados que estão atrasados.
    - [relatorio_de_emprestimos_cadastrados.sql](src/sql_relatorios/relatorio_de_emprestimos_cadastrados.sql): Script SQL responsável por realizar a consulta de emprestimos registrados.
    - [relatorio_de_estoque_livros_emprestados.sql](src/sql_relatorios/relatorio_de_estoque_livros_emprestados.sql): Script SQL responsável por realizar a consulta do estoque restante dos livros que estão emprestados.
    - [relatorio_de_livros_acervos.sql](src/sql_relatorios/relatorio_de_livros_acervos.sql): Script SQL responsável por realizar aconsulta dos livros registrados.
  * [utilitarios](src/utilitarios): Diretórios onde estão contidas as classes responsáveis pela criação da Splash Screen e Menus exibidos ao decorrer do funcionamento do sistema.
    - [menus.py](src/utilitarios/menus.py): Classe responsável por conter os menus utilizados no sistema.
    - [splash_screen.py](src/utilitarios/splash_screen.py): Classe responsável por gerar a tela 'Splash Screen' contendo informações como os integrante do projeto, quantidade de registros de cada tabela, disciplina do projeto, professor da disciplina e semestre da disciplina
  * [bibliotecas.txt](src/bibliotecas.txt): Arquivo de texto contendo as bibliotecas e suas respectivas versões utilizadas para o funcionamento do sistema.
  * [criar_tabelas_registros.py](src/criar_tabelas_registros.py): Script Python responsável pela criação das tabelas com seus relacionamentos, além de registros de exemplos.
  * [principal.py](src/principal.py): Script python responsável por ser a interface entre o usuário e os módulos de acesso ao Banco de Dados. Deve ser executado após a criação das tabelas.
