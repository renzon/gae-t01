# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
from mock import Mock
import tmpl
from web import home


class HomeTests(unittest.TestCase):
    def test_index(self):
        funcao = Mock()
        home.index(funcao)
        funcao.assert_called_once_with('templates/base.html')
        tmpl.render('templates/base.html',
                    {'_aba_deve_ficar_selecionada': Mock()})

