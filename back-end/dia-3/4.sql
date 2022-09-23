USE PecasFornecedores;
SELECT * FROM Fornecedores
WHERE name LIKE '%LTDA%'
ORDER BY name DESC
;

# Ordenar a tabela Fornecedores que possuem a palavra LTDA no name, e ordenar os resultado por ordem decrescente
