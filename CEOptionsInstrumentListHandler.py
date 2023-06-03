from OptionsInstrumentListHandler import OptionsInstrumentListHandler


class CEOptionsInstrumentListHandler(OptionsInstrumentListHandler):
    def __init__(self, symbol):
        OptionsInstrumentListHandler.__init__(self, symbol, 'CE')
