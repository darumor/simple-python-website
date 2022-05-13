import hashlib
from common.network.network import Network


def calculate_password_hash(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def check_login(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute(
        'SELECT user_id from auth_methods where username=? and password=? and type=\'USERNAME_AND_PASSWORD\'',
        (username, password_hash)).fetchone()
    if row:
        return int(row['user_id'])
    return -1


def check_admin(db, username):
    user = user_by_username(db, username)
    if user:
        return bool(user["is_admin"])
    else:
        return False


def user_by_username(network, db, username):
    user_id = user_id_by_username(db, username)
    return get_user_by_id(network, db, user_id)


def get_user_by_id(network, user_id, token):
    return network.get(Network.SERVICE_USERS, f'{Network.END_POINT_USER_BY_ID}{user_id}', {}, token)


def user_id_by_username(db, username):
    row = db.execute("SELECT user_id from auth_methods where username=? and type='USERNAME_AND_PASSWORD'", (username,)).fetchone()
    if row:
        user_id = int(row["user_id"])
        return user_id
    return None


def user_name_exists(db, username):
    return user_id_by_username(db, username) is not None


def register_user(network, db, config, firstname, lastname, username, password, token):
    if user_name_exists(db, username):
        return False

    # create_user
    resp = network.post(Network.SERVICE_USERS, f'{Network.END_POINT_USERS}',
                        dict(firstname=firstname, lastname=lastname), token)
    print(f'new user: {resp}')
    user_id = resp['user_id']

    # create_auth_method
    if user_id > 0:
        password_hash = calculate_password_hash(config, password)
        row_count = db.execute(
            "INSERT INTO auth_methods(user_id, username, password, type) values(?, ?, ?, 'USERNAME_AND_PASSWORD');",
            (user_id, username, password_hash)).rowcount

        if row_count > 0:
            return True

    return None
