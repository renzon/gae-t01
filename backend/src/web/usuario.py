# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def index(_resp, _usuario_logado):
    _resp.write('Olá Usuário %s' % _usuario_logado.nome)


def salvar(_req, _resp, nome, sobrenome):
    _resp.write('Salvando usuário %s %s %s'
                % (_req.method, nome, sobrenome))