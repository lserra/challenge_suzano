DROP TABLE IF EXISTS bt_concorrentes
CREATE TABLE bt_concorrentes AS
SELECT 
	  rc.codigo AS cod_concorrente
	, rc.nome AS nome_concorrente
	, rc.endereco  AS end_concorrente
	, rc.faixa_preco  AS preco_praticado
	, rb.nome AS bairro_concorrente
	, rp.populacao AS populacao
	, rb.area AS area
	, (populacao/area) AS densidade
FROM 
	rd_concorrentes rc INNER JOIN rd_bairros rb 
	ON rc.codigo_bairro = rb.codigo 
	
	INNER JOIN rd_populacao rp 
	ON rp.codigo = rb.codigo

SELECT * FROM bt_concorrentes bc 

DROP TABLE IF EXISTS bt_fluxo_eventos
CREATE TABLE bt_fluxo_eventos AS
SELECT 
	  redf.codigo_concorrente AS cod_concorrente 
	, strftime('%Y-%m-%d %H:%M:%S', redf."datetime") AS evento
	, strftime('%Y-%m-%d', redf."datetime") AS data_evento
	, strftime('%H:%M:%S', redf."datetime") AS tempo_evento
	, CAST(strftime('%Y', redf."datetime") AS integer) AS ano_evento
	, CAST(strftime('%m', redf."datetime") AS integer) AS mes_evento
	, CAST(strftime('%d', redf."datetime") AS integer) AS dia_evento
	, CAST(strftime('%H', redf."datetime") AS integer) AS hora_evento
	, CAST(strftime('%W', redf."datetime") AS integer) AS semana_evento
	, CAST(strftime('%w', redf."datetime") AS integer) AS num_dia_semana_evento
	, CASE 
		WHEN CAST(strftime('%w', redf."datetime") AS integer) == 0 THEN "domingo"
		WHEN CAST(strftime('%w', redf."datetime") AS integer) == 1 THEN "segunda-feira"
		WHEN CAST(strftime('%w', redf."datetime") AS integer) == 2 THEN "terça-feira"
		WHEN CAST(strftime('%w', redf."datetime") AS integer) == 3 THEN "quarta-feira"
		WHEN CAST(strftime('%w', redf."datetime") AS integer) == 4 THEN "quinta-feira"
		WHEN CAST(strftime('%w', redf."datetime") AS integer) == 5 THEN "sexta-feira"
		WHEN CAST(strftime('%w', redf."datetime") AS integer) == 6 THEN "sábado"
	END AS nome_dia_semana_evento
	, CASE 
		WHEN CAST(strftime('%H', redf."datetime") AS integer) >= 00 AND CAST(strftime('%H', redf."datetime") AS integer) <= 11 THEN "manhã"
     	WHEN CAST(strftime('%H', redf."datetime") AS integer) >= 12 AND CAST(strftime('%H', redf."datetime") AS integer) <= 17 THEN "tarde"
	 	WHEN CAST(strftime('%H', redf."datetime") AS integer) >= 18 AND CAST(strftime('%H', redf."datetime") AS integer) <= 23 THEN "noite"
	END AS periodo_evento
FROM rd_eventos_de_fluxo redf 

SELECT * FROM bt_fluxo_eventos bfe 
