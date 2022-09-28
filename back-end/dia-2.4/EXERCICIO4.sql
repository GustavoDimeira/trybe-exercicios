SELECT * FROM Pixar.Movies;

UPDATE Pixar.Movies
SET title = 'Procurando Nemo', year = 2003
WHERE id = 9
;

/*
 Exercício 4: O título do filme “Ratatouille” está incorreto
 na tabela Movies. Além disso, o filme foi lançado em 2007
 e não em 2010. Corrija esses dados utilizando o comando UPDATE.
*/