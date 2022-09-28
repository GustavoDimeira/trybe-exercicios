USE hr;
SELECT MAX(salary) AS 'Maior', MIN(salary) AS 'Menor',
SUM(salary) AS 'Soma', AVG(salary) AS 'Média' FROM employees;

/*
Escreva uma query que exiba quatro informações:
o maior salário, o menor salário, a soma de todos
os salários e a média dos salários. Todos os valores
devem ser formatados para ter apenas duas casas decimais.
*/