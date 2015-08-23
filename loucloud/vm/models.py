# encoding: utf-8


from sqlalchemy import Column
from ..extension import db


class Vm(db.Model):

    __tablename__ = 'vms'

    id = Column(db.Integer, primary_key=True)
    templateid = Column(db.Integer, db.ForeignKey('templates.id'))
    userid = Column(db.Integer, db.ForeignKey('users.id'))
    cpunum = Column(db.Integer, nullable=False)
    createtime = Column(db.DateTime, nullable=False)
