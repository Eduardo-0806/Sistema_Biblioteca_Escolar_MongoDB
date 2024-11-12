with alunos_devedores as (
	select codigo_aluno,
    count(codigo_aluno) as quantidade,
    sum((datediff(curdate(), data_devolucao) * 1.50)) as valor_multa
    from EMPRESTIMOS 
	where data_devolucao < curdate()
    group by codigo_aluno
    )
	
select Distinct e.codigo_aluno as "Matricula Aluno",
	a.nome as "Nome Aluno",
	a.email as "Email Aluno",
	ad.quantidade as 'Quantidade de Livros Atrasados',
	ad.valor_multa as 'Valor Total de Multa(R$)'
	from EMPRESTIMOS e
	inner join ALUNOS a on e.codigo_aluno = a.matricula
	inner join alunos_devedores ad on e.codigo_aluno = ad.codigo_aluno
	where data_devolucao < curdate() and ad.codigo_aluno = e.codigo_aluno
	order by a.nome
    