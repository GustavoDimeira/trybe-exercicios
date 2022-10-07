USE Pixar;
SELECT m.title, b.domestic_sales, b.international_sales FROM BoxOffice b
INNER JOIN Movies m
ON m.id = b.movie_id
;

SELECT * FROM BoxOffice;
SELECT * FROM Movies;

/*
	Utilizando o INNER JOIN, encontre as vendas nacionais(domestic_sales)
	e internacionais (international_sales) de cada filme.
*/