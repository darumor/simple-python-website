from bottle import route, post, get, request, response, HTTPError
from common.config import Config
from common.network.network import Network
from common.network.token import Token
from login.datastore import login as store
from login.login_main import Login


@route('/login', method=['OPTIONS', 'POST'])
def do_login(db):
    success = False
    username = request.json.get('username')
    password = request.json.get('password')
    config = Login.service.config
    user_id = store.check_login(db, config, username, password)
    if user_id > 0:
        success = True
        login_token = Token.create_service_token(Config.SERVICE_LOGIN, config)
        token = create_token(user_id, request.remote_addr, Network.get_network(config), login_token, config)
        cookie_content = {
            'token': token
        }
        conf = Login.service.config
        response.set_cookie("account", cookie_content, secret=conf.cookie_secret,
                            max_age=conf.session_ttl)

    response.headers['Content-type'] = 'application/json'
    return dict(login_success=success)


@post('/register')
def register(db):
    firstname = request.json.get('firstname')
    lastname = request.json.get('lastname')
    username = request.json.get('username')
    password = request.json.get('password')
    error_msg = None
    if firstname is not None and lastname is not None and username is not None and password is not None:
        network = Network.get_network(Login.service.config)
        user_id = store.user_id_by_username(db, username)

        if user_id is not None:
            registration_success = False
            error_msg = 'Username is already in use'
        else:
            registration_success = store.create_user(db, Login.service.config, firstname, lastname, username, password)
            if not registration_success:
                error_msg = 'Some random error occurred'
    else:
        registration_success=False
        error_msg = 'Mandatory information missing'

    response.headers['Content-type'] = 'application/json'
    return dict(registration_success=registration_success,
                error_msg=error_msg)


@get('/current-user')
def current_user(db):
    cookie_content = request.get_cookie("account", secret=Login.service.config.cookie_secret)
    if cookie_content:
        return cookie_content['user']
    return HTTPError(401, 'Access denied')


def create_token(user_id, user_ip, network, login_token, config):
    user = store.get_user_by_id(network, user_id, login_token)
    rights = {}
    token = Token(user, user_ip, rights)
    token.sign(config)
    return token
