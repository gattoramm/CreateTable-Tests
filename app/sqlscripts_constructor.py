import configparser

TYPES = '../migrations/data_types.ini'


class DatatypeReader:
    def __init__(self, config_file: str = TYPES):
        self.config_file = config_file

    def get_map_types(self, is_aliases: bool, lst: dict) -> dict:
        config = configparser.ConfigParser()
        config.read(self.config_file)

        if is_aliases:
            return {key: config[item][key].split(', ') for item in lst for key in config[item]}
        else:
            return {item: config[item]['types'].split(', ') for item in lst}


reader = DatatypeReader()


def get_types(is_aliases: bool, lst: dict) -> list:
    return [val for key, value in reader.get_map_types(is_aliases, lst).items() for val in value]


def get_list__type_table_column(is_aliases: bool, lst: dict) -> list:
    list__type_table_column = []
    for item in get_types(is_aliases, lst):
        _item = item.replace(' ', '_')
        column_string = f"column_{_item}"
        table_string = f"test_table_1_column__{_item}"
        list__type_table_column.append([item, column_string, table_string])
    return list__type_table_column


map_type__table_column = dict()


def get_scripts_create_tables(is_aliases: bool, lst: dict) -> list:
    scripts = []
    for item in get_list__type_table_column(is_aliases, lst):
        type = item[0]
        column = item[1]
        table = item[2]
        sql_string = f"create table {table} ({column} {type});"
        scripts.append(sql_string)

        map_type__table_column[type] = [table, column]
    return scripts


def get_scripts_create_tables_with_limit(is_aliases: bool, lst: dict, limit: int) -> list:
    scripts = []
    for item in get_list__type_table_column(is_aliases, lst):
        type = item[0]\
            .replace('(p)', f"({limit})")

        column = item[1]\
            .replace('(p)', f"_{limit}")

        table = item[2]\
            .replace('(p)', f"_{limit}")

        sql_string = f"create table {table} ({column} {type});"
        scripts.append(sql_string)

        map_type__table_column[type] = [table, column]
    return scripts


def get_scripts_create_tables_with_two_limit(is_aliases: bool, lst: dict, limit1: int, limit2: int) -> list:
    scripts = []
    for item in get_list__type_table_column(is_aliases, lst):
        type = item[0]\
            .replace('(p', f"({limit1}")\
            .replace('t)', f"{limit2})")

        column = item[1]\
            .replace('(p,', f"_{limit1}")\
            .replace('t)', f"_{limit2}")

        table = item[2]\
            .replace('(p,', f"_{limit1}")\
            .replace('t)', f"_{limit2}")

        sql_string = f"create table {table} ({column} {type});"
        scripts.append(sql_string)

        map_type__table_column[type] = [table, column]
    return scripts


def get_scripts_drop_tables(is_aliases: bool, lst: dict) -> list:
    scripts = []
    for item in get_list__type_table_column(is_aliases, lst):
        sql_string = f"drop table {item[2]} cascade;"
        scripts.append(sql_string)
    return scripts
