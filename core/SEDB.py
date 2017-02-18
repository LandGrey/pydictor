#!/usr/bin/env python
# coding:utf-8
# Social Engineering Dictionary Builder
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
from functools import reduce
import os
import cmd
from lib.text import help_dict, settings_dict, helpmsg, pydictor_ascii_text_2 as pydictor_art_text
from lib.data import get_result_store_path, get_buildtime, CRLF, SEDB_prefix, filextension
from lib.fun import finishprinter, finishcounter, is_Windows, is_Linux, is_Mac, cool
from rules.CBrule import CBrule
from rules.EBrule import EBrule
from rules.SBrule import SBrule
from rules.SingleRule import SingleRule
from rules.WeakPass import weak_pass_set


class SEDB(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.do_cls('')
        self.prompt = cool.green("pydictor SEDB>>")
        self.do_help('')

    def do_EOF(self):
        return True

    def do_help(self, key):
        if key in help_dict:
            print(cool.orange(help_dict[key]))
        elif key == 'desc':
            for k in help_dict.keys():
                print(cool.orange(help_dict[k]))
        else:
            self.do_cls('')
            print(cool.green(pydictor_art_text))
            print(helpmsg)

    def do_exit(self, args):
        return True

    def do_quit(self, args):
        return True

    def do_cls(self, line):
        if is_Windows():
            os.system("cls")
        elif is_Linux():
            os.system("clear")
        elif is_Mac():
            os.system("clear")

    def do_clear(self, line):
        self.do_cls(self)

    def do_cname(self, args):
        for item in str(args).split(' '):
            settings_dict['cname'].append(item)

    def do_ename(self, args):
        for item in str(args).split(' '):
            settings_dict['ename'].append(item)

    def do_sname(self, args):
        for item in str(args).split(' '):
            settings_dict['sname'].append(item)

    def do_birth(self, args):
        for item in str(args).split(' '):
            if len(item) != 8 or str(item).isdigit() is False:
                print(cool.fuchsia("[!] Input format:[YYYYMMDD] exp:19900512"))
            elif int(item[4:6]) > 12 or int(item[4:6]) < 1 or int(item[6:8]) > 31 or int(item[6:8]) < 1:
                print(cool.fuchsia("[!] Date format {1 <= month <= 12} and {1 <= day <=31}"))
            else:
                settings_dict['birth'].append(item)

    def do_usedpwd(self, args):
        for item in str(args).split(' '):
            settings_dict['usedpwd'].append(item)

    def do_phone(self, args):
        for item in str(args).split(' '):
            settings_dict['phone'].append(item)

    def do_uphone(self, args):
        for item in str(args).split(' '):
            settings_dict['uphone'].append(item)

    def do_hphone(self, args):
        for item in str(args).split(' '):
            settings_dict['hphone'].append(item)

    def do_email(self, args):
        for item in str(args).split(' '):
            settings_dict['email'].append(item)

    def do_postcode(self, args):
        for item in str(args).split(' '):
            settings_dict['postcode'].append(item)

    def do_nickname(self, args):
        for item in str(args).split(' '):
            settings_dict['nickname'].append(item)

    def do_idcard(self, args):
        for item in str(args).split(' '):
            if len(item) < 15:
                print(cool.fuchsia("[!] Identity card number length too short (should >=15)"))
            else:
                settings_dict['idcard'].append(item)

    def do_jobnum(self, args):
        for item in str(args).split(' '):
            settings_dict['jobnum'].append(item)

    def do_otherdate(self, args):
        for item in str(args).split(' '):
            if len(item) != 8 or str(item).isdigit() is False:
                print(cool.fuchsia("[!] Input format:[YYYYMMDD] exp:19900512"))
            else:
                settings_dict['otherdate'].append(item)

    def do_usedchar(self, args):
        for item in str(args).split(' '):
            settings_dict['usedchar'].append(item)

    def do_show(self, key):
        if key in settings_dict.keys():
            if type(settings_dict[key]) is str:
                print(cool.blue("%-10s :%s" % (key, settings_dict[key])))
            else:
                print(cool.blue("%-10s :%s" % (key, ' '.join([x for x in settings_dict[key]]))))
        else:
            for key in settings_dict.keys():
                print(cool.blue("%-10s :%s" % (key, ' '.join([x for x in settings_dict[key]]))))

    def do_run(self, args):
        results = []
        storepath = os.path.join(get_result_store_path(), '%s_%s%s' % (SEDB_prefix, get_buildtime(), filextension))
        with open(storepath, 'w') as f:
            # SingleRule
            for single in SingleRule(settings_dict['cname'], settings_dict['ename'], settings_dict['sname'],
                                     settings_dict['birth'], settings_dict['usedpwd'], settings_dict['phone'],
                                     settings_dict['uphone'], settings_dict['hphone'], settings_dict['email'],
                                     settings_dict['postcode'], settings_dict['nickname'], settings_dict['idcard'],
                                     settings_dict['jobnum'], settings_dict['otherdate'], settings_dict['usedchar']):
                results.append(single)
            # CBrule
            for cb in CBrule(settings_dict['cname'], settings_dict['birth']):
                results.append(cb)
            # EBrule
            for eb in EBrule(settings_dict['ename'], settings_dict['birth']):
                results.append(eb)
            # SBrule
            for sb in SBrule(settings_dict['sname'], settings_dict['birth']):
                results.append(sb)
            # WeakPass
            for weakpwd in weak_pass_set:
                results.append(weakpwd)

            # de-duplication
            for _ in reduce(lambda x, y: x if y in x else x + [y], [[], ] + results):
                f.write(_ + CRLF)
        finishprinter(finishcounter(storepath), storepath)

