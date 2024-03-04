class Table:
    # тут сделать основные проверки таблицы (по сути - проверка, что таблица есть в БД в конкретной схеме, с данным названием)

    def __init__(self, conn, table_name, columns, schema):
        self.conn = conn
        self.table_name = table_name
        self.columns = columns
        self.schema = schema

    # проверка таблицы
    def check_table(self):
        query = f"SELECT * FROM information_schema.columns WHERE table_name = '{self.table_name}'"
        with self.conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchall()
            print(result)           #debug
            if result != self.columns:
                raise Exception('Columns do not match')


class Column:
    # тут проверки, что кол-во столбцов, названия столбцов, типы столбцов, алиасы столбцов соответствуют ожидаемому

    def __init__(self, conn, table_name, column_name, column_type):
        self.conn = conn
        self.column_name = table_name
        self.column_name = column_name
        self.column_type = column_type

    # проверка столбцов
    def check_column(self):
        pass
