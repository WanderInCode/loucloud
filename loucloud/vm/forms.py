# encoding: utf-8

from flask_wtf import Form
from wtforms import (SubmitField, DateTimeField, IntegerField)


class AddVmForm(Form):
    templateid = IntegerField(u'模板ID')
    userid = IntegerField(u'用户ID')
    cpunum = IntegerField(u'cpu数量')
    createtime = DateTimeField(u'创建时间')

    submit = SubmitField(u'创建')
