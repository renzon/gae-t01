# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from filmes.modelo import Filme


def listar_filmes(_json):
    query = Filme.query().order(Filme.nome)
    filmes = query.fetch()
    filmes_lista = [f.to_dict() for f in filmes]
    _json(filmes_lista,'')

def salvar(_json,nome ,preco, status):
    filme=Filme(nome=nome,preco=float(preco),status=status)
    filme.put()
    _json(filme.to_dict())