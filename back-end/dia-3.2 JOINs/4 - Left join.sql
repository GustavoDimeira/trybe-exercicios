USE Pixar;

SELECT m.*, t.* FROM Movies m
LEFT JOIN Theater t
ON m.theater_id = t.id
ORDER BY m.title ASC
;

/*
Exercício 4: Utilizando o LEFT JOIN, faça uma busca que retorne todos os dados dos
cinemas, mesmo os que não possuem filmes em cartaz e, adicionalmente, os dados dos
filmes que estão em cartaz nestes cinemas. Retorne os nomes dos cinemas em ordem alfabética.
*/