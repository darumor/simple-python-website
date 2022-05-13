import datetime
import hashlib


class Token:

    def __init__(self, user=None, user_ip=None, rights=None, service=None, valid_until=None, timestamp=None, signature=None):
        if service is None and (user is None or user_ip is None):
            raise ValueError('Can not create a Token: Not enough info')
        elif service is not None and (user is not None or user_ip is not None):
            raise ValueError('Can not create a Token: Too much info')
        self.user = user
        self.user_ip = user_ip
        self.rights = rights
        self.service = service
        self.valid_until = valid_until
        self.timestamp = timestamp
        self.signature = signature

    def to_dict(self):
        return dict(
            token_user=str(self.user),
            token_user_ip=str(self.user_ip),
            token_rights=str(self.rights),
            token_service=str(self.service),
            token_valid_until=str(self.valid_until),
            token_timestamp=str(self.timestamp.isoformat()),
            token_signature=str(self.signature)
        )

    @staticmethod
    def parse(query_params):
        for key in query_params.keys():
            print(f'{key}: {query_params[key]}')
            if query_params[key] == 'None':
                query_params[key] = None

        return Token(
            user=query_params['token_user'],
            user_ip=query_params['token_user_ip'],
            rights=query_params['token_rights'],
            valid_until=datetime.datetime.fromisoformat(query_params['token_valid_until']),
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
            return f'{self.service}|{self.valid_until}'
        else:
            return f'{self.user}|{self.user_ip}|{self.rights}|{self.valid_until}'

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
        return self.valid_until - datetime.timedelta(minutes=5) < now < self.valid_until

    def is_expired(self):
        return datetime.datetime.now() > self.valid_until

    def renew(self, config):
        if not self.is_expired():
            self.valid_until = datetime.datetime.now() + datetime.timedelta(minutes=config.session_ttl)
            self.sign(config)

    @staticmethod
    def create_service_token(service, config):
        valid_until = datetime.datetime.now() + datetime.timedelta(minutes=1)
        token = Token(service=service, valid_until=valid_until)
        token.sign(config)
        return token




