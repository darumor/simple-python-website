import os


class Config:

    SERVICE_APP = 'SERVICE_APP'
    SERVICE_USERS = 'SERVICE_USERS'
    SERVICE_LOGIN = 'SERVICE_LOGIN'
    SERVICE_THINGS = 'SERVICE_THINGS'

    CONF_SERVICE_NAME = 'service_name'
    CONF_HOST = 'host'
    ENV_HOST = 'env_host'
    CONF_PORT = 'port'
    ENV_PORT = 'env_port'
    CONF_DATA_DIRECTORY = 'data_directory'
    CONF_DB_FILE_NAME = 'db_file_name'
    CONF_MIGRATIONS_FILE_NAME = 'migrations_file_name'
    CONF_STATIC_FILES_DIRECTORY = 'static_files_directory'

    ENV_STATIC_FILES_DIRECTORY = 'SPW_STATIC_FILES_DIRECTORY'
    ENV_COOKIE_SECRET = 'SPW_COOKIE_SECRET'
    ENV_PASSWORD_SECRET = 'SPW_PASSWORD_SECRET'
    ENV_TOKEN_SECRET = 'SPW_TOKEN_SECRET'
    ENV_SESSION_TTL = 'SPW_SESSION_TTL'
    ENV_CONFIG_FILE_NAME = 'SPW_CONFIG_FILE_NAME'

    defaults = dict(
        SPW_COOKIE_SECRET='some-secret-value',
        SPW_PASSWORD_SECRET='some-other-secret-value',
        SPW_TOKEN_SECRET='yet-another-secret-value',
        SPW_SESSION_TTL=30,
        SPW_CONFIG_FILE_NAME=None
    )

    SERVICES = [
        {
            CONF_SERVICE_NAME: SERVICE_APP,
            CONF_HOST: 'localhost',
            ENV_HOST: 'SPW_APP_HOST',
            CONF_PORT: 9999,
            ENV_PORT: 'SPW_APP_PORT',
            CONF_DATA_DIRECTORY: 'app/data',
            CONF_DB_FILE_NAME: 'app.db',
            CONF_MIGRATIONS_FILE_NAME: 'app_migrations.json',
            CONF_STATIC_FILES_DIRECTORY: 'app/public'
        },
        {
            CONF_SERVICE_NAME: SERVICE_USERS,
            CONF_HOST: 'localhost',
            ENV_HOST: 'SPW_USERS_HOST',
            CONF_PORT: 9998,
            ENV_PORT: 'SPW_USERS_PORT',
            CONF_DATA_DIRECTORY: 'users/data',
            CONF_DB_FILE_NAME: 'users.db',
            CONF_MIGRATIONS_FILE_NAME: 'users_migrations.json',
            CONF_STATIC_FILES_DIRECTORY: None
        },
        {
            CONF_SERVICE_NAME: SERVICE_LOGIN,
            CONF_HOST: 'localhost',
            ENV_HOST: 'SPW_LOGIN_HOST',
            CONF_PORT: 9996,
            ENV_PORT: 'SPW_LOGIN_PORT',
            CONF_DATA_DIRECTORY: 'login/data',
            CONF_DB_FILE_NAME: 'login.db',
            CONF_MIGRATIONS_FILE_NAME: 'login_migrations.json',
            CONF_STATIC_FILES_DIRECTORY: None
        },
        {
            CONF_SERVICE_NAME: SERVICE_THINGS,
            CONF_HOST: 'localhost',
            ENV_HOST: 'SPW_THINGS_HOST',
            CONF_PORT: 9997,
            ENV_PORT: 'SPW_THINGS_PORT',
            CONF_DATA_DIRECTORY: 'things/data',
            CONF_DB_FILE_NAME: 'things.db',
            CONF_MIGRATIONS_FILE_NAME: 'things_migrations.json',
            CONF_STATIC_FILES_DIRECTORY: None
        }
    ]

    def __init__(self, service=None):
        self.service = service
        self.cookie_secret = os.getenv(Config.ENV_COOKIE_SECRET) or Config.defaults[Config.ENV_COOKIE_SECRET]
        self.password_secret = os.getenv(Config.ENV_PASSWORD_SECRET) or Config.defaults[Config.ENV_PASSWORD_SECRET]
        self.token_secret = os.getenv(Config.ENV_TOKEN_SECRET) or Config.defaults[Config.ENV_TOKEN_SECRET]
        self.session_ttl = os.getenv(Config.ENV_SESSION_TTL) or Config.defaults[Config.ENV_SESSION_TTL]
        self.config_file_name = os.getenv(Config.ENV_CONFIG_FILE_NAME) or Config.defaults[Config.ENV_CONFIG_FILE_NAME]

        #todo read SERVICES from [config_file_name] -> local / public

        self.data_directory = None
        self.db_file_name = None
        self.migrations_file_name = None
        self.static_files_directory = None

        self.all_services = dict()
        for service_item in Config.SERVICES:
            service_name = service_item.get(Config.CONF_SERVICE_NAME)
            self.all_services[service_name] = dict()
            self.all_services[service_name][Config.CONF_HOST] = \
                os.getenv(service_item.get(Config.ENV_HOST)) or \
                service_item.get(Config.CONF_HOST)

            self.all_services[service_name][Config.CONF_PORT] = \
                os.getenv(service_item.get(Config.ENV_PORT)) or \
                service_item.get(Config.CONF_PORT)

            if service_name == self.service:
                self.data_directory = service_item.get(Config.CONF_DATA_DIRECTORY)
                self.data_directory = service_item.get(Config.CONF_DATA_DIRECTORY)
                self.db_file_name = service_item.get(Config.CONF_DB_FILE_NAME)
                self.migrations_file_name = service_item.get(Config.CONF_MIGRATIONS_FILE_NAME)
                self.static_files_directory = service_item.get(Config.CONF_STATIC_FILES_DIRECTORY)

    def get_db_file_path(self):
        return os.path.join(self.data_directory, self.db_file_name)

    def get_migrations_file_path(self):
        return os.path.join(self.data_directory, self.migrations_file_name)

    def get_host(self, service=None):
        if service is None:
            service = self.service
        return self.all_services.get(service).get(Config.CONF_HOST)

    def get_port(self, service=None):
        if service is None:
            service = self.service
        return self.all_services.get(service).get(Config.CONF_PORT)

    def get_service_url(self, service=None):
        if service is None:
            service = self.service
        return f'http://{self.get_host(service)}:{self.get_port(service)}'
