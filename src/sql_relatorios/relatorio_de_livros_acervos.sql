select id as 'ID',
	nome_obra as 'Nome da Obra',
    autor as 'Autor da Obra',
    editora_edicao as 'Editora da Edicao',
    numero_edicao as 'Numero da Edicao',
    ano_edicao as 'Ano da Edicao',
    quantidade_exemplares as 'Quantidade de Exemplares'
    from LIVROS order by nome_obra, autor;