import bottle
from bottle_sqlite import SQLitePlugin
from common.config import Config
from common.store import Store
from common.enable_cors import EnableCors


class Main:

    def __init__(self, service):
        self.service = service
        self.config = Config(self.service)

    def run(self):
        print(f"Starting up {self.service}...")
        Store.migrate_db(self.config, self.service)

        a = bottle.app()
        a.install(SQLitePlugin(dbfile=self.config.get_db_file_path()))
        a.install(EnableCors(self.config.get_service_url(Config.SERVICE_APP)))
        a.run(host=self.config.get_host(), port=self.config.get_port())

