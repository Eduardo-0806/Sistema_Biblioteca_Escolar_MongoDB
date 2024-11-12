
/*Realiza o drop das chaves estrangeiras*/

alter table EMPRESTIMOS drop foreign key ALUNOS_EMPRESTIMOS_FK;
alter table EMPRESTIMOS drop foreign key LIVROS_EMPRESTIMOS_FK;

/*Realiza o drop das tabelas*/

drop table EMPRESTIMOS;
drop table LIVROS;
drop table ALUNOS;

/*Realiza a criacao das tabelas e de seu campos*/

create table LIVROS (
    id integer not null,
    nome_obra varchar(150) not null,
    autor varchar(100) not null,
    editora_edicao varchar(100) not null,
    numero_edicao integer not null,
    ano_edicao year not null,
    quantidade_exemplares integer not null,
    constraint LIVROS_PK primary key (id)
);

create table ALUNOS (
matricula integer not null,
nome varchar(100) not null,
email varchar(150) not null,
constraint ALUNOS_PK primary key (matricula)
);

create table EMPRESTIMOS (
codigo integer not null,
codigo_livro integer not null,
codigo_aluno integer not null,
data_devolucao date,
constraint EMPRESTIMOS_PK primary key (codigo)
);

/*Realiza a alteracao nas tabelas para adicionar as chaves estrangeiras*/

alter table EMPRESTIMOS add constraint LIVROS_EMPRESTIMOS_FK foreign key (codigo_livro) references LIVROS (id);
alter table EMPRESTIMOS add constraint ALUNOS_EMPRESTIMOS_FK foreign key (codigo_aluno) references ALUNOS (matricula);