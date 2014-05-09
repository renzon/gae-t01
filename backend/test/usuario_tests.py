# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from base import GAETestCase
from usuario.modelo import Usuario


class DBTests(GAETestCase):
    def test_busca_por_google_id(self):
        query = Usuario.query_por_google_id('123')
        usuario = query.get()
        self.assertIsNone(usuario)
        chave_usuario = Usuario(nome='qualuer', email='email', google_id='123').put()
        usuario = query.get()
        self.assertEqual(chave_usuario, usuario.key)
