import pytest
import app.db_connector as dbc
import app.sqlscripts_generator as generator

DB_CONF = '../migrations/dbconfig.ini'


def create_tables(connection):
    with connection.cursor() as cur:
        for _ in generator.get_sql_scripts_list():
            cur.execute(_)


def drop_tables(connection):
    with connection.cursor() as cur:
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_name like 'test_table_1_column%'")
        tables = cur.fetchall()
        for table in tables:
            cur.execute(f"DROP TABLE {table[0]}")


# @pytest.fixture(scope="session")
# def db_engine():
#     default_db = (
#         "postgresql://postgres:database@postgres:5432/postgres"
#     )
#     test_db = "postgresql://postgres:database@postgres:5432/test"
#     engine = create_async_engine(default_db)
#     if not database_exists(test_db):  # <- Getting error on this line
#         create_database(test_db)


@pytest.fixture(scope='session')
def init_db():
    conn = dbc.get_connection(DB_CONF)
    create_tables(conn)
    yield conn
    drop_tables(conn)
    conn.close()
