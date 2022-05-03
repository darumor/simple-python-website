import sqlite3
from sqlite3 import Error
import os


class Connection(object):
    def __init__(self, conf):
        self.config = conf
        self.database_filename = conf.get_db_file_path()
        self.db_connection = None

    def __enter__(self):
        self.db_connection = self.create_connection()
        return self.db_connection

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value or exc_type or traceback:
            print(exc_value)
            print(exc_type)
            print(traceback)
        self.db_connection.commit()
        self.db_connection.close()

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.database_filename)
            return conn
        except Error as e:
            print(e)
        return conn
