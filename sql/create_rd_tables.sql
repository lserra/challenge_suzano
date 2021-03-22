-- bairros definition
CREATE TABLE "bairros" (
	codigo VARCHAR,
	nome VARCHAR,
	municipio VARCHAR,
	uf VARCHAR,
	area REAL
);

-- concorrentes definition
CREATE TABLE "concorrentes" (
	codigo VARCHAR,
	nome VARCHAR,
	categoria VARCHAR,
	faixa_preco INTEGER,
	endereco VARCHAR,
	municipio VARCHAR,
	uf VARCHAR,
	codigo_bairro VARCHAR
);

-- eventos_de_fluxo definition
CREATE TABLE "eventos_de_fluxo" (
	codigo VARCHAR,
	datetime VARCHAR,
	codigo_concorrente VARCHAR
);

-- populacao definition
CREATE TABLE "populacao" (
	codigo VARCHAR,
	populacao INTEGER
);