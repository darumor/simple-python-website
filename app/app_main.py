from common.config import Config
from common.main import Main
import app.api


class App(Main):

    def __init__(self):
        super().__init__(Config.SERVICE_APP)


if __name__ == '__main__':
    App().run()






