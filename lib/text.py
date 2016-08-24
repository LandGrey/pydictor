#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-08-23
#
# store text for others import
#

helpmsg = "               Social Engineering Dictionary Builder\n" \
                  "                                                              Build by LandGrey\n"\
                  "----------------------------------[ command ]------------------------------------\n"\
                  "[+]help [options](View help message)    |  [+]show [setting](Show current settings)\n"\
                  "[+]cls/clear     (Clean the screen)     |  [+]quit/exit     (Quit the progress)\n"\
                  "[+]run           (Build the dictionary) |\n"\
                  "Usage Exp :show  (Show all of settings) |  help settings    (View all of setings help)\n"\
                  "----------------------------------[ settings ]------------------------------------\n"\
                  "[+]cname      [+]ename      [+]sname    |  [+]birth      [+]usedpwd    [+]phone   \n"\
                  "[+]uphone     [+]hphone     [+]email    |  [+]postcode   [+]nickname   [+]idcard  \n"\
                  "[+]jobnum     [+]otherid    [+]usedchar | \n"\
                  "Usage Exp :nickname zs zhangs zsan      |  *Each setting supports multiple values"


settings_dict = {
    'cname': [], 'ename': [], 'sname': [], 'birth': [],
    'usedpwd': [], 'phone': [], 'uphone': [], 'hphone': [],
    'email': [], 'postcode': [], 'nickname': [], 'idcard': [],
    'jobnum': [], 'otherid': [], 'usedchar': []}


help_dict = {
    # settings help message
    'cname': "[+]cname      Chinese name's phonetic          中文名拼音全拼\n".decode('utf-8'),
    'ename': "[+]ename      English name                     英文名\n".decode('utf-8'),
    'sname': "[+]sname      Simple spellings phonetic        姓名简拼\n".decode('utf-8'),
    'birth': "[+]birth      Birthday [YYYYMMDD]              生日\n".decode('utf-8'),
    'usedpwd': "[+]usedpwd    Used password                    曾用密码\n".decode('utf-8'),
    'phone': "[+]phone      Cell phone number                手机号\n".decode('utf-8'),
    'uphone': "[+]uphone     Used phone                       曾用手机号\n".decode('utf-8'),
    'hphone': "[+]hphone     Homephone number                 家庭座机号\n".decode('utf-8'),
    'email': "[+]email      E-mail accounts                  电子邮箱账号\n".decode('utf-8'),
    'postcode': "[+]postcode   Postcode                         家庭邮政编码\n".decode('utf-8'),
    'nickname': "[+]nickname   Commonly used nickname           常用昵称\n".decode('utf-8'),
    'idcard': "[+]idcard     Identity card number             身份证号\n".decode('utf-8'),
    'jobnum': "[+]jobnum     Job or student number            学号或工号或其简写等\n".decode('utf-8'),
    'otherid': "[+]otherid    Social network platform accounts 社交平台账号或昵称\n".decode('utf-8'),
    'usedchar': "[+]usedchar   Commonly used characters         其他常用字符串数字等\n".decode('utf-8')}




