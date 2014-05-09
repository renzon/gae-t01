# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
from base import GAETestCase
from filmes.modelo import Filme
from mock import Mock
import tmpl
from web import home, filme


class FilmeTests(GAETestCase):
    def test_deletar(self):
        handler = Mock()
        filme_chave = Filme(nome='b', preco=5).put()
        filme.deletar(handler, filme_chave.id())
        handler.redirect.assert_called_once_with('/filme')


