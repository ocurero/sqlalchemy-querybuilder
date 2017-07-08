from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base, MyParentModel, MyChildModel
import pytest


@pytest.fixture(scope='session')
def engine():
    return create_engine('sqlite://')


@pytest.yield_fixture(scope='session')
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)


@pytest.yield_fixture
def query(engine, tables):
    """Returns an sqlalchemy query object"""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)
    session.add(MyParentModel(parentid=1))
    session.add(MyParentModel(parentid=2))
    session.add(MyParentModel(parentid=3))
    session.add(MyChildModel(childid=1, parentid=1))
    session.add(MyChildModel(childid=2, parentid=1))
    session.add(MyChildModel(childid=3, parentid=2))
    yield session.query()

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()
