from bottle import run, install
from bottle_sqlite import SQLitePlugin
from common.config import Config
from datastore.store import Store
from common import api


class Main:

    def __init__(self, service):
        self.service = service
        self.config = Config(self.service)

    def run(self):
        print(f"Starting up {self.service}...")
        Store.migrate_db(self.config, self.service)

        install(SQLitePlugin(dbfile=self.config.get_db_file_path()))
        run(host=self.config.get_host(), port=self.config.get_port())

