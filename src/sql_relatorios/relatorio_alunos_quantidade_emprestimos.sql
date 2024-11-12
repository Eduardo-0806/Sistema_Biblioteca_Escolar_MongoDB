select a.matricula as 'Matricula Aluno',
a.nome as 'Nome',
count(e.codigo_aluno) as 'Quantidade de Emprestimos'
from ALUNOS a 
inner join EMPRESTIMOS e on e.codigo_aluno = a.matricula
group by e.codigo_aluno
order by count(e.codigo_aluno) Desc;