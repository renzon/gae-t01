# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import tmpl
from tekton.gae.middleware import Middleware


def execute(next_process, handler, dependencies, **kwargs):
    def write_tmpl(template_name, values=None):
        def aba_deve_ficar_selecionada(path_da_aba):
            return handler

        values = values or {}
        return handler.response.write(tmpl.render(template_name, values))

    dependencies["_write_tmpl"] = write_tmpl
    dependencies["_render"] = tmpl.render
    next_process(dependencies, **kwargs)


class TemplateMiddleware(Middleware):
    def set_up(self):
        def write_tmpl(template_name, values=None):
            def aba_deve_ficar_selecionada(path_da_aba):
                return self.handler.request.path.startswith(path_da_aba)

            values = values or {}
            values['_aba_deve_ficar_selecionada'] = aba_deve_ficar_selecionada
            values['_login_url'] = self.dependencies['_login_url']
            values['_logout_url'] = self.dependencies['_logout_url']
            values['_usuario_logado'] = self.dependencies['_usuario_logado']
            return self.handler.response.write(tmpl.render(template_name, values))

        self.dependencies["_write_tmpl"] = write_tmpl
        self.dependencies["_render"] = tmpl.render
