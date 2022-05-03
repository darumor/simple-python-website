from bottle import get
from app.app_main import App
from common.network.network import Network

@get('/services/<service>')
def service_url(service):
    url = App.service.config.get_service_url(service)
    #network = Network.get_network(App.service.config)
    # network.get_url(service)
    return dict(service_url=url)

