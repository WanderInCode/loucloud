# encoding: utf-8

from flask_wtf import Form
from wtforms import (TextField, SubmitField, IntegerField)


class AddTemplateForm(Form):
    templatename = TextField(u'模板名')
    imageid = IntegerField(u'镜像ID')
    cpunum = IntegerField(u'CPU数量')
    memnum = IntegerField(u'内存容量')

    submit = SubmitField(u'创建')
