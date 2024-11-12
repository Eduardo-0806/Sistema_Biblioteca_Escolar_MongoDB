select e.codigo as 'Codigo Emprestimo',
	e.codigo_livro as 'ID Livro',
    l.nome_obra as 'Nome da Obra',
    e.codigo_aluno as 'Matricula Aluno',
    a.nome as 'Nome Aluno',
    a.email as 'Email do Aluno',
    e.data_devolucao as 'Data de Devolucao',
    (datediff(curdate(), e.data_devolucao) * 1.50) as "Valor Multa(R$1,50 por dia)"
    from EMPRESTIMOS e 
    inner join LIVROS l on e.codigo_livro = l.id
    inner join ALUNOS a on e.codigo_aluno = a.matricula
    where e.data_devolucao < curdate()
    order by e.codigo;