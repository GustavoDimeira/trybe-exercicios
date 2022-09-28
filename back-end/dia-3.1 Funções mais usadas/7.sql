USE hr;
SELECT SUM(salary), job_id FROM employees
GROUP BY job_id
;
 /*
 Escreva uma query que exiba a quantidade de dinheiro necessária
 para efetuar o pagamento de cada profissão (JOB_ID).
 */