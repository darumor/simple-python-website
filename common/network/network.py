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
         #   body = {'ids': [12, 14, 50]}
         #   myurl = "http://www.testmycode.com"
         #   req = urllib.request.Request(myurl)
         #   req.add_header('Content-Type', 'application/json; charset=utf-8')
         #   jsondata = json.dumps(body)
         #   jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
         #   req.add_header('Content-Length', len(jsondataasbytes))
         #   response = urllib.request.urlopen(req, jsondataasbytes)


            data = parse.urlencode(parameters).encode('utf-8')
            print(f'data: {data}')
            req = request.Request(data_url, data=data)
            response = request.urlopen(req).read()
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
        query_parameters = dict(req.query.decode())
        token = Token.parse(query_parameters)
        return token

    @staticmethod
    def extract_token_from_body(request):
        token_dict = ast.literal_eval(request.forms.get('token').decode('utf-8'))
        print(token_dict)
        token = Token.parse(token_dict)
        return token
