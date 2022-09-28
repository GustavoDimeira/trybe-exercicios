# vejo os Movies que ele fez, e seus id's

SELECT id FROM Movies
WHERE director = 'Andrew Staton';

# removo esses movies da tabela BoxOffice

DELETE FROM BoxOffice
WHERE movie_id IN (2, 9);

# por fim, consigo remover o diretor da tabela movies

DELETE FROM Movies
WHERE director = 'Andrew Staton';

# Exercício 7: Exclua da tabela Movies todos os filmes dirigidos por “Andrew Staton”.
