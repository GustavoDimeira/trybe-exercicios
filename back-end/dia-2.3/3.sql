USE PecasFornecedores;
SELECT peca, Preco, Fornecedor FROM Fornecimentos
WHERE Fornecedor LIKE '%N%'
;

# Peças, Preço e Fornecedores que possuam a letra 'N' na coluna fornecedor