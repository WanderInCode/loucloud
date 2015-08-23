# encoding: utf-8

from flask_wtf import Form
from wtforms import (TextField, SubmitField)


class AddImageForm(Form):
    imagename = TextField(u'镜像名')
    imagepath = TextField(u'镜像路径')

    submit = SubmitField(u'创建')
    