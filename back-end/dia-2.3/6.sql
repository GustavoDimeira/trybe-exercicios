USE PecasFornecedores;
SELECT * FROM Fornecimentos
WHERE Preco between 15 AND 40
ORDER BY Preco DESC
;

# Fornecimentos cuja o preço é maior que 15 e menor que 40, ordenados de forma decrescente.