from KiteSession import KiteSessionSingleton
from threading import Thread


class LiveMarketDataFetcher:
    __kite_ticker_instance = None
    __tick_data = []
    subscribed_tokens = []
    __web_socket = None
    __subscribed_tokens_changed = False
    __fetching_process_thread = None

    def __init__(self):
        self.__kite_ticker_instance = KiteSessionSingleton.get_ticker_instance()
        # self.__kite_ticker_instance.on_close = self.on_close
        self.__fetching_process_thread = Thread(target=self.monitor_tokens_process)

    def on_ticks(self, ws, ticks):
        self.__tick_data.append(ticks)
        print(ticks)

    def on_connect(self, ws, response):
        self.__web_socket = ws
        ws.subscribe(LiveMarketDataFetcher.subscribed_tokens)

    # def on_close(self, ws, code, reason):
    #     print("closed")

    def subscribe_new_token(self, token_number):
        LiveMarketDataFetcher.subscribed_tokens.append(token_number)
        self.__subscribed_tokens_changed = True

    def unsubscribe_existing_token(self, token_number):
        LiveMarketDataFetcher.subscribed_tokens.remove(token_number)

    def monitor_tokens_process(self):
        while True:
            if self.__kite_ticker_instance.is_connected() and self.__subscribed_tokens_changed:
                self.__subscribed_tokens_changed = False
                print(LiveMarketDataFetcher.subscribed_tokens)
                self.__web_socket.subscribe(LiveMarketDataFetcher.subscribed_tokens)

    def start_fetching(self):
        self.__fetching_process_thread.start()
        self.__kite_ticker_instance.on_ticks = self.on_ticks
        self.__kite_ticker_instance.on_connect = self.on_connect
        self.__kite_ticker_instance.connect(threaded=True)
        # self.__fetching_process_thread.join()

    def get_recorded_tick_data(self):
        return self.__tick_data
