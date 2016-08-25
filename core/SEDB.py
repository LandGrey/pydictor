#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-08-25
#
# Social Engineering Dictionary Builder
#
# This is a part of pydictor


import os
import sys
import cmd
import time
sys.path.append('..')
from lib.text import *
from rules.CBrule import CBrule
from rules.EBrule import EBrule
from rules.SBrule import SBrule
from rules.SingleRule import SingleRule
from rules.WeakPass import weak_pass_set


class SEDB(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        reload(sys)
        sys.setdefaultencoding('utf-8')
        os.system("cls")
        self.prompt = "pydictor SEDB>>"
        self.do_help(self)

    def do_EOF(self):
        return True

    def do_help(self, key):
        if key in help_dict.keys():
            print help_dict[key]
        elif key == 'all':
            for k in help_dict.keys():
                print help_dict[k]
        else:
            print helpmsg

    def do_exit(self):
        return True

    def do_quit(self):
        return True

    def do_cls(self, line):
        os.system("cls")

    def do_clear(self, line):
        os.system("cls")

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
                print 'Input format:[YYYYMMDD] exp:19890512'
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
                print 'Identity card number length too short (should >=15)'
            else:
                settings_dict['idcard'].append(item)

    def do_jobnum(self, args):
        for item in str(args).split(' '):
            settings_dict['jobnum'].append(item)

    def do_otherdate(self, args):
        for item in str(args).split(' '):
            if len(item) != 8 or str(item).isdigit() is False:
                print 'Input format:[YYYYMMDD] exp:19890512'
            else:
                settings_dict['otherdate'].append(item)

    def do_usedchar(self, args):
        for item in str(args).split(' '):
            settings_dict['usedchar'].append(item)

    def do_show(self, key):
        if key in settings_dict.keys():
            if type(settings_dict[key]) is str:
                print "%-10s :%s" % (key, settings_dict[key])
            else:
                print "%-10s :%s" % (key, ' '.join([x for x in settings_dict[key]]))
        else:
            for args in settings_dict.keys():
                print "%-10s :%s" % (args, ' '.join([x for x in settings_dict[args]]))

    def do_run(self, args):
        count = 0
        storepath = os.path.join(os.getcwd(), "results", 'SEDB_%s.txt' % str(time.strftime("%Y%m%d_%H.%M.%S", time.localtime(time.time()))))
        with open(storepath, 'w') as f:
            # SingleRule
            for single in SingleRule(settings_dict['cname'], settings_dict['ename'], settings_dict['sname'],
                                     settings_dict['birth'], settings_dict['usedpwd'], settings_dict['phone'],
                                     settings_dict['uphone'], settings_dict['hphone'], settings_dict['email'],
                                     settings_dict['postcode'], settings_dict['nickname'], settings_dict['idcard'],
                                     settings_dict['jobnum'], settings_dict['otherdate'], settings_dict['usedchar']):
                f.write(single + '\n')
                count += 1
            # CBrule
            for cb in CBrule(settings_dict['cname'], settings_dict['birth']):
                f.write(cb + '\n')
                count += 1
            # EBrule
            for eb in EBrule(settings_dict['ename'], settings_dict['birth']):
                f.write(eb + '\n')
                count += 1
            # SBrule
            for sb in SBrule(settings_dict['sname'], settings_dict['birth']):
                f.write(sb + '\n')
                count += 1
            # WeakPass
            for weakpwd in weak_pass_set:
                f.write(weakpwd + '\n')
                count += 1
        print "[+] A total of %s lines" % str(count)
        print "[+] Store in %s " % storepath




