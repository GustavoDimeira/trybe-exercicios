USE PecasFornecedores;
SELECT * FROM Vendas
WHERE DATE(order_date) between DATE('2018-04-15') AND DATE('2019-07-30')
ORDER BY DATE(order_date) DESC
;

/* 
	vendas feitas dentro das duas datas, ordenadas pela da mais recente para a mais antiga
 */