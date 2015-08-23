# encoding: utf-8


from sqlalchemy import Column
from ..extension import db


class Image(db.Model):

    __tablename__ = 'images'

    id = Column(db.Integer, primary_key=True)
    imagename = Column(db.String(128), nullable=False, unique=True)
    imagepath = Column(db.String(128), nullable=False)

