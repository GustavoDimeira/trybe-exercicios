USE Pixar;

SELECT title, rating FROM Movies Movies
INNER JOIN BoxOffice b
ON movie_id = id
ORDER BY rating DESC
;

/*
Exercício 3: Utilizando o INNER JOIN, faça uma busca que retorne
os filmes e sua avaliação (rating) em ordem decrescente.
*/