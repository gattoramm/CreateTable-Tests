import pytest
import app.db_connector as dbc


@pytest.fixture(scope='session')
def db_connection():
    conn = dbc.get_connection()
    yield conn
    conn.close()
