from DavesLogger import Color
from DavesLogger.Logger import Log

Debug = Log ('DEBUG MESSAGE', Color.LightPurple + '[Debug] ')
Warning = Log ('WARNING MESSAGE', Color.LightYellow + '[Debug] ')
Error = Log ('ERROR MESSAGE', Color.LightRed + '[Debug] ')
Success = Log ('SUCCESS MESSAGE', Color.LightGreen + '[Debug] ')
