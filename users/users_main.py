from common.config import Config
from common.main import Main
import users.api


class Users(Main):

    service = None

    def __init__(self):
        super().__init__(Config.SERVICE_USERS)


if __name__ == '__main__':
    users_service = Users()
    users.users_main.Users.service = users_service
    users_service.run()
