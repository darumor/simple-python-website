import os


class Config:

    config = None

    ENV_DATABASE_FILENAME = 'SPW_DATABASE_FILENAME'
    ENV_MIGRATIONS_FILENAME = 'SPW_MIGRATIONS_FILENAME'
    ENV_DATA_DIRECTORY = 'SPW_DATA_DIRECTORY'
    ENV_STATIC_FILES_DIRECTORY = 'SPW_STATIC_FILES_DIRECTORY'
    ENV_COOKIE_SECRET = 'SPW_COOKIE_SECRET'
    ENV_PASSWORD_SECRET = 'SPW_PASSWORD_SECRET'
    ENV_PORT = 'SPW_PORT'
    ENV_SESSION_TTL = 'SPW_SESSION_TTL'

    defaults = dict(
        SPW_MIGRATIONS_FILENAME='migrations.json',
        SPW_DATA_DIRECTORY='data',                  # should be an absolute path
        SPW_STATIC_FILES_DIRECTORY='static',        # should be an absolute path
        SPW_COOKIE_SECRET='some-secret-value',
        SPW_PASSWORD_SECRET='some-other-secret-value',
        SPW_PORT=9999,
        SPW_SESSION_TTL=10
    )

    def __init__(self,
                 migrations_filename=None,
                 data_directory=None,
                 static_files_directory=None,
                 cookie_secret=None,
                 password_secret=None,
                 port=None,
                 session_ttl=None):
        self.migrations_filename = migrations_filename or os.getenv(Config.ENV_MIGRATIONS_FILENAME) or Config.defaults[Config.ENV_MIGRATIONS_FILENAME]
        self.data_directory = data_directory or os.getenv(Config.ENV_DATA_DIRECTORY) or Config.defaults[Config.ENV_DATA_DIRECTORY]
        self.static_files_directory = static_files_directory or os.getenv(Config.ENV_STATIC_FILES_DIRECTORY) or Config.defaults[Config.ENV_STATIC_FILES_DIRECTORY]
        self.cookie_secret = cookie_secret or os.getenv(Config.ENV_COOKIE_SECRET) or Config.defaults[Config.ENV_COOKIE_SECRET]
        self.password_secret = password_secret or os.getenv(Config.ENV_PASSWORD_SECRET) or Config.defaults[Config.ENV_PASSWORD_SECRET]
        self.port = port or os.getenv(Config.ENV_PORT) or Config.defaults[Config.ENV_PORT]
        self.session_ttl = session_ttl or os.getenv(Config.ENV_SESSION_TTL) or Config.defaults[Config.ENV_SESSION_TTL]
        Config.config = self
