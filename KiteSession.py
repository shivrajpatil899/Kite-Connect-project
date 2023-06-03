from kiteconnect import KiteConnect, KiteTicker
from ApiKeyAndSecret import ApiKeyAndSecret
from LoginAndAuthenticator import LoginAndAuthenticator


class KiteSessionSingleton:
    __kite_connect_instance = None
    __kite_ticker_instance = None
    __access_token = ''

    @staticmethod
    def get_connect_instance():
        if KiteSessionSingleton.__kite_connect_instance is None:
            KiteSessionSingleton.__create_connect_session()
        return KiteSessionSingleton.__kite_connect_instance

    @staticmethod
    def get_ticker_instance():
        KiteSessionSingleton.get_connect_instance()
        if KiteSessionSingleton.__kite_ticker_instance is None:
            KiteSessionSingleton.__create_ticker_session()
        return KiteSessionSingleton.__kite_ticker_instance

    @staticmethod
    def __create_connect_session():
        api_key_and_secret_obj = ApiKeyAndSecret()
        KiteSessionSingleton.__kite_connect_instance = KiteConnect(api_key=api_key_and_secret_obj.get_api_key())
        login_auth_obj = LoginAndAuthenticator(KiteSessionSingleton.__kite_connect_instance)
        login_auth_obj.start_login_and_auth()
        auth_data = KiteSessionSingleton.__kite_connect_instance.generate_session(login_auth_obj.get_request_token(), api_secret=api_key_and_secret_obj.get_api_secret())
        KiteSessionSingleton.__access_token = auth_data["access_token"]
        KiteSessionSingleton.__kite_connect_instance.set_access_token(KiteSessionSingleton.__access_token)

    @staticmethod
    def __create_ticker_session():
        api_key_and_secret_obj = ApiKeyAndSecret()
        KiteSessionSingleton.__kite_ticker_instance = KiteTicker(api_key=api_key_and_secret_obj.get_api_key(), access_token=KiteSessionSingleton.__access_token)
