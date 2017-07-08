from sqlalchemy import Column, Integer, select, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()


class MyParentModel(Base):
    __tablename__ = 'test1'
    parentid = Column('test1id', Integer, primary_key=True)
    childs = relationship('MyChildModel')

    @hybrid_property
    def childid(self):
        return self.childs[0].childid

    @childid.expression
    def childid(cls):
        return select([MyChildModel.childid]).where(
               cls.parentid == MyChildModel.parentid).as_scalar()


class MyChildModel(Base):
    __tablename__ = 'test2'
    childid = Column('test2id', Integer, primary_key=True)
    parentid = Column('parentid', Integer, ForeignKey('test1.test1id'),
                      primary_key=True)
