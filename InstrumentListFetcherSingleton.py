from KiteSession import KiteSessionSingleton


class InstrumentListFetcherSingleton:
    __options_list = list()
    __indices_list = list()
    __equities_list = list()

    @staticmethod
    def __create_lists():
        InstrumentListFetcherSingleton.__equities_list = KiteSessionSingleton.get_connect_instance().instruments()
        for indices_dict in InstrumentListFetcherSingleton.__equities_list:
            if 'INDICES' in indices_dict['segment']:
                InstrumentListFetcherSingleton.__indices_list.append(indices_dict)
        InstrumentListFetcherSingleton.__options_list = KiteSessionSingleton.get_connect_instance().instruments(
            KiteSessionSingleton.get_connect_instance().EXCHANGE_NFO)

    @staticmethod
    def get_equities_list():
        if not InstrumentListFetcherSingleton.__equities_list:
            InstrumentListFetcherSingleton.__create_lists()
        return InstrumentListFetcherSingleton.__equities_list

    @staticmethod
    def get_options_list():
        if not InstrumentListFetcherSingleton.__options_list:
            InstrumentListFetcherSingleton.__create_lists()
        return InstrumentListFetcherSingleton.__options_list

    @staticmethod
    def get_index_list():
        if not InstrumentListFetcherSingleton.__indices_list:
            InstrumentListFetcherSingleton.__create_lists()
        return InstrumentListFetcherSingleton.__indices_list
