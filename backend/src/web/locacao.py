# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class Locacao(object):
    def __init__(self, nome, status, preco, data):
        self.data = data
        self.preco = preco
        self.nome = nome
        self.status = status


def index(_write_tmpl):
    locacoes = [Locacao('Coração Valente', 'Devolvido', 8.59, '08/08/2012'),
                Locacao('Sonho de Liberdade', 'Alugado', 4.99, '10/11/2013')]
    dct = {'locacoes': locacoes}
    _write_tmpl('templates/locacao_home.html', dct)