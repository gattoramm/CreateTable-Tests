import os
import re


SQL_SCRIPTS_PATH = '../migrations/scripts/positive_table'
# SQL_SCRIPTS_PATH = '../migrations/scripts/many_columns'


class SqlScriptFieReader:
    def __init__(self, path:str = SQL_SCRIPTS_PATH):
        self.path = path

    def sql_files_path(self):
        path_list = []
        for root, subdirs, files in os.walk(self.path):
            for _ in files:
                file_path = os.path.join(root, _)
                path_list.append(file_path)
        return path_list

    def sql_files_map_script_value(self):
        script_dict = dict()
        for _ in self.sql_files_path():
            with open(_, 'r') as fd:
                script_dict[_] = fd.read()
        return script_dict

    def sql_files_scripts_list(self):
        script_list = list()
        for _ in self.sql_files_path():
            with open(_, 'r') as fd:
                script_list.append(fd.read())
        return script_list

    def sql_files_scripts_tables(self):
        table_name_list = list()
        for _ in self.sql_files_scripts_list():
            column_name_reg = re.compile(r'test_table[^(]*')
            column_name = column_name_reg.search(_)
            table_name_list.append(column_name.group().strip())
        return table_name_list

# if __name__ == '__main__':
#     print(SqlScriptFieReader().sql_files_scripts_list())
