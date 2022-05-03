from common.config import Config
from common.main import Main
import login.api


class Login(Main):

    service = None

    def __init__(self):
        super().__init__(Config.SERVICE_LOGIN)


if __name__ == '__main__':
    login_service = Login()
    login.login_main.Login.service = login_service
    login_service.run()
