from OptionsInstrumentListHandler import OptionsInstrumentListHandler


class PEOptionsInstrumentListHandler(OptionsInstrumentListHandler):
    def __init__(self, symbol):
        OptionsInstrumentListHandler.__init__(self, symbol, 'PE')
