#!/usr/bin/python3
# -*- coding: utf-8 -*-

seg = dict()
ter = dict()
qua = dict()
qui = dict()
sex = dict()
sab = dict()
dom = dict()


def fluxo_medio(result):
    """Convert Python objects into JSON strings"""
    for row in result:
        if row['num_dia_semana_evento'] == 1:
            if row['periodo_evento'] == 'manhã':
                seg['manhã'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'tarde':
                seg['tarde'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'noite':
                seg['noite'] = str(row['fluxo_medio'])
        if row['num_dia_semana_evento'] == 2:
            if row['periodo_evento'] == 'manhã':
                ter['manhã'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'tarde':
                ter['tarde'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'noite':
                ter['noite'] = str(row['fluxo_medio'])
        if row['num_dia_semana_evento'] == 3:
            if row['periodo_evento'] == 'manhã':
                qua['manhã'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'tarde':
                qua['tarde'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'noite':
                qua['noite'] = str(row['fluxo_medio'])
        if row['num_dia_semana_evento'] == 4:
            if row['periodo_evento'] == 'manhã':
                qui['manhã'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'tarde':
                qui['tarde'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'noite':
                qui['noite'] = str(row['fluxo_medio'])
        if row['num_dia_semana_evento'] == 5:
            if row['periodo_evento'] == 'manhã':
                sex['manhã'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'tarde':
                sex['tarde'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'noite':
                sex['noite'] = str(row['fluxo_medio'])
        if row['num_dia_semana_evento'] == 6:
            if row['periodo_evento'] == 'manhã':
                sab['manhã'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'tarde':
                sab['tarde'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'noite':
                sab['noite'] = str(row['fluxo_medio'])
        if row['num_dia_semana_evento'] == 0:
            if row['periodo_evento'] == 'manhã':
                dom['manhã'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'tarde':
                dom['tarde'] = str(row['fluxo_medio'])
            if row['periodo_evento'] == 'noite':
                dom['noite'] = str(row['fluxo_medio'])


def parser_json_string_fluxo_medio(result):
    fluxo_medio(result)
    json_string_fluxo_medio = {
        "segunda-feira": {
            "manhã": seg['manhã'] if seg.get('manhã') else '0',
            "tarde": seg['tarde'] if seg.get('tarde') else '0',
            "noite": seg['noite'] if seg.get('noite') else '0'
        },
        "terça-feira": {
            "manhã": ter['manhã'] if ter.get('manhã') else '0',
            "tarde": ter['tarde'] if ter.get('tarde') else '0',
            "noite": ter['noite'] if ter.get('noite') else '0'
        },
        "quarta-feira": {
            "manhã": qua['manhã'] if qua.get('manhã') else '0',
            "tarde": qua['tarde'] if qua.get('tarde') else '0',
            "noite": qua['noite'] if qua.get('noite') else '0'
        },
        "quinta-feira": {
            "manhã": qui['manhã'] if qui.get('manhã') else '0',
            "tarde": qui['tarde'] if qui.get('tarde') else '0',
            "noite": qui['noite'] if qui.get('noite') else '0'
        },
        "sexta-feira": {
            "manhã": sex['manhã'] if sex.get('manhã') else '0',
            "tarde": sex['tarde'] if sex.get('tarde') else '0',
            "noite": sex['noite'] if sex.get('noite') else '0'
        },
        "sábado": {
            "manhã": sab['manhã'] if sab.get('manhã') else '0',
            "tarde": sab['tarde'] if sab.get('tarde') else '0',
            "noite": sab['noite'] if sab.get('noite') else '0'
        },
        "domingo": {
            "manhã": dom['manhã'] if dom.get('manhã') else '0',
            "tarde": dom['tarde'] if dom.get('tarde') else '0',
            "noite": dom['noite'] if dom.get('noite') else '0'
        }
    }

    return json_string_fluxo_medio
