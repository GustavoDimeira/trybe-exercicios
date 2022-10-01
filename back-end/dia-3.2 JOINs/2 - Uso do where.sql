USE Pixar;

SELECT m.title, b.international_sales, b.domestic_sales FROM BoxOffice b
INNER JOIN Movies m
ON m.id = b.movie_id
WHERE b.international_sales > b.domestic_sales
;

/*
Exercício 2: Utilizando o INNER JOIN, faça uma busca que retorne o
número de vendas para cada filme que possui um número maior de vendas
internacionais (international_sales) do que vendas nacionais (domestic_sales).
*/