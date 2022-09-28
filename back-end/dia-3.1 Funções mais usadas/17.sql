USE hr;
SELECT first_name, last_name, DATEDIFF(now(), hire_date) AS 'Dias na empresa' FROM  employees

/*
 Escreva uma query que exiba as seguintes informações
 de cada funcionário: nome, sobrenome, tempo
 que trabalha na empresa (em dias).
*/