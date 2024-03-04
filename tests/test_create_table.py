import random


def test_query(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        str = random.Random(5)
        print(str)
        cursor.execute("INSERT INTO users (name) VALUES ('{}')".format(str))
        conn.commit()


def test_query2(db_connection):
    with db_connection as conn:
        cursor = conn.cursor()
        str = random.Random(5)
        print(str)
        cursor.execute("INSERT INTO users2 (name) VALUES ('{}')".format(str))
        conn.commit()
