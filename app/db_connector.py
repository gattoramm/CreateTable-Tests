import configparser
import psycopg2

LINK = '../migrations/dbconfig.ini'


class DBConnection:
    def __init__(self, config_file):
        self.conn = None
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def create_connection(self):
        self.config = self.config['db']
        self.conn = psycopg2.connect(
            database=self.config["database"],
            user=self.config["user"],
            password=self.config["password"],
            host=self.config["host"],
            port=self.config["port"]
        )

        return self.conn


def get_connection(config_file: str = LINK):
    return DBConnection(config_file).create_connection()
