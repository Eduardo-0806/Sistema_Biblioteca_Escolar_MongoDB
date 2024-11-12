/*Inseres dados na tabela LIVROS*/

insert into LIVROS value (1, 'A Divina Comedia', 'Dante Alighieri', 'Editora 34', 4, 2018, 6);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'O Ateneu', 'Raul Pompeia', 'Martin Claret', 4, 2017, 4);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'Anna Karienina', 'Lev Tolstoi', 'Editora 34', 1, 2021, 3);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'O Morro dos Ventos Uivantes', 'Emily Bronte', 'Principis', 1, 2019, 2);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'O Morro dos Ventos Uivantes', 'Emily Bronte', 'Darkside', 1, 2020, 4);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'Os Irmaos Karamazov', 'Fiodor Dostoievsk', 'Editora 34', 2, 2019, 1);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'Os Miseraveis', 'Victor Hugo', 'Penguin Livros', 1, 2017, 3);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'Os Miseraveis', 'Victor Hugo', 'Martin Claret', 1, 2020, 4);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'Memorias postumas de Bras Cubas', 'Machado de Assis', 'Editora Antofagica', 1, 2019, 7);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'Triste Fim de Policarpo Quaresma', 'Lima Barreto', 'Martin Claret', 5, 2011, 3);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'Confissoes', 'Santo Agostinho', 'Pandorga Editora', 1, 2022, 4);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'O Banquete', 'Platao', 'Edipro', 1, 2012, 5);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'Etica a Nicomaco', 'Aristoteles', 'Principis', 1, 2021, 3);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'A Arte da Guerra', 'Sun Tzu', 'Editora Garnier', 1, 2023, 4);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), 'O Senhor dos Aneis', 'J.R.R. Tolkien', 'HarperCollins', 1, 2019, 1);
insert into LIVROS values((select (max(id) + 1) from LIVROS l), '50 Sonetos de Shakespeare', 'William Shakespeare', 'Nova Fronteira', 1, 2015, 5);

/*Inseres dados na tabela ALUNOS*/

insert into ALUNOS values(23110101, 'Rodolfo Santos', 'rodolfosanto@hotmail.com');
Insert into ALUNOS values(40020914, 'Joao Vitor Shneider', 'JVShneider66@gmail.com');
Insert into ALUNOS values(30367117, 'Antonio Amorim', 'Amorim@gmail.com');
Insert into ALUNOS values(29447899, 'Maria Eduarda Pereira', 'Pereira@hotmail.com');
Insert into ALUNOS values(12439076, 'Allan Ferreira da Silva', 'alanferreira@gmail.com');
Insert into ALUNOS values(40040321, 'Ana Clara Claudino da Silva Almeida', 'hannax@gmail.com');
Insert into ALUNOS values(19845344, 'Davi Candal Lopes', 'DaviCL@hotmail.com');
Insert into ALUNOS values(23086905, 'Talita Candal Lopes ', 'tatalopes@hotmail.com');
Insert into ALUNOS values(19791509, 'Flavia Lopes Ribeiro ', 'flaviaribeiro@gmail.com');
Insert into ALUNOS values(25000806, 'Carlos Eduardo Malaquias ', 'carlosEM@gmail.com');
Insert into ALUNOS values(21761909, 'Marcelo Freitas ', 'MF@hotmail.com');
Insert into ALUNOS values(23967788, 'Tania Guilherme ', 'GullhermeTania@hotmail.com');
Insert into ALUNOS values(22634544, 'Vinivius Souza', 'viniciusSO@gmail.com');

/*Inseres dados na tabela EMPRESTIMOS*/

insert into EMPRESTIMOS values(1, 1, 23110101, '2024-10-25');
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 14, 40020914, '2024-10-18' );
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 15, 40020914, '2024-10-08' );
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 16, 40040321, '2024-10-16' );
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 10, 19845344, '2024-10-14' );
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 16, 19845344, '2024-10-17' );
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 3, 19845344, '2024-10-07' );
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 5, 25000806, '2024-10-22' );
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 8, 25000806, '2024-11-03' );
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 13, 25000806, '2024-10-24' );
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 12, 23967788, '2024-10-26' );
insert into EMPRESTIMOS values((select (max(codigo) + 1) from EMPRESTIMOS e), 2, 22634544, '2024-10-29' );