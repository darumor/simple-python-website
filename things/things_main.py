from common.config import Config
from common.main import Main
import things.api


class Things(Main):

    service = None

    def __init__(self):
        super().__init__(Config.SERVICE_THINGS)


if __name__ == '__main__':
    things_service = Things()
    things.things_main.Things.service = things_service
    things_service.run()
