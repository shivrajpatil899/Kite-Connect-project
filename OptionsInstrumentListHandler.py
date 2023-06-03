# from KiteSession import KiteSessionSingleton
from InstrumentListFetcherSingleton import InstrumentListFetcherSingleton


class OptionsInstrumentListHandler:
    # _kite_obj = None
    _symbol = ''
    _exchange_type = 'NFO'
    _instrument_list = None
    _instrument_type = None

    def __init__(self, symbol, instrument_type=None):
        # self._kite_obj = KiteSessionSingleton.get_connect_instance()
        self._symbol = symbol
        self._instrument_type = instrument_type
        self._instrument_list = InstrumentListFetcherSingleton.get_options_list()
        self._rearrange_instrument_list()

    def _rearrange_instrument_list(self):
        result = []
        for dictionary in self._instrument_list:
            if self._symbol in dictionary['tradingsymbol']:
                if self._instrument_type == dictionary['instrument_type']:
                    result.append(dictionary)

        self._instrument_list = sorted(result, key=lambda t: t['expiry'])

    def get_expiry_date(self, forward_expiry=0):
        expiry = None
        for i in range(len(self._instrument_list)):
            if expiry != self._instrument_list[i]['expiry']\
                    and forward_expiry >= 0:
                expiry = self._instrument_list[i]['expiry']
                if forward_expiry == 0:
                    break
                else:
                    forward_expiry -= 1
        return expiry

    def get_symbol_details(self, strike_price, forward_expiry=0):
        result = []
        for dictionary in self._instrument_list:
            if strike_price in dictionary['tradingsymbol'] and forward_expiry >= 0:
                result = dictionary
                if forward_expiry == 0:
                    break
                else:
                    forward_expiry -= 1
        return result
