select e.codigo as 'Codigo Emprestimo',
	e.codigo_livro as 'ID Livro',
    l.nome_obra as 'Nome da Obra',
    l.editora_edicao as 'Editora da Edicao',
    l.numero_edicao as 'Numero da Edicao',
    e.codigo_aluno as 'Matricula Aluno',
    a.nome as 'Nome Aluno',
    a.email as 'Email do Aluno',
    e.data_devolucao as 'Data de Devolucao'
    from EMPRESTIMOS e 
    inner join LIVROS l on e.codigo_livro = l.id
    inner join ALUNOS a on e.codigo_aluno = a.matricula
    order by e.codigo;