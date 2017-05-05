#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import cmd
from rules.EB import EB
from rules.SB import SB
from rules.NB import NB
from rules.SDrule import SDrule
from rules.NNrule import NNrule
from rules.SNrule import SNrule
from rules.SSrule import SSrule
from rules.Mailrule import Mailrule
from rules.SingleRule import SingleRule
from plugins.extend import extend_enter
from lib.fun.osjudger import is_Windows, is_Linux, is_Mac
from lib.data.text import help_dict, helpmsg, pydictor_art_text
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.fun import cool, unique, finishprinter, finishcounter, walks_all_files, lengthchecker, mybuildtime


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
            print(cool.yellow(help_dict[key]))
        elif key == 'desc':
            for k in help_dict.keys():
                print(cool.yellow(help_dict[k]))
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

    def do_set(self, args):
        arguments = []
        for item in str(args).split(' '):
            arguments.append(item)
        option = arguments[0]
        if option in pystrs.sedb_dict.keys():
            arguments.remove(option)
            sucessflag = True
            if option == pystrs.sedb_range[3] or option == pystrs.sedb_range[13]:
                for x in arguments:
                    if len(x) != 8 or not x.isdigit():
                        sucessflag = False
                        print(cool.fuchsia("[!] Input format:[YYYYMMDD] exp:19900512" + pyoptions.CRLF))
                    elif int(x[4:6]) > 12 or int(x[4:6]) < 1 or int(x[6:8]) > 31 or int(x[6:8]) < 1:
                        sucessflag = False
                        print(cool.fuchsia("[!] Date format {1 <= month <= 12} and {1 <= day <=31}" + pyoptions.CRLF))
                    else:
                        pystrs.sedb_dict[option].append(x)
            elif option == pystrs.sedb_range[11]:
                for x in arguments:
                    if len(x) < 15:
                        sucessflag = False
                        print(cool.fuchsia("[!] Identity card number length too short (should >=15)" + pyoptions.CRLF))
                    else:
                        pystrs.sedb_dict[pystrs.sedb_range[11]].append(x)
            else:
                for s in arguments:
                    pystrs.sedb_dict[option].append(s)
            if sucessflag:
                self.do_show(option)
        elif option != '':
            print(cool.fuchsia("[!] no option named %s %s" % (option, pyoptions.CRLF)))
        else:
            print(cool.fuchsia("[!] please set option and arguments" + pyoptions.CRLF))

    def do_show(self, key):
        if key in pystrs.sedb_dict.keys():
            print(cool.blue("%-10s :%s" % (key, ' '.join([x for x in pystrs.sedb_dict[key]]))))
        else:
            for key in pystrs.sedb_dict.keys():
                print(cool.blue("%-10s :%s" % (key, ' '.join([x for x in pystrs.sedb_dict[key]]))))

    def do_ls(self, key):
        SEDB.do_show(self, key)

    def do_rm(self, key):
        if key in pystrs.sedb_dict.keys():
            pystrs.sedb_dict[key] = []
            print(cool.white("[+] %s option was removed %s" % (key, pyoptions.CRLF)))
        elif key == '':
            for key in pystrs.sedb_dict.keys():
                pystrs.sedb_dict[key] = []
            print(cool.white("[+] all option was removed" + pyoptions.CRLF))
        else:
            print(cool.fuchsia("[!] no option named %s %s" % (key, pyoptions.CRLF)))

    def do_pick(self, key):
        chunk = key.split(' ')
        if len(chunk) != 2:
            print(cool.fuchsia("[!] usage: pick minlen maxlen" + pyoptions.CRLF))
        else:
            minlen = key.split(' ')[0]
            maxlen = key.split(' ')[1]
            if lengthchecker(minlen, maxlen, sedb=True):
                pyoptions.args_pick = True
                pyoptions.minlen = int(minlen)
                pyoptions.maxlen = int(maxlen)
                print(cool.white("[+] minlen = {0} maxlen = {1}".format(pyoptions.minlen, pyoptions.maxlen)) + pyoptions.CRLF)

    def do_mode(self, key):
        chunk = key.split(' ')
        if len(chunk) != 1:
            print(cool.fuchsia("[!] usage: mode code") + pyoptions.CRLF)
        else:
            if chunk[0].isdigit() and (0 <= int(chunk[0]) <= 2 or 11 <= int(chunk[0]) <= 19 or 21 <= int(chunk[0]) <= 29):
                pyoptions.sedb_leet = True
                pyoptions.leetmode_code = int(chunk[0])
                print(cool.white("[+] code: {0}".format(chunk[0])) + pyoptions.CRLF)
            else:
                print(cool.fuchsia("[!] code vaule:[0, 1, 2, 11-19, 21-29]") + pyoptions.CRLF)

    def do_run(self, args):
        results = []
        storepath = os.path.join(paths.results_path, '%s_%s%s' % (pystrs.SEDB_prefix, mybuildtime(),
                                                                  pyoptions.filextension))
        with open(storepath, "a") as f:
            # SingleRule
            for single in SingleRule(pystrs.sedb_dict[pystrs.sedb_range[0]], pystrs.sedb_dict[pystrs.sedb_range[1]],
                                     pystrs.sedb_dict[pystrs.sedb_range[2]], pystrs.sedb_dict[pystrs.sedb_range[3]],
                                     pystrs.sedb_dict[pystrs.sedb_range[4]], pystrs.sedb_dict[pystrs.sedb_range[5]],
                                     pystrs.sedb_dict[pystrs.sedb_range[6]], pystrs.sedb_dict[pystrs.sedb_range[7]],
                                     pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[9]],
                                     pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[11]],
                                     pystrs.sedb_dict[pystrs.sedb_range[12]], pystrs.sedb_dict[pystrs.sedb_range[13]],
                                     pystrs.sedb_dict[pystrs.sedb_range[14]]):
                results.append(single)
            # SDrule
            for cb in SDrule(pystrs.sedb_dict[pystrs.sedb_range[0]], pystrs.sedb_dict[pystrs.sedb_range[3]]):
                results.append(cb)
            for cb in SDrule(pystrs.sedb_dict[pystrs.sedb_range[0]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(cb)
            # EB
            for eb in EB(pystrs.sedb_dict[pystrs.sedb_range[1]], pystrs.sedb_dict[pystrs.sedb_range[3]]):
                results.append(eb)
            for eb in EB(pystrs.sedb_dict[pystrs.sedb_range[1]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(eb)
            # Mailrule
            for mr in Mailrule(pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[0]]):
                results.append(mr)
            for mr in Mailrule(pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[1]]):
                results.append(mr)
            for mr in Mailrule(pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[2]]):
                results.append(mr)
            for mr in Mailrule(pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[4]]):
                results.append(mr)
            for mr in Mailrule(pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[10]]):
                results.append(mr)
            for mr in Mailrule(pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[14]]):
                results.append(mr)
            for mr in Mailrule(pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[3]], isstrs=False):
                results.append(mr)
            for mr in Mailrule(pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[13]], isstrs=False):
                results.append(mr)
            # NB
            for nn in NB(pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[3]]):
                results.append(nn)
            for nn in NB(pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(nn)

            # SB
            for sb in SB(pystrs.sedb_dict[pystrs.sedb_range[2]], pystrs.sedb_dict[pystrs.sedb_range[3]]):
                results.append(sb)
            for sb in SB(pystrs.sedb_dict[pystrs.sedb_range[2]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(sb)

            # NNrule
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[3]], pystrs.sedb_dict[pystrs.sedb_range[5]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[3]], pystrs.sedb_dict[pystrs.sedb_range[6]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[5]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[6]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[7]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[9]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[12]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[3]], pystrs.sedb_dict[pystrs.sedb_range[7]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[3]], pystrs.sedb_dict[pystrs.sedb_range[9]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[3]], pystrs.sedb_dict[pystrs.sedb_range[11]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[3]], pystrs.sedb_dict[pystrs.sedb_range[12]]):
                results.append(nn)
            for nn in NNrule(pystrs.sedb_dict[pystrs.sedb_range[3]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(nn)

            # SNrule
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[4]], pystrs.sedb_dict[pystrs.sedb_range[3]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[4]], pystrs.sedb_dict[pystrs.sedb_range[5]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[4]], pystrs.sedb_dict[pystrs.sedb_range[6]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[4]], pystrs.sedb_dict[pystrs.sedb_range[7]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[4]], pystrs.sedb_dict[pystrs.sedb_range[9]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[4]], pystrs.sedb_dict[pystrs.sedb_range[11]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[4]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(sn)

            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[3]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[5]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[6]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[7]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[9]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[11]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(sn)

            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[14]], pystrs.sedb_dict[pystrs.sedb_range[3]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[14]], pystrs.sedb_dict[pystrs.sedb_range[5]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[14]], pystrs.sedb_dict[pystrs.sedb_range[6]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[14]], pystrs.sedb_dict[pystrs.sedb_range[7]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[14]], pystrs.sedb_dict[pystrs.sedb_range[9]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[14]], pystrs.sedb_dict[pystrs.sedb_range[11]]):
                results.append(sn)
            for sn in SNrule(pystrs.sedb_dict[pystrs.sedb_range[14]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
                results.append(sn)

            # SSrule
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[0]], pystrs.sedb_dict[pystrs.sedb_range[1]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[0]], pystrs.sedb_dict[pystrs.sedb_range[4]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[0]], pystrs.sedb_dict[pystrs.sedb_range[8]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[0]], pystrs.sedb_dict[pystrs.sedb_range[10]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[0]], pystrs.sedb_dict[pystrs.sedb_range[14]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[1]], pystrs.sedb_dict[pystrs.sedb_range[4]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[1]], pystrs.sedb_dict[pystrs.sedb_range[8]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[1]], pystrs.sedb_dict[pystrs.sedb_range[10]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[1]], pystrs.sedb_dict[pystrs.sedb_range[14]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[10]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[8]], pystrs.sedb_dict[pystrs.sedb_range[14]]):
                results.append(ss)
            for ss in SSrule(pystrs.sedb_dict[pystrs.sedb_range[10]], pystrs.sedb_dict[pystrs.sedb_range[14]]):
                results.append(ss)

            # WeakPass
            for weakpwd in walks_all_files(paths.sedblist_path):
                results.append(weakpwd)
            readylist = []
            readylist.extend(pystrs.sedb_dict[pystrs.sedb_range[0]])
            readylist.extend(pystrs.sedb_dict[pystrs.sedb_range[1]])
            readylist.extend(pystrs.sedb_dict[pystrs.sedb_range[2]])
            readylist.extend(pystrs.sedb_dict[pystrs.sedb_range[4]])
            readylist.extend(pystrs.sedb_dict[pystrs.sedb_range[10]])
            readylist.extend(pystrs.sedb_dict[pystrs.sedb_range[14]])
            # Using extend_enter plug
            for extendstr in extend_enter(readylist, leet=pyoptions.sedb_leet):
                results.append(extendstr)

            if not pyoptions.args_pick:
                for ur in unique(results):
                    f.write(ur + pyoptions.CRLF)
            else:
                for ur in unique(results):
                    if pyoptions.minlen <= len(ur) <= pyoptions.maxlen:
                        f.write(ur + pyoptions.CRLF)
        finishprinter(finishcounter(storepath), storepath)
