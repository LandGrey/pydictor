#!/usr/bin/env python
# coding:utf-8
# store some text
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
from collections import OrderedDict
from lib.fun import cool


pydictor_ascii_text_0 = '''
                                ##
                #####            #   #
                 #   #           #            #
                 #   # ## ##  ####  ##   ### ###   ###  ## #
                 ####   # #  #   #   #  #  #  #   #   #  ##
                 #      # #  #   #   #  #     #   #   #  #
                 #       #   #  ##   #  #     #   #   #  #
                ###      #    ## ## ###  ###   ##  ###  ###
                       # #
                       ##
'''


pydictor_ascii_text_2 = '''
             _______                __   _          _
            |_   __ \              |  ] (_)        / |_
              | |__) |_   __   .--.| |  __   .---.`| |-' .--.   _ .--.
              |  ___/[ \ [  ]/ /'`\' | [  | / /'`\]| | / .'`\ \[ `/'`\]
             _| |_    \ '/ / | \__/  |  | | | \__. | |,| \__. | | |
            |_____| [\_:  /   '.__.;__][___]'.___.'\__/ '.__.' [___]
                     \__.'
'''

pydictor_ascii_text_3 = '''
                             o
                            O  o
                            o             O
                            o            oOo
            .oOo. O   o .oOoO  O  .oOo    o   .oOo. `OoOo.
            O   o o   O o   O  o  O       O   O   o  o
            o   O O   o O   o  O  o       o   o   O  O
            oOoO' `OoOO `OoO'o o' `OoO'   `oO `OoO'  o
            O         o
            o'     OoO'
'''

helpmsg = '''
                       {0}
                                                                {1}
    ----------------------------------[ {2} ]------------------------------------
    [+]help desc     (View the description) |  [+]show setting  (Show current settings)
    [+]cls/clear     (Clean the screen)     |  [+]quit/exit     (Quit the progress)
    [+]run           (Build the dictionary) |
                                            |
    Usage Exp :show  (Show all of settings) |  help desc   (view all of descriptions)

    -------------------------------[ {3} ]--------------------------------
    [+]cname      [+]ename      [+]sname    |  [+]birth      [+]usedpwd    [+]phone
    [+]uphone     [+]hphone     [+]email    |  [+]postcode   [+]nickname   [+]idcard
    [+]jobnum     [+]otherdate  [+]usedchar |
                                            |
    Usage Exp :sname zhang wei zw zwell     |  * Each setting supports multiple values
'''.format(cool.orange("Social Engineering Dictionary Builder"), cool.green("Build by LandGrey"), cool.yellow("command")
           , cool.yellow("setting options"))

settings_dict = OrderedDict([
    ('cname', []), ('ename', []), ('sname', []), ('birth', []),
    ('usedpwd', []), ('phone', []), ('uphone', []), ('hphone', []),
    ('email', []), ('postcode', []), ('nickname', []), ('idcard', []),
    ('jobnum', []), ('otherdate', []), ('usedchar', [])
    ]
)

help_dict = OrderedDict([
    # settings help message
    ('cname', "cname      Chinese name's phonetic          中文名拼音全拼"),
    ('ename', "ename      English name                     英文名"),
    ('sname', "sname      Simple spellings phonetic        姓名简拼"),
    ('birth', "birth      Birthday [YYYYMMDD]              生日"),
    ('usedpwd', "usedpwd    Used password                    曾用密码"),
    ('phone', "phone      Cell phone number                手机号"),
    ('uphone', "uphone     Used phone                       曾用手机号"),
    ('hphone', "hphone     Homephone number                 家庭座机号"),
    ('email', "email      E-mail accounts                  电子邮箱账号"),
    ('postcode', "postcode   Postcode                         家庭邮政编码"),
    ('nickname', "nickname   Commonly used nickname           常用昵称"),
    ('idcard', "idcard     Identity card number             身份证号"),
    ('jobnum', "jobnum     Job or student number            学号或工号或其简写等"),
    ('otherdate', "otherdate  Others date [YYYYMMDD]           其他亲人生日等特殊日期"),
    ('usedchar', "usedchar   Commonly used characters         其他社交平台账号等常用字符")
    ])
