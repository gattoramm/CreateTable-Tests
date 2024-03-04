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
            # cur.execute("CREATE SCHEMA read_write")
            # cur.execute("GRANT SELECT ON ALL TABLES IN SCHEMA read_only TO read_only_user")
            # cur.execute("GRANT ALL ON ALL TABLES IN SCHEMA read_write TO read_write_user")


def create_role(db_name, user, password, host, port, file_path):
    pass


if __name__ == '__main__':
    create_db()
