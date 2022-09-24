# vejo aonde a chave esta sendo usada

DELETE FROM Pixar.Movies
WHERE id = 11;

# deleto as colunas que a usam

SELECT * FROM Pixar.BoxOffice;
DELETE FROM Pixar.BoxOffice
WHERE id = 11;

# tento novamente deletar a chave

DELETE FROM Pixar.Movies
WHERE id = 11;

# Exercício 6: Exclua da tabela Movies o filme “WALL-E”.