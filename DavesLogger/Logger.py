from DavesLogger import Color

class Log:
    def __init__ (self, Message = '', Prefix = '', Suffix = ''):
        self.Message = Message
        self.IPrefix = Prefix
        self.ISuffix = Suffix

    def __call__ (self, _Message = ''):
        if _Message != '':
            self.Message = _Message

        print (self.IPrefix + Color.Reset + self.Message + Color.Reset + self.ISuffix)

    def Message (self, _Message):
        self.Message += _Message
        return Log (self.Message, self.IPrefix, self.ISuffix)

    def Prefix (self, _Prefix):
        self.IPrefix += _Prefix
        return Log (self.Message, self.IPrefix, self.ISuffix)

    def Suffix (self, _Suffix):
        self.ISuffix += _Suffix
        return Log (self.Message, self.IPrefix, self.ISuffix)
