# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from google.appengine.ext import ndb
from usuario.modelo import Usuario


class Filme(ndb.Model):
    nome = ndb.StringProperty(required=True)
    preco = ndb.FloatProperty(required=True)
    status = ndb.StringProperty(choices=['DISPONIVEL', 'ALUGADO'], default='DISPONIVEL')

    def to_dict(self):
        dct = super(Filme, self).to_dict()
        dct['id'] = self.key.id()
        return dct


class Locacao(ndb.Model):
    status = ndb.StringProperty(choices=['DISPONIVEL', 'ALUGADO', 'DEVOLVIDO'], default='DISPONIVEL')
    preco = ndb.FloatProperty(required=True)
    data = ndb.DateTimeProperty(auto_now_add=True)
    nome = ndb.StringProperty(required=True, indexed=False)
    usuario_key = ndb.KeyProperty(Usuario, required=True)
    filme_key = ndb.KeyProperty(Filme, required=True)
