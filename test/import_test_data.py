from common.store import Store
from common.config import Config
import os

test_data_directory = 'test/test_data/'


def import_users(config, file_name='users.json'):
    Store.migrate_db(config)
    users_file = os.path.join(test_data_directory, file_name)
    Store.import_test_data(config, 'users', users_file)


def import_authdata(config, file_name='authdata.json'):
    Store.migrate_db(config)
    authdata_file = os.path.join(test_data_directory, file_name)
    Store.import_test_data(config, 'auth_methods', authdata_file)


def import_things(config, file_name='things.json'):
    Store.migrate_db(config)
    things_file = os.path.join(test_data_directory, file_name)
    Store.import_test_data(config, 'things', things_file)


if __name__ == '__main__':
    print("importing test data...")
    #import_users(Config(Config.SERVICE_USERS))
    #import_authdata(Config(Config.SERVICE_LOGIN))
    #import_things(Config(Config.SERVICE_THINGS))

