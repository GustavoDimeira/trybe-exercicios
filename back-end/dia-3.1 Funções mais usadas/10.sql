USE hr;
SELECT ROUND(AVG(salary), 2), COUNT(employee_id) FROM employees
GROUP BY DEPARTMENT_ID
; 
 
 /*
 Escreva um query que exiba média salarial e o número de
 funcionários de todos os departamentos com mais de dez
 funcionários. Dica: agrupe pelo DEPARTMENT_ID
 */