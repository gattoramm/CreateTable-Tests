import app.sqlscripts_filereader as sql_reader
import app.sqlscripts_constructor as sql_constructor


without_limit_type = ['numeric', 'monetary', 'character', 'binary', 'datetime', 'interval']
character_with_limit_type = ['character with limit']
datetime_with_limit_type = ['datetime with limit']
interval_with_limit_type = ['interval with limit']
numeric_with_two_limit_type = ['numeric with limit']
postgresql_without_limit_type = ['aliases']
postgresql_with_limit_type = ['aliases with limit']
postgresql_with_two_limit_type = ['aliases with two limit']


def create_tables_from_resources(connection):
    sql_scripts = sql_reader.SqlScriptFieReader().sql_files_scripts_list()
    with connection.cursor() as cur:
        for _ in sql_scripts:
            cur.execute(_)


def create_table_from_constructor(connection):
    with connection.cursor() as cur:
        for _ in get_sql_scripts_list():
            cur.execute(_)


def get_sql_scripts_list():
    types_base = sql_constructor.get_scripts_create_tables(False, without_limit_type)
    types_character = sql_constructor.get_scripts_create_tables_with_limit(False, character_with_limit_type, 255)
    types_datetime = sql_constructor.get_scripts_create_tables_with_limit(False, datetime_with_limit_type, 255)
    types_interval = sql_constructor.get_scripts_create_tables_with_limit(False, interval_with_limit_type, 2)
    types_numeric = sql_constructor.get_scripts_create_tables_with_two_limit(False, numeric_with_two_limit_type, 6, 4)
    types_al1 = sql_constructor.get_scripts_create_tables_with_limit(True, postgresql_without_limit_type, 255)
    types_al2 = sql_constructor.get_scripts_create_tables_with_limit(True, postgresql_with_limit_type, 200)
    types_al3 = sql_constructor.get_scripts_create_tables_with_two_limit(True, postgresql_with_two_limit_type, 6 , 4)

    return types_base + types_character + types_datetime + types_interval + types_numeric + types_al1 + types_al2 + types_al3

