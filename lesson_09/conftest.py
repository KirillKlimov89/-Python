import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = (
    "postgresql+psycopg2://postgres:Gvidon89@localhost:5432/school_bd"
    "?client_encoding=utf8"
)


@pytest.fixture(scope="session")
def engine():
    return create_engine(DATABASE_URL)


@pytest.fixture
def db_session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session

    session.close()
    transaction.rollback()
    connection.close()
