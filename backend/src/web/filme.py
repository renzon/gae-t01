# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import logging
from google.appengine.ext import ndb
from filmes.modelo import Filme, Locacao
from tekton import router


def index(_write_tmpl):
    query = Filme.query().order(Filme.nome)

    filmes = query.fetch()
    for f in filmes:
        f.editar_path = router.to_path(editar, f.key.urlsafe())
        f.deletar_path = router.to_path(deletar, f.key.id())
        f.alugar_path = router.to_path(alugar, f.key.id())
    dct = {'salvar_path': router.to_path(salvar),
           'filmes': filmes}
    _write_tmpl('templates/filme_home.html', dct)


def alugar(_handler, _usuario_logado, filme_id):
    filme_key = ndb.Key(Filme, int(filme_id))
    filme_futuro = filme_key.get_async()
    logging.info('Operação custosa')
    filme = filme_futuro.get_result()
    locacao = Locacao(usuario_key=_usuario_logado.key,
                      filme_key=filme_key,
                      nome=filme.nome,
                      preco=filme.preco,
                      status='ALUGADO')
    filme.status = 'ALUGADO'
    ndb.put_multi([filme, locacao])
    path = router.to_path(index)
    _handler.redirect(path)


def deletar(_handler, id):
    key = ndb.Key(Filme, int(id))
    key.delete()
    path = router.to_path(index)
    _handler.redirect(path)


def salvar(_handler, nome, preco, status='DISPONIVEL'):
    filme = Filme(nome=nome, preco=float(preco), status=status)
    filme.put()
    path = router.to_path(index)
    _handler.redirect(path)


def editar(_write_tmpl, key_str):
    key = ndb.Key(urlsafe=key_str)
    filme = key.get()
    dct = {'filme': filme,
           'salvar_path': router.to_path(edit)}
    _write_tmpl('templates/filme_form.html', dct)


def edit(_handler, id, nome, preco, status):
    filme = Filme.get_by_id(int(id))
    filme.nome = nome
    filme.preco = float(preco)
    filme.status = status
    filme.put()
    path = router.to_path(index)
    _handler.redirect(path)
