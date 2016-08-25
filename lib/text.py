#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-08-25
#
# store text for others import
#
# This is a part of pydictor


from collections import OrderedDict

helpmsg = "               Social Engineering Dictionary Builder\n" \
                  "                                                              Build by LandGrey\n"\
                  "----------------------------------[ command ]------------------------------------\n"\
                  "[+]help [all]    (View help message)    |  [+]show [setting](Show current settings)\n"\
                  "[+]cls/clear     (Clean the screen)     |  [+]quit/exit     (Quit the progress)\n"\
                  "[+]run           (Build the dictionary) |\n"\
                  "Usage Exp :show  (Show all of settings) |  help settings    (View all of setings help)\n"\
                  "----------------------------------[ settings ]------------------------------------\n"\
                  "[+]cname      [+]ename      [+]sname    |  [+]birth      [+]usedpwd    [+]phone   \n"\
                  "[+]uphone     [+]hphone     [+]email    |  [+]postcode   [+]nickname   [+]idcard  \n"\
                  "[+]jobnum     [+]otherdate  [+]usedchar | \n"\
                  "Usage Exp :nickname zwell zhangs zsan   |  *Each setting supports multiple values"

settings_dict = OrderedDict([
    ('cname', []), ('ename', []), ('sname', []), ('birth', []),
    ('usedpwd', []), ('phone', []), ('uphone', []), ('hphone', []),
    ('email', []), ('postcode', []), ('nickname', []), ('idcard', []),
    ('jobnum', []), ('otherdate', []), ('usedchar', [])
    ]
)

help_dict = OrderedDict([
    # settings help message
    ('cname', "[+]cname      Chinese name's phonetic          中文名拼音全拼".decode('utf-8')),
    ('ename', "[+]ename      English name                     英文名".decode('utf-8')),
    ('sname', "[+]sname      Simple spellings phonetic        姓名简拼".decode('utf-8')),
    ('birth', "[+]birth      Birthday [YYYYMMDD]              生日".decode('utf-8')),
    ('usedpwd', "[+]usedpwd    Used password                    曾用密码".decode('utf-8')),
    ('phone', "[+]phone      Cell phone number                手机号".decode('utf-8')),
    ('uphone', "[+]uphone     Used phone                       曾用手机号".decode('utf-8')),
    ('hphone', "[+]hphone     Homephone number                 家庭座机号".decode('utf-8')),
    ('email', "[+]email      E-mail accounts                  电子邮箱账号".decode('utf-8')),
    ('postcode', "[+]postcode   Postcode                         家庭邮政编码".decode('utf-8')),
    ('nickname', "[+]nickname   Commonly used nickname           常用昵称".decode('utf-8')),
    ('idcard', "[+]idcard     Identity card number             身份证号".decode('utf-8')),
    ('jobnum', "[+]jobnum     Job or student number            学号或工号或其简写等".decode('utf-8')),
    ('otherdate', "[+]otherdate  Others date [YYYYMMDD]           其他亲人生日等特殊日期".decode('utf-8')),
    ('usedchar', "[+]usedchar   Commonly used characters         其他社交平台账号等常用字符".decode('utf-8'))
    ]
)

