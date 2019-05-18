from colorama import init
try:
    init ()

except:
    print ('Console color didn\'t load!')

import DavesLogger.Color
import DavesLogger.Format
import DavesLogger.Logs
import DavesLogger.Text
from DavesLogger.Logger import Log
