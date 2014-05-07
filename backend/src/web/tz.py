# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime
from pytz import timezone, utc

sp_timezone = timezone('America/Sao_Paulo')


def index(_json):
    agora_utc = datetime.now(tz=utc)

    agora_sp = agora_utc.astimezone(sp_timezone)
    agora_utc_str = agora_utc.strftime('%Y/%m/%d %H:%M:%S')
    agora_sp_str = agora_sp.strftime('%Y/%m/%d %H:%M:%S')
    dct = {'utc': agora_utc_str, 'sp': agora_sp_str}
    _json(dct)
