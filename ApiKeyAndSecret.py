APIKEY = 'your api key'
APISECRET = 'your api secret'


class ApiKeyAndSecret:
    _api_key = APIKEY
    _api_secret = APISECRET

    def get_api_key(self):
        return self._api_key

    def get_api_secret(self):
        return self._api_secret

