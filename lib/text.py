#!/usr/bin/env python
# coding:utf-8
# Store some text
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
from collections import OrderedDict
from lib.data import sedb_range
from lib.fun import cool


pydictor_ascii_text = '''
             _______                __   _          _
            |_   __ \              |  ] (_)        / |_
              | |__) |_   __   .--.| |  __   .---.`| |-' .--.   _ .--.
              |  ___/[ \ [  ]/ /'`\' | [  | / /'`\]| | / .'`\ \[ `/'`\]
             _| |_    \ '/ / | \__/  |  | | | \__. | |,| \__. | | |
            |_____| [\_:  /   '.__.;__][___]'.___.'\__/ '.__.' [___]
                     \__.'
'''


helpmsg = '''
                       {0}
                                                                {1}
    ----------------------------------[ {2} ]------------------------------------
    [+]help desc     (View the description) |  [+]show name     (Show current settings)
    [+]cls/clear     (Clean the screen)     |  [+]quit/exit     (Quit the progress)
    [+]run           (Build the dictionary) |
                                            |
    Usage Exp :show  (Show all of settings) |  help desc   (view all of descriptions)

    -------------------------------[ {3} ]--------------------------------
    [+]{4}      [+]{5}      [+]{6}    |  [+]{7}      [+]{8}    [+]{9}
    [+]{10}     [+]{11}     [+]{12}    |  [+]{13}   [+]{14}   [+]{15}
    [+]{16}     [+]{17}  [+]{18} |
                                            |
    Usage Exp :sname zhang wei zw zwell     |  * Each setting supports multiple values
'''.format(cool.orange("Social Engineering Dictionary Builder"), cool.green("Build by LandGrey"), cool.yellow("command")
           , cool.yellow("setting options"), sedb_range[0], sedb_range[1], sedb_range[2], sedb_range[3], sedb_range[4],
           sedb_range[5], sedb_range[6], sedb_range[7], sedb_range[8], sedb_range[9], sedb_range[10], sedb_range[11],
           sedb_range[12], sedb_range[13], sedb_range[14], )

settings_dict = OrderedDict([
    (sedb_range[0], []), (sedb_range[1], []), (sedb_range[2], []), (sedb_range[3], []), (sedb_range[4], []),
    (sedb_range[5], []), (sedb_range[6], []), (sedb_range[7], []), (sedb_range[8], []), (sedb_range[9], []),
    (sedb_range[10], []), (sedb_range[11], []), (sedb_range[12], []), (sedb_range[13], []), (sedb_range[14], [])
    ]
)

help_dict = OrderedDict([
    # settings help message
    (sedb_range[0], " {:10}     Chinese name's phonetic        中文名拼音全拼".format(sedb_range[0])),
    (sedb_range[1], " {:10}     English name                   英文名".format(sedb_range[1])),
    (sedb_range[2], " {:10}     Simple name spellings          姓名简拼".format(sedb_range[2])),
    (sedb_range[3], " {:10}     Birthday [yyyyMMdd]            生日".format(sedb_range[3])),
    (sedb_range[4], " {:10}     Used password                  曾用密码".format(sedb_range[4])),
    (sedb_range[5], " {:10}     Cell phone number              手机号".format(sedb_range[5])),
    (sedb_range[6], " {:10}     Previous phone number          曾用手机号".format(sedb_range[6])),
    (sedb_range[7], " {:10}     HomePhone number               家庭座机号".format(sedb_range[7])),
    (sedb_range[8], " {:10}     Email accounts                 电子邮箱账号".format(sedb_range[8])),
    (sedb_range[9], " {:10}     Postal code                    家庭邮政编码".format(sedb_range[9])),
    (sedb_range[10], " {:10}     Commonly used nickname         常用昵称".format(sedb_range[10])),
    (sedb_range[11], " {:10}     Identity card number           身份证号".format(sedb_range[11])),
    (sedb_range[12], " {:10}     Job or student number          学号或工号或其简写等".format(sedb_range[12])),
    (sedb_range[13], " {:10}     Others date [yyyyMMdd]         其他亲人生日等特殊日期".format(sedb_range[13])),
    (sedb_range[14], " {:10}     Commonly used characters       其他社交平台账号等常用字符".format(sedb_range[14]))
    ])

