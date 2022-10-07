USE Pixar;

SELECT m.*, t.* FROM Theater t
RIGHT JOIN Movies m
ON m.theater_id = t.id
ORDER BY m.title ASC
;

/*
Exercício 5: Utilizando o RIGHT JOIN, faça uma busca que retorne todos os dados dos
filmes, mesmo os que não estão em cartaz e, adicionalmente, os dados dos cinemas que
possuem estes filmes em cartaz. Retorne os nomes dos cinemas em ordem alfabética.
*/