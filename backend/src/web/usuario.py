# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def index(_resp):
    _resp.write('Olá Usuário')


def salvar(_req, _resp, nome,sobrenome):
    _resp.write('Salvando usuário %s %s %s'
                % (_req.method,nome, sobrenome))