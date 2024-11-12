with livros_emprestimos as (
	select codigo_livro ,
    count(codigo_livro) as qtd_emprestado
    from EMPRESTIMOS
    group by codigo_livro
    order by codigo_livro
)
select l.id as 'ID',
	l.nome_obra as 'Nome da Obra',
    l.autor as 'Autor da Obra',
    l.editora_edicao as 'Editora da Edicao',
    l.numero_edicao as 'Numero da Edicao',
    l.quantidade_exemplares as 'Quantidade Total',
    le.qtd_emprestado as 'Quantidade Emprestada',
    (l.quantidade_exemplares - le.qtd_emprestado) as 'Quantidade Disponivel'
    from LIVROS l 
    inner join livros_emprestimos le on l.id = le.codigo_livro
    order by nome_obra, autor;