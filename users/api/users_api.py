from bottle import route, request, response, HTTPError
from users.datastore import users as store
from common.network.network import Network
from users.users_main import Users


@route('/user/<user_id>', method=['OPTIONS', 'GET'])
def user_by_user_id(db, user_id):
    token = Network.extract_token_from_query(request)
    config = Users.service.config
    if token.is_valid_service_token(config):
        return store.get_user_by_id(db, user_id)
    else:
        return dict(error='Invalid token')


# post create_user
@route('/users', method=['OPTIONS', 'POST'])
def create_user(db):
    details = request.forms
    for key in details.keys():
        print(f'{key}: {details[key]}')
    token = Network.extract_token_from_body(request)
    config = Users.service.config
    if token.is_valid_service_token(config):
        firstname = request.forms.get('firstname')
        lastname = request.forms.get('lastname')
        cursor = db.execute(
            'INSERT INTO users(firstname, lastname, created_at, is_admin) values(?, ?, CURRENT_TIMESTAMP, 0);',
            (firstname, lastname))
        row_count = cursor.rowcount
        if row_count != 1:
            return dict(error='Error inserting user')
        else:
            return dict(user_id=cursor.lastrowid)
    else:
        return dict(error='Invalid token')


