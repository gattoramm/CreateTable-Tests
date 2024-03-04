import os
import re


if __name__ == '__main__':
    LINK = '../migrations/scripts/positive_table'

    for root, subdirs, files in os.walk(LINK):
        list_file_path = os.path.join(root)
        for _ in files:
            file_path = os.path.join(root, _)
            # print(file_path)
            with open(file_path, 'r') as fd:
                file = fd.read()
                print(file)
                # ff = file.split(' ')
                #
                #
                # #create table test_table_1_column__smallint (column_smallint smallint);
                table_name = re.search(r'create table (\w+)', file).group(1)
                print(table_name)
                # print(ff[3][1:])


    # with db_connection() as (conn, cursor):
    #     cursor.execute("CREATE TABLE users (id serial PRIMARY KEY, name text)")
    #     conn.commit()
