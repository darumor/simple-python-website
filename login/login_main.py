import os
from bottle import run, install
from bottle_sqlite import SQLitePlugin
from data.config import Config
from datastore.store import Store
import api

if __name__ == '__main__':
    print("Starting up...")

    Config()
    Store.migrate_db(Config.config)

    #test_db = bottle.ext.sqlite.Plugin(dbfile='/tmp/test.db')
    #cache_db = bottle.ext.sqlite.Plugin(dbfile=':memory:', keyword='cache')
    #app.install(test_db)
    #app.install(cache_db)

    database_filename = os.path.join(Config.config.data_directory, Config.config.db_filename)
    install(SQLitePlugin(dbfile=database_filename))

    run(host='localhost', port=Config.config.port)
