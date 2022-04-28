from bottle import get
from app.app_main import App


@get('/services/<service>')
def service_url(service):
    url = App().config.get_service_url(service)
    return dict(service_url=url)

