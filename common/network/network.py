import ast
from common.config import Config
from common.network.token import Token
import json
from urllib import request, parse, error


class Network:

    SERVICE_APP = 'SERVICE_APP'
    SERVICE_USERS = 'SERVICE_USERS'
    SERVICE_LOGIN = 'SERVICE_LOGIN'
    SERVICE_THINGS = 'SERVICE_THINGS'

    END_POINT_APP_SERVICES = '/services/'
    END_POINT_USER_BY_ID = '/user/'
    END_POINT_USERS = '/users'
    END_POINT_LOGIN_USER_BY_USER_NAME = '/by-user-name/'
    END_POINT_LOGIN_LOGIN = '/login'
    END_POINT_LOGIN_REGISTER = '/register'

    TOKEN = 'token'
    network = None

    def __init__(self, config):
        self.config = config

    def get(self, service, path, parameters, token):
        data_url = self.get_url(service, path)
        url_parts = list(parse.urlparse(data_url))
        query = dict(parse.parse_qsl(url_parts[4]))
        query.update(parameters)
        query.update(token.to_dict())
        url_parts[4] = parse.urlencode(query)

        data_url = parse.urlunparse(url_parts)
        print(f'network.data_url = GET {data_url}')
        try:
            content = request.urlopen(data_url).read()
            return json.loads(content)
        except error.HTTPError as err:
            print(f'Error {err}')
            return dict(error=err)

    def post(self, service, path, parameters, token):
        if parameters is None:
            parameters = {}
        parameters[Network.TOKEN] = token.to_dict()
        data_url = self.get_url(service, path)
        print(f'network.data_url = POST {data_url}')
        try:
            req = request.Request(data_url)
            req.add_header('Content-Type', 'application/json; charset=utf-8')
            json_data = json.dumps(parameters)
            json_data_as_bytes = json_data.encode('utf-8')
            req.add_header('Content-Length', str(len(json_data_as_bytes)))
            response = request.urlopen(req, json_data_as_bytes).read()
            return json.loads(response)
        except error.HTTPError as err:
            print(f'Error {err}')
            return dict(error=err)

    def get_url(self, service, path):
        return f'http://' \
               f'{self.config.all_services[service][Config.CONF_HOST]}:' \
               f'{self.config.all_services[service][Config.CONF_PORT]}' \
               f'{path or ""}'

    @staticmethod
    def get_network(config):
        if Network.network is None:
            Network.network = Network(config)
        return Network.network

    @staticmethod
    def extract_token_from_query(req):
        token = Token.parse(dict(req.query.decode()))
        return token

    @staticmethod
    def extract_token_from_body(json_val):
        token = Token.parse(json_val["token"])
        return token
