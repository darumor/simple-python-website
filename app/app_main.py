from common.config import Config
from common.main import Main
import app.api


class App(Main):

    service = None

    def __init__(self):
        super().__init__(Config.SERVICE_APP)


if __name__ == '__main__':
    app_service = App()
    app.app_main.App.service = app_service
    app_service.run()
