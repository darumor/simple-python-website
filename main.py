import os
from bottle import run, install
from bottle_sqlite import SQLitePlugin
from data.config import Config
from common.store import Store

if __name__ == '__main__':
    print("Starting up...")

    Config()
    Store.migrate_db(Config.config)

    database_filename = os.path.join(Config.config.data_directory, Config.config.db_filename)
    install(SQLitePlugin(dbfile=database_filename))

    run(host='localhost', port=Config.config.port)
