import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import app.db_connector as dbc

LINK = '../migrations/scripts/000_create_db.sql'


def create_db():
    with open(LINK, 'r') as fd:
        file = fd.read()

    with dbc.get_connection() as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(sql.SQL(file))


def create_role(db_name, user, password, host, port, file_path):
    pass
