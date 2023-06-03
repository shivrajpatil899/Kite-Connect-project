from datetime import date, timedelta
from pathlib import Path
import pandas as pd

from KiteSession import KiteSessionSingleton


class HistoricalDataFetcher:
    _timeframe = ''
    _expiry_date = None
    _DTE = 0
    _kite = None
    _instrument_token = 0
    _historical_data_frames = []

    def __init__(self, tf, dte, expiry, token):
        self._kite = KiteSessionSingleton.get_connect_instance()
        self._timeframe = tf
        self._DTE = dte
        self._expiry_date = expiry
        self._instrument_token = token

    def set_dte(self, dte):
        self._DTE = dte

    def generate_historical_data(self):
        self._historical_data_frames = self._kite.historical_data(self._instrument_token,
                                                                  self._expiry_date-timedelta(self._DTE),
                                                                  self._expiry_date,
                                                                  self._timeframe)
        return self._historical_data_frames

    def save_to_folder(self, trading_symbol):
        df = pd.DataFrame(data=self._historical_data_frames)
        df.to_csv('output_csv/{}-{}-{}dte.csv'.format(date.today(), trading_symbol, self._DTE), index=False)
        df['date'] = df['date'].dt.tz_localize(None)

        file_name = 'output_excel/{}-{}dte.xlsx'.format(date.today(), self._DTE)
        if not Path(file_name).exists():
            df.to_excel(file_name, sheet_name='{}'.format(trading_symbol), index=False)
        else:
            with pd.ExcelWriter(file_name, engine="openpyxl", mode='a') as writer:
                df.to_excel(writer, sheet_name='{}'.format(trading_symbol), index=False)

