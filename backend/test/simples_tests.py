# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest


class SimplesTests(unittest.TestCase):
    def setUp(self):
        print('foo')

    def test_soma(self):
        resultado = 1 + 2
        self.assertEqual(3, resultado)

    def test_foo(self):
        pass
        # self.fail('Falhou')

    def tearDown(self):
        print 'Downs'


if __name__ == '__main__':
    unittest.main()
