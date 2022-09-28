USE hr;
SELECT job_id, AVG(salary) AS 'A' FROM employees
GROUP BY job_id
ORDER BY AVG('A')
;
