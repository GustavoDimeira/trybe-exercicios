USE hr;
UPDATE employees
SET phone_number = REPLACE(phone_number, '515', '777')
WHERE LEFT(phone_number, 3) = '515' 
;

SELECT * FROM employees;

SET SQL_SAFE_UPDATES = 0 ;

/*
SUBSTRING → pega uma quantia (definida no 3 par.)
de letras da string no 1 par. a partir do index (definido no 2 par.)

Escreva uma query que atualize a coluna PHONE_NUMBER,
de modo que todos os telefones iniciados por 515
agora devem iniciar com 777.

UPDATE nome_da_tabela
SET chave1 = 'novoValor1’, chave2 = ‘novoValor2’
WHERE alguma_condicao; -- importantíssimo aplicar o WHERE para não alterar a tabela inteira!
*/