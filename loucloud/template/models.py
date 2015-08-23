# encoding: utf-8

from sqlalchemy import Column
from ..extension import db


class Template(db.Model):

    __tablename__ = 'templates'

    id = Column(db.Integer, primary_key=True)
    templatename = Column(db.String(128), nullable=False, unique=True)
    imageid = Column(db.Integer, db.ForeignKey('images.id'))
    cpunum = Column(db.Integer, nullable=False)
    memnum = Column(db.Integer, nullable=False)
