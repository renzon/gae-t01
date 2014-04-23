# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from google.appengine.api import users
from tekton.gae.middleware import Middleware
from usuario.modelo import Usuario


class LoginMiddleware(Middleware):
    def set_up(self):
        usuario_google = users.get_current_user()
        if usuario_google:
            self.dependencies['_login_url'] = None
            self.dependencies['_logout_url'] = users.create_logout_url('/')
            google_id = usuario_google.user_id()
            query = Usuario.query_por_google_id(google_id)
            usuario=query.get()
            if usuario is None:
                usuario=Usuario(google_id=google_id,
                                nome=usuario_google.nickname(),
                                email=usuario_google.email())
                usuario.put()
            self.dependencies['_usuario_logado'] = usuario
        else:
            login_url = users.create_login_url(self.handler.request.path)
            self.dependencies['_login_url'] = login_url
            self.dependencies['_logout_url'] = None
            self.dependencies['_usuario_logado'] = None

