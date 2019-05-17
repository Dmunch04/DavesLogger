# DavesLogger
> A simple but in depth logger for Python, Customize by Composition.

The idea for this tool is composing logging functions, so you can make the logs look exactly how you want or need them to.

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
