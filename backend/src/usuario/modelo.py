# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from google.appengine.ext import ndb


class Usuario(ndb.Model):
    nome = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    google_id = ndb.StringProperty()

    @classmethod
    def query_por_google_id(cls, google_id):
        return cls.query(cls.google_id == google_id)