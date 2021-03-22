SELECT * FROM bt_fluxo_eventos bfe 

DROP TABLE IF EXISTS agg_fluxo_eventos
CREATE TABLE agg_fluxo_eventos AS 
SELECT
      bfe.cod_concorrente AS cod_concorrente 
    , bfe.num_dia_semana_evento AS num_dia_semana_evento 
	, bfe.nome_dia_semana_evento AS nome_dia_semana_evento 
	, bfe.periodo_evento AS periodo_evento 
	, count(bfe.cod_concorrente) AS fluxo_medio
FROM 
	bt_fluxo_eventos bfe
GROUP BY
	  bfe.cod_concorrente 
	, bfe.num_dia_semana_evento 
	, bfe.nome_dia_semana_evento
	, bfe.periodo_evento
ORDER BY 1, 2, 3

SELECT * FROM agg_fluxo_eventos afe 