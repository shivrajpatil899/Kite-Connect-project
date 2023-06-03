index_contract_name_dict = {'NIFTY BANK': 'BANKNIFTY',
                            'NIFTY FIN SERVICE': 'FINNIFTY',
                            'NIFTY 50': 'NIFTY'}


def get_index_name_from_symbol(index_name):
    return index_contract_name_dict[index_name]


def calculate_closest_trade_able_level(open_val, strike_width):
    rem = open_val % strike_width
    if rem < strike_width / 2:
        calculate_level = open_val - rem
    else:
        calculate_level = open_val + strike_width - rem
    return calculate_level


def get_token_from_index_list(index, list_fetcher):
    index_token = 0
    for dictionary in list_fetcher.get_index_list():
        if index == dictionary['tradingsymbol']:
            index_token = dictionary['instrument_token']
    return index_token
