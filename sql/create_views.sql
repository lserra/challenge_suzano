SELECT * FROM bt_concorrentes bc 
SELECT * FROM agg_fluxo_eventos afe 

DROP VIEW IF EXISTS vw_fluxo_medio
CREATE VIEW vw_fluxo_medio AS 
SELECT 
	bc.cod_concorrente 
	, bc.nome_concorrente 
	, bc.end_concorrente 
	, bc.bairro_concorrente 
	, bc.preco_praticado 
	, bc.populacao 
	, bc.densidade 
	, afe.num_dia_semana_evento 
	, afe.nome_dia_semana_evento 
	, afe.periodo_evento 
	, afe.fluxo_medio	
FROM 
	bt_concorrentes bc INNER JOIN agg_fluxo_eventos afe 
	ON bc.cod_concorrente  = afe.cod_concorrente
ORDER BY 
	bc.cod_concorrente
	, afe.num_dia_semana_evento 
	
SELECT * FROM vw_fluxo_medio vfm

DROP VIEW IF EXISTS vw_concorrentes
CREATE VIEW vw_concorrentes AS 
SELECT DISTINCT 
	bc.cod_concorrente 
FROM 
	bt_concorrentes bc
	
SELECT * FROM vw_concorrentes vc