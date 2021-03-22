#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
# SUBMIT QUERY AND GENERATE JSON FILE
# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 20/03/2021
# ==============================================================================

# Defining the libraries
import json
import sys

import pandas as pd
from sqlalchemy import create_engine

from src.transformers import dados_cadastrais as dc
from src.transformers import fluxo_medio as fm

path = '/Users/lserra/PyProjects/challenge_suzano'
inputpath = path + "/input/"
jsonpath = path + "/output/json/"
dbpath = "/db/suzano.db"


def connecting_database():
    """Creating and returning the engine with sqlite database"""
    try:
        engine = create_engine(
            'sqlite:///{}{}'.format(path, dbpath),
            echo=False
        )
        return engine
    except Exception as error:
        print("----> Something wrong with the system!")
        print(f"----> Error: {error}")
        sys.exit(1)


def submitting_query(cod_concorrente):
    """Submitting the query and retrning the results in dataframe"""

    sql = """
    SELECT * FROM vw_concorrentes WHERE cod_concorrente = '{}'
    """.format(cod_concorrente)

    engine = connecting_database()

    print("----> Searching for the code in database . . .")
    df = pd.read_sql(sql=sql, con=engine)

    if len(df) > 0:
        return True
    else:
        return False


def sql_fluxo_medio(cod_concorrente):
    return """
    SELECT 
        vfm.cod_concorrente,
        vfm.num_dia_semana_evento,
        vfm.nome_dia_semana_evento,
        vfm.periodo_evento,
        vfm.fluxo_medio
    FROM vw_fluxo_medio vfm 
    WHERE cod_concorrente = '{}'
    """.format(cod_concorrente)


def sql_dados_cadastrais(cod_concorrente):
    return """
    SELECT DISTINCT 
        vfm.cod_concorrente ,
        vfm.nome_concorrente ,
        vfm.end_concorrente ,
        vfm.bairro_concorrente ,
        vfm.preco_praticado ,
        vfm.populacao ,
        vfm.densidade 
    FROM vw_fluxo_medio vfm 
    WHERE cod_concorrente = '{}'
    """.format(cod_concorrente)


def save_json_file(cod_concorrente):
    """Save the results into the JSON file: (/output/json)"""

    engine = connecting_database()
    connection = engine.connect()

    result_fluxo_medio = connection.execute(sql_fluxo_medio(cod_concorrente))
    json_string_fluxo_medio = fm.parser_json_string_fluxo_medio(
        result_fluxo_medio
    )

    result_dados_cadastrais = connection.execute(
        sql_dados_cadastrais(cod_concorrente)
    )
    json_string = dc.parser_json_string_dados_cadastrais(
        json_string_fluxo_medio, result_dados_cadastrais
    )
    connection.close()

    print("----> Generating JSON file . . .")
    jsonfile = jsonpath + "{}.json".format(cod_concorrente)
    with open(jsonfile, 'w') as jsonfile:
        json.dump(json_string, jsonfile, indent=4, ensure_ascii=False)
