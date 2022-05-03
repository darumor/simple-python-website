from common.network.network import Network
from common.config import Config
import datetime
import hashlib


class Token:

    def __init__(self, user=None, user_ip=None, rights=None, service=None, timestamp=None, signature=None):
        if service is None and (user is None or user_ip is None):
            raise ValueError('Can not create a Token: Not enough info')
        elif service is not None and (user is not None or user_ip is not None):
            raise ValueError('Can not create a Token: Too much info')
        self.user = user
        self.user_ip = user_ip
        self.rights = rights
        self.service = service
        self.timestamp = timestamp
        self.signature = signature

    def to_dict(self):
        return dict(
            token_user=str(self.user),
            token_user_ip=str(self.user_ip),
            token_rights=str(self.rights),
            token_service=str(self.service),
            token_timestamp=str(self.timestamp.isoformat()),
            token_signature=str(self.signature)
        )

    @staticmethod
    def parse(query_params):
        return Token(
            user=query_params['token_user'],
            user_ip=query_params['token_user_ip'],
            rights=dict(query_params['token_rights'] or {}),
            service=query_params['token_service'],
            timestamp=datetime.datetime.fromisoformat(query_params['token_timestamp']),
            signature=query_params['token_signature']
        )


    def is_signed(self):
        return self.timestamp is not None and self.signature is not None

    def signature_is_valid(self, config):
        return self.signature == self.create_signature(self.timestamp, config)

    def to_signable_str(self):
        if self.service is not None:
            return f'{self.service}'
        else:
            return f'{self.user}|{self.user_ip}|{self.rights}'

    def create_signature(self, timestamp, config):
        secret = config.token_secret
        module = hashlib.md5()
        string = f'{self.to_signable_str()}|{timestamp}|{secret}'
        module.update(bytes(string, encoding='utf-8'))
        return module.hexdigest()

    def sign(self, config):
        timestamp = datetime.datetime.now()
        self.timestamp = timestamp
        self.signature = self.create_signature(timestamp, config)

    def is_valid(self, config):
        return self.signature_is_valid(config) and not self.is_expired()

    def is_valid_service_token(self, config):
        # print(str(self.to_dict()))
        return self.is_valid(config) and self.service is not None

    def is_expiring(self):
        now = datetime.datetime.now()
        return self.timestamp - datetime.timedelta(minutes=5) < now < self.timestamp

    def is_expired(self):
        return datetime.datetime.now() > self.timestamp

    def renew(self, config):
        if self.is_expiring():
            self.sign(config)

    @staticmethod
    def create_service_token(service, config):
        token = Token(service=service)
        token.sign(config)
        return token




