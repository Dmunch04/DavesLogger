from DavesLogger import Color
import datetime
import platform

Time = datetime.datetime.now ().time ()
Date = datetime.datetime.now ().date ()
FullDate = datetime.datetime.now ()
Platform = platform.platform ()
System = platform.system ()
Release = platform.release ()
Version = platform.version ()

def Format (_Text, _Color, _Reset = True, _EndColor = None):
    if _Reset:
        return _Color + _Text + Color.Reset

    else:
        if _EndColor != None:
            return _Color + _Text + _EndColor

        else:
            return _Color + _Text
