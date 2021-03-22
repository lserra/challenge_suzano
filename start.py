#!/usr/bin/python3
# -*- coding: utf-8 -*-

import click
from src import gerar_json as gj


@click.command()
@click.option('--cod_concorrente',
              prompt='Enter the Codigo Concorente',
              help='Codigo Concorrente to search and generate JSON file.')
def run(cod_concorrente):
    """Running the main tasks of the app"""
    print("*".rjust(100, '*'))
    print(" S U Z A N O ".center(100, '*'))
    print("*".rjust(100, '*'))

    if gj.submitting_query(cod_concorrente):
        gj.save_json_file(cod_concorrente)
    else:
        print("----> Code not found!")

    print("----> Process finished successfully!")


if __name__ == '__main__':
    run()
