#!/usr/bin/python3
# -*- coding: utf-8 -*-


def parser_json_string_dados_cadastrais(json_string, result):
    """Convert Python objects into JSON strings"""
    for row in result:
        json_string_dados_cadastrais = {
            "cod_concorrente": str(row['cod_concorrente']),
            "nome_concorrente": str(row['nome_concorrente']),
            "endereço": str(row['end_concorrente']),
            "preco_praticado": str(row['bairro_concorrente']),
            "bairro": str(row['preco_praticado']),
            "população": int(row['populacao']),
            "densidade": int(row['densidade']),
            "fluxo_medio": json_string
        }

    return json_string_dados_cadastrais
