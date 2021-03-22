#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==============================================================================
# LOAD CSV TO SQLITE
# ==============================================================================
# Created by: laercio.serra@gmail.com
# Created at: 20/03/2021
# ==============================================================================

# Defining the libraries
import os
import sys

import pandas as pd
from sqlalchemy import create_engine

# Defining parameters
path = '/Users/lserra/PyProjects/challenge_suzano'
inputfile = path + "/input/"
dbfile = "/db/suzano.db"


def connecting_database():
    """Creating and returning the engine with sqlite database"""
    try:
        engine = create_engine(
            'sqlite:///{}{}'.format(path, dbfile),
            echo=False
        )
        return engine
    except Exception as error:
        print(">> Something wrong with the system!")
        print(f">> Error: {error}")


def sql_create_big_table():
    """Retunrs the SQL command to create the table into the database"""
    return """
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
    """


def loading_data_to_sqlite(list_files):
    """Saving all the data into the sqlite database"""
    engine = connecting_database()
    if engine is None:
        return False

    print()
    print("-".rjust(60, "-"))
    print("Loading data".center(60))
    print("-".rjust(60, "-"))

    for filename in list_files:
        name, ext = os.path.splitext(filename)
        if ext != '.csv':
            print(">> WARNING: CSV file invalid!")
            return False

        print(f">> Populating the table: rd_{name}")
        df = pd.read_csv(path + inputfile + filename, sep=',', header=0)
        df.to_sql(f"rd_{name}", con=engine, index=False, if_exists='replace')
        print("-".rjust(60, "-"))

    return True


def creating_big_table():
    """
    Creating the big table
    """
    engine = connecting_database()
    if engine is None:
        return False

    sql = sql_create_big_table()
    engine = connecting_database()
    print(">> Creating the table: bt_challenge_suzano")
    df = pd.read_sql(sql=sql, con=engine)
    df.to_sql(
        "bt_challenge_suzano", con=engine, index=False, if_exists='replace'
    )

    return True


def execute(list_files):
    """Execute all process"""
    result = loading_data_to_sqlite(list_files=list_files)
    if not result:
        print("\n>> Something went wrong!")
        sys.exit(1)

    result = creating_big_table()
    if not result:
        print("\n>> Something went wrong!")
        sys.exit(1)

    print("\n>> Process finished successfully!")


if __name__ == "__main__":
    files = os.listdir(path + inputfile)
    execute(files)
