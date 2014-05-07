# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from google.appengine.ext import ndb
from filmes.modelo import Locacao
from tekton import router


def index(_write_tmpl, _usuario_logado):
    query = Locacao.query(Locacao.usuario_key == _usuario_logado.key).order(-Locacao.data)
    locacoes = query.fetch()
    for loc in locacoes:
        loc.devolver_path = router.to_path(devolver, loc.key.id())
    dct = {'locacoes': locacoes}
    _write_tmpl('templates/locacao_home.html', dct)


def devolver(_handler, loc_id):
    loc = Locacao.get_by_id(int(loc_id))
    filme = loc.filme_key.get()
    loc.status = 'DEVOLVIDO'
    filme.status = 'DISPONIVEL'
    ndb.put_multi([loc, filme])
    _handler.redirect(router.to_path(index))
