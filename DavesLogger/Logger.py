from DavesLogger import Color
from DavesLogger import Logs

class Log:
    def __init__ (self, Message = '', Prefix = '', Suffix = ''):
        self.Message = Message
        self.IPrefix = Prefix
        self.ISuffix = Suffix

    def __call__ (self, _Message = '', _AutoReset = True):
        if _Message != '' and _Message != None:
            if _AutoReset:
                print (self.IPrefix + Color.Reset + _Message + Color.Reset + self.ISuffix + Color.Reset)

            else:
                print (self.IPrefix + _Message + self.ISuffix)

        else:
            if _AutoReset:
                print (self.IPrefix + Color.Reset + self.Message + Color.Reset + self.ISuffix + Color.Reset)

            else:
                print (self.IPrefix + self.Message + self.ISuffix)

    def Template (self, _Template):
        if not isinstance (_Template, Log):
            Logs.Error ('No template found!')
            return

        return Log (_Template.Message, _Template.IPrefix, _Template.ISuffix)

    def Prefix (self, _Prefix):
        return Log (self.Message, self.IPrefix + _Prefix, self.ISuffix)

    def Suffix (self, _Suffix):
        return Log (self.Message, self.IPrefix, self.ISuffix + _Suffix)
