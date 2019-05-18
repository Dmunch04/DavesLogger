# DavesLogger
> A simple but in depth logger for Python, Customize by Composition.

The idea for this tool is composing logging functions, so you can make the logs look exactly how you want or need them to.

<a href = 'https://www.npmjs.com/package/logger3'>Dave's logger3<a/>, but written in Python

# Usage
You just import the package, and call log.
```py
from DavesLogger import Log

Log ('Hello, World!') ()

# This would print:
# Hello, World!
```

That's not interesting, lets compose a simple prefix in front of the message.
```py
from DavesLogger import Log

Prefixed = Log ().Prefix ('[DEBUG] ')

Prefixed ('Hello World, Debug Edition')

# This would print:
# [DEBUG] Hello World, Debug Edition
```

You can also chain the logging modifiers
```py
from DavesLogger import Log

Prefixed = Log ().Prefix ('[DEBUG] ').Suffix (' [SUFFIX])

Prefixed ('Hello World, Debug Edition')

# This would print:
# [DEBUG] Hello World, Debug Edition [SUFFIX]
```

There are also a bunch of built in formatters, and colors. Colors are based on the `colorama` module, so you can use their api of chaining properties.
```py
from DavesLogger import Log, Color

Prefixed = Log ().Prefix (Color.LightRed + '[DEBUG] ').Suffix (Color.LightGreen + ' [SUFFIX])

Prefixed (Color.Blue + 'Hello World, Debug Edition')

# This would print:
# [DEBUG] Hello World, Debug Edition [SUFFIX]
# But colored ^^
```

Or you can call some premade logs
```py
from DavesLogger import Logs

MyLog = Logs.Debug
MyLog ()

# This would print:
# [DEBUG] DEBUG MESSAGE
# But colored ^^
```

You can event also change the text of premade logs!
```py
from DavesLogger import Logs

MyLog = Logs.Debug
MyLog ('My custom debug message')

# This would print:
# [DEBUG] My custom debug message
# But colored ^^
```

# Log Object
A log object has the following attributes:
- Message
- IPrefix
- ISuffix

And the following functions:
- Template
- Prefix
- Suffix

How the attributes work
```py
from DavesLogger import Log

MyLog = Log ()
MyLog.Message = 'Hello!'
MyLog.IPrefix = '[Test] '
MyLog ()

# This would print:
# [Test] Hello!
```

The template function lets you load specific settings for your log
```py
from DavesLogger import Log, Logs

MyLog = Log ().Template (Logs.Debug)
# This is the same as doing:
MyLog = Logs.Debug
```

The `Prefix` and `Suffix` function appends a new prefix or suffix to the current logs prefix or suffix.

# Format
Format attributes:
- Time :: The current time
- Date :: The current date
- FullDate :: The current date and time
- Platform :: All info about the OS
- System :: The OS
- Release :: The release of the OS
- Version :: The version of the OS

Example use of the attribues:
```py
from DavesLogger import Logs, Format

MyLog = Logs.Server.Prefix (f'[{Format.Time}] ')
MyLog ()

# This would print:
# [SERVER] [20:57:18.633029] SERVER MESSAGE
# But colored ^^
# *The time may vary!*
```

You can also use the Formats `Format` function
```py
from DavesLogger import Logs, Format, Color

MyLog = Logs.Server.Prefix (Format.Format (f'[{Format.Time}] ', Color.Red))
MyLog ()

# This would print:
# [SERVER] [20:57:18.633029] SERVER MESSAGE
# But colored ^^
# *The time may vary!*
```

# Colors
- Reset
- End (Same as Reset)
- White
- LightGray
- Gray
- Black
- Red
- LightRed
- Blue
- LightBlue
- Green
- LightGreen
- Yellow
- LightYellow
- Purple
- LightPurple
- Cyan

# Premade Logs
- Debug :: `[DEBUG] DEBUG MESSAGE` >> The Prefix is LightPurple
- Warning :: `[WARNING] WARNING MESSAGE` >> The Prefix is LightYellow
- Error :: `[ERROR] ERROR MESSAGE` >> The Prefix is LightRed
- Success :: `[SUCCESS] SUCCESS MESSAGE` >> The Prefix is LightGreen
- Server :: `[SERVER] SERVER MESSAGE` >> The prefix is LightBlue
