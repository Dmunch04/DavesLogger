from DavesLogger import Color
from DavesLogger.Logger import Log

Debug = Log ('DEBUG MESSAGE', Color.LightPurple + '[Debug] ')
Warning = Log ('WARNING MESSAGE', Color.LightYellow + '[WARNING] ')
Error = Log ('ERROR MESSAGE', Color.LightRed + '[ERROR] ')
Success = Log ('SUCCESS MESSAGE', Color.LightGreen + '[SUCCESS] ')
