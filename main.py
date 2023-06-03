import time

from threading import Thread
from CEOptionsInstrumentListHandler import CEOptionsInstrumentListHandler
from PEOptionsInstrumentListHandler import PEOptionsInstrumentListHandler
from HistoricalDataFetcher import HistoricalDataFetcher
from KiteSession import KiteSessionSingleton
from InstrumentListFetcherSingleton import InstrumentListFetcherSingleton
from LiveMarketDataFetcher import LiveMarketDataFetcher
import HelperFunctions

from datetime import timedelta
from PlotGraph import plot_graph


def get_straddle_strike_details(dte, tf, strike_width, index):
    ce_list_handler = CEOptionsInstrumentListHandler(HelperFunctions.get_index_name_from_symbol(index))
    pe_list_handler = PEOptionsInstrumentListHandler(HelperFunctions.get_index_name_from_symbol(index))
    expiry_date = ce_list_handler.get_expiry_date()

    index_token = HelperFunctions.get_token_from_index_list(index, InstrumentListFetcherSingleton)

    if index_token == 0:
        print('Index not found')
        return

    index_open = \
        KiteSessionSingleton.get_connect_instance().historical_data(index_token, expiry_date - timedelta(dte),
                                                                    expiry_date, tf)[0]['open']

    index_open = HelperFunctions.calculate_closest_trade_able_level(index_open, strike_width)

    ce_symbol_details = ce_list_handler.get_symbol_details(str(int(index_open)))
    pe_symbol_details = pe_list_handler.get_symbol_details(str(int(index_open)))

    return ce_symbol_details, pe_symbol_details, expiry_date


def fetch_and_save_options_data(dte, tf, strike_width, index):
    ce_symbol_details, pe_symbol_details, expiry_date = get_straddle_strike_details(dte, tf, strike_width, index)
    ce_hist_data_fetcher = HistoricalDataFetcher(tf, dte, expiry_date, ce_symbol_details['instrument_token'])
    ce_hist = ce_hist_data_fetcher.generate_historical_data()

    pe_hist_data_fetcher = HistoricalDataFetcher(tf, dte, expiry_date, pe_symbol_details['instrument_token'])
    pe_hist = pe_hist_data_fetcher.generate_historical_data()

    # test_ticker(ce_symbol_details['instrument_token'], pe_symbol_details['instrument_token'])
    plot_graph(ce_hist, pe_hist)
    pe_hist_data_fetcher.save_to_folder(pe_symbol_details['tradingsymbol'])
    ce_hist_data_fetcher.save_to_folder(ce_symbol_details['tradingsymbol'])


def test_ticker(new_token1, new_token2):
    fetcher = LiveMarketDataFetcher()
    fetcher.start_fetching()
    fetcher.subscribe_new_token(new_token2)
    time.sleep(5)
    fetcher.subscribe_new_token(new_token1)


def initiate():
    # test_ticker()
    # plot_graph()
    # fetch_and_save_options_data(0, 'minute', 100, 'NIFTY BANK')
    # fetch_and_save_options_data(6, '5minute', 100, 'NIFTY BANK')
    # fetch_and_save_options_data(13, '5minute', 100, 'NIFTY BANK')
    # fetch_and_save_options_data(20, '5minute', 100, 'NIFTY BANK')
    # fetch_and_save_options_data(27, '5minute', 100, 'NIFTY BANK')
    # fetch_and_save_options_data(34, '5minute', 100, 'NIFTY BANK')
    # fetch_and_save_options_data(41, '5minute', 100, 'NIFTY BANK')

    # fetch_and_save_options_data(0, 'minute', 50, 'NIFTY 50')
    # fetch_and_save_options_data(6, '5minute', 50, 'NIFTY 50')
    # fetch_and_save_options_data(13, '5minute', 50, 'NIFTY 50')
    # fetch_and_save_options_data(20, '5minute', 50, 'NIFTY 50')
    # fetch_and_save_options_data(27, '5minute', 50, 'NIFTY 50')
    # fetch_and_save_options_data(34, '5minute', 50, 'NIFTY 50')
    # fetch_and_save_options_data(41, '5minute', 50, 'NIFTY 50')

    # fetch_and_save_options_data(6, '5minute', 50, 'NIFTY FIN SERVICE')
    fetch_and_save_options_data(6, 'minute', 50, 'NIFTY FIN SERVICE')


if __name__ == '__main__':
    initiate()
