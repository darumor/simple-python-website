from bottle import route, request, response, HTTPError
from users.datastore import users as store
from data.config import Config
from common.network.token import Token
from users.users_main import Users
import json


@route('/user/<user_id>', method=['OPTIONS', 'GET'])
def user_by_user_id(db, user_id):
    query_parameters = dict(request.query.decode())
    for key in query_parameters.keys():
        if query_parameters[key] == 'None':
            query_parameters[key] = None
    token = Token.parse(query_parameters)
    config = Users.service.config
    if token.is_valid_service_token(config):
        return store.get_user_by_id(db, user_id)
    else:
        return dict(error='Invalid token')

# post create_user


