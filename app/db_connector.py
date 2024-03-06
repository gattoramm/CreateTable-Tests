import configparser
import psycopg2


def get_connection(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    config = config['db']
    conn = psycopg2.connect(
        database=config["database"],
        user=config["user"],
        password=config["password"],
        host=config["host"],
        port=config["port"])

    return conn
