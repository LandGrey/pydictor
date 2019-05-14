## pydictor API developer document

### *plugin*

#### step 0:
create "name.py" script in /plugins/ folder:

#### step 1:
import following modules and write author name:
```
#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from lib.fun.fun import cool
from lib.fun.decorator import magic
from lib.data.data import pyoptions

```

#### step 2:
define "name_magic(*args)" function, and write function usage doc、get args value:
```
def name_magic(*args):
    """[keyword1] [keyword2] ..."""
    args = list(args[0])
```

#### step 3:
handle the exception arguments that user input:
```
if len(args) == 1:
    exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.plugins_info.get(args[0]))))
```

#### step 4:
use "magic" decorator, warp "name()" function:
```
@magic
def name():
```

#### step 5:
in "name()" function, generate your wordlist(python list type) or yield the values:
```
results = []

append something to results ...

retrun results
```
or
```
results is python generator

for r in results:
    yield r
```
if you want to add your own weak password wordlist in final word list,
there some folders you can put your wordlist (defined in /lib/data/data.py script)

|  path              | variable             |                 
| :----------------  | :------------------- |
|  /wordlist         | paths.wordlist_path  |
|  /wordlist/App     | paths.applist_path   |
|  /wordlist/IoT     | paths.iotlist_path   |
|  /wordlist/NiP     | paths.niplist_path   |
|  /wordlist/SEDB    | paths.sedblist_path  |
|  /wordlist/Sys     | paths.syslist_path   |
|  /wordlist/Web     | paths.weblist_path   |
|  /wordlist/WiFi    | paths.wifilist_path  |

use it like:
```
from lib.data.data import paths
from lib.fun.fun import walks_all_files

@magic
def name():
    for _ in walks_all_files(paths.weblist_path):
        yield "".join(_)
```

##### now, your script supported all hand functions in pydictor

##### if it's "/plugins/ftp.py" script, and it's name must be "ftp", a simple example:

```
#!/usr/bin/env python
# coding:utf-8
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from lib.fun.fun import cool
from lib.fun.decorator import magic
from lib.data.data import pyoptions


def ftp_magic(*args):
    """[keyword1] [keyword2] ..."""
    args = list(args[0])
    if len(args) == 1:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.plugins_info.get(args[0]))))

    @magic
    def ftp():
        results = []
        default_password = ('ftp', 'anonymous', 'any@', 'craftpw', 'xbox', 'r@p8p0r+', 'pass', 'admin',
                            'lampp', 'password', 'Exabyte', 'pbxk1064', 'kilo1987', 'help1954', 'tuxalize')
        results += default_password
        weak_password = ('root', '123456', '111111', '666666', 'ftppass')
        results += weak_password
        for r in results:
            yield r

        tails = ['1', '01', '001', '123', 'abc', '!@#', '!QAZ', '1q2w3e', '!@#$', '!', '#', '.', '@123',
                 '2016', '2017', '2018', '@2016', '@2017', '@2018', ]
        for keyword in args:
            for tail in tails:
                yield keyword + tail
```

#### call ftp plugin, with command "python pydictor.py -plug ftp \[keyword1\] \[keyword2\] ..."
#

### *tool*
same as plugin api, except

```
place script in "/tools/" folder
```

#### call tool with command "python pydictor.py -tool name \[some_args\]"
#

### *encode*
just write your python script in "/lib/encode/" folder, and

```
1. script file name end with "_encode", like "name_encode.py"
2. function name must same to script file name, like "def name_encode(item)"
3. function "name_encode(item)" next line must be function usage tips and wrap with """
4. return item after your encode
```

#### an example for "base64" encode function:
create "b64_encode.py" file in "/lib/encode/" folder, and write code:

```
#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

from base64 import b64encode


def b64_encode(item):
    """base64 encode"""
    try:
        return (b64encode(item.encode('utf-8'))).decode()
    except:
        return ''

```

#### call encode function with command "python pydictor.py --encode name"
