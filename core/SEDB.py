#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import cmd
import time

from core.EXTEND import extend_enter
from lib.fun.decorator import magic
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.osjudger import is_Windows, is_Linux, is_Mac
from lib.data.text import help_dict, helpmsg, pydictor_art_text
from lib.fun.fun import cool, walks_all_files, mybuildtime, finalsavepath, fun_name
from rules.EB import EB
from rules.NB import NB
from rules.SB import SB
from rules.SDrule import SDrule
from rules.SNrule import SNrule
from rules.SSrule import SSrule
from rules.NNrule import NNrule
from rules.Mailrule import Mailrule
from rules.SingleRule import SingleRule


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
                self.do_show(option, setflag=True)
        elif option != '':
            print(cool.fuchsia("[!] no option named %s %s" % (option, pyoptions.CRLF)))
        else:
            print(cool.fuchsia("[!] please set option and arguments" + pyoptions.CRLF))

    def do_show(self, key, setflag=False):
        if not setflag:
            if pyoptions.args_pick:
                print(cool.orange("{description:11}: minlen: [{0}] maxlen: [{1}]".
                                  format(pyoptions.minlen, pyoptions.maxlen, description="lenght")))
            else:
                print(cool.orange("{description:11}: minlen: [{0}] maxlen: [{0}]".format("no-limited",
                                                                                         description="len")))
            if pyoptions.head:
                print(cool.orange("{description:11}: [{0}]".format(pyoptions.head, description="head")))
            else:
                print(cool.orange("{description:11}: [{0}]".format("none", description="head")))

            if pyoptions.tail:
                print(cool.orange("{description:11}: [{0}]".format(pyoptions.tail, description="tail")))
            else:
                print(cool.orange("{description:11}: [{0}]".format("none", description="tail")))

            print(cool.orange("{description:11}: [{0}]".format(pyoptions.encode, description="encode")))

            print(cool.orange("{description:11}: letter: [ {0:5}] digital: [ {1:5}] special: [ {2:5} ]".format
                              (pyoptions.letter_occur, pyoptions.digital_occur, pyoptions.special_occur,
                               description="occur")))

            print(cool.orange("{description:11}: letter: [ {0:5}] digital: [ {1:5}] special: [ {2:5} ]".format
                              (pyoptions.letter_types, pyoptions.digital_types, pyoptions.special_types,
                               description="types")))

            print(cool.orange("{description:11}: letter: [ {0:5}] digital: [ {1:5}] special: [ {2:5} ]".format
                              (pyoptions.letter_repeat, pyoptions.digital_repeat, pyoptions.special_repeat,
                               description="repeat")))

            print(cool.orange("{description:11}: [{0}]".format(pyoptions.level, description="level")))

            if pyoptions.sedb_leet:
                print(cool.orange("{description:11}: [{0}]".format(" ".join(map(str, pyoptions.leetmode_code)),
                                                                   description="leet")))
            else:
                print(cool.orange("{description:11}: [{0}]".format("none", description="leet")))

            print(cool.orange("{description:11}: [{0}]".format(pyoptions.filter_regex, description="regex")))

        if key in pystrs.sedb_dict.keys():
            print(cool.blue("%-10s :%s" % (key, ' '.join([x for x in pystrs.sedb_dict[key]]))))
        else:
            for key in pystrs.sedb_dict.keys():
                print(cool.blue("%-10s :%s" % (key, ' '.join([x for x in pystrs.sedb_dict[key]]))))

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

    def do_head(self, key):
        chunk = key.split(' ')
        if len(chunk) != 1:
            print(cool.fuchsia("[!] usage: head prefix" + pyoptions.CRLF))
        else:
            pyoptions.head = chunk[0]
            print("[+] head: {0}".format(cool.green(pyoptions.head)) + pyoptions.CRLF)

    def do_tail(self, key):
        chunk = key.split(' ')
        if len(chunk) != 1:
            print(cool.fuchsia("[!] usage: tail suffix" + pyoptions.CRLF))
        else:
            pyoptions.tail = chunk[0]
            print("[+] tail: {0}".format(cool.green(pyoptions.tail)) + pyoptions.CRLF)

    def do_len(self, key):
        chunk = key.split(' ')
        if len(chunk) != 2:
            print(cool.fuchsia("[!] usage: len minlen maxlen" + pyoptions.CRLF))
        else:
            minlen = chunk[0]
            maxlen = chunk[1]
            try:
                pyoptions.args_pick = True
                pyoptions.minlen = int(minlen)
                pyoptions.maxlen = int(maxlen)
                print("[+] minlen: {0} maxlen: {1}".format(cool.green(pyoptions.minlen), cool.green(pyoptions.maxlen)) +
                      pyoptions.CRLF)
            except:
                print(cool.fuchsia("[!] ensure length is digital" + pyoptions.CRLF))

    def do_encode(self, key):
        chunk = key.split(' ')
        if len(chunk) != 1:
            print(cool.fuchsia("[!] usage: encode type" + pyoptions.CRLF))
        else:
            if chunk[0] in pystrs.encode_range:
                pyoptions.encode = chunk[0]
                print("[+] encode: {0}".format(cool.green(pyoptions.encode)) + pyoptions.CRLF)
            else:
                print(cool.fuchsia("[!] no encode type: %s" % chunk[0] + pyoptions.CRLF))

    def do_occur(self, key):
        chunk = key.split(' ')
        if len(chunk) != 3:
            print(cool.fuchsia("[!] usage: occur letter digital special" + pyoptions.CRLF) +
                  cool.blue("[?] exp: occur <=6 >4 >=0") + pyoptions.CRLF)
        else:
            pyoptions.occur_is_filter = True
            letter = chunk[0].strip('"').strip("'")
            digital = chunk[1].strip('"').strip("'")
            special = chunk[2].strip('"').strip("'")
            pyoptions.letter_occur = letter if letter != "" else pyoptions.letter_occur
            pyoptions.digital_occur = digital if digital != "" else pyoptions.digital_occur
            pyoptions.special_occur = special if special != "" else pyoptions.special_occur
            print("[+] letter occur: {0} digital occur: {1} special occur: {2}".
                  format(cool.green(pyoptions.letter_occur), cool.green(pyoptions.digital_occur),
                         cool.green(pyoptions.special_occur)) + pyoptions.CRLF)

    def do_types(self, key):
        chunk = key.split(' ')
        if len(chunk) != 3:
            print(cool.fuchsia("[!] usage: types letter digital special" + pyoptions.CRLF) +
                  cool.blue("[?] exp: types <=6 >4 >=0") + pyoptions.CRLF)
        else:
            pyoptions.types_is_filter = True
            letter = chunk[0].strip('"').strip("'")
            digital = chunk[1].strip('"').strip("'")
            special = chunk[2].strip('"').strip("'")
            pyoptions.letter_types = letter if letter != "" else pyoptions.letter_types
            pyoptions.digital_types = digital if digital != "" else pyoptions.digital_types
            pyoptions.special_types = special if special != "" else pyoptions.special_types
            print("[+] letter types: {0} digital types: {1} special types: {2}".format
                  (cool.green(pyoptions.letter_types), cool.green(pyoptions.digital_types),
                   cool.green(pyoptions.special_types)) + pyoptions.CRLF)

    def do_repeat(self, key):
        chunk = key.split(' ')
        if len(chunk) != 3:
            print(cool.fuchsia("[!] usage: repeat letter digital special" + pyoptions.CRLF) +
                  cool.blue("[?] exp: repeat <=6 >4 >=0") + pyoptions.CRLF)
        else:
            pyoptions.repeat_is_filter = True
            letter = chunk[0].strip('"').strip("'")
            digital = chunk[1].strip('"').strip("'")
            special = chunk[2].strip('"').strip("'")
            pyoptions.letter_repeat = letter if letter != "" else pyoptions.letter_repeat
            pyoptions.digital_repeat = digital if digital != "" else pyoptions.digital_repeat
            pyoptions.special_repeat = special if special != "" else pyoptions.special_repeat
            print("[+] letter repeat: {0} digital types: {1} special types: {2}".format
                  (cool.green(pyoptions.letter_repeat), cool.green(pyoptions.digital_repeat),
                   cool.green(pyoptions.special_repeat)) + pyoptions.CRLF)

    def do_regex(self, key):
        chunk = key.split(' ')
        if len(chunk) != 1:
            print(cool.fuchsia("[!] usage: regex filter-string" + pyoptions.CRLF))
        else:
            pyoptions.regex_is_filter = True
            pyoptions.filter_regex = chunk[0]
            print("[+] regex: {0}".format(cool.green(pyoptions.filter_regex)) + pyoptions.CRLF)

    def do_level(self, key):
        chunk = key.split(' ')
        if len(chunk) != 1:
            print(cool.fuchsia("[!] usage: level code" + pyoptions.CRLF))
        else:
            try:
                if not 1 <= int(chunk[0]) <= 5:
                    print(cool.fuchsia("[!] code range: 1-5" + pyoptions.CRLF))
                else:
                    pyoptions.level = int(chunk[0])
                    print("[+] level code: {}".format(cool.green(pyoptions.level)) + pyoptions.CRLF)
            except:
                print(cool.fuchsia("[!] code must be a digital" + pyoptions.CRLF))

    def do_leet(self, key):
        chunk = key.split(' ')
        if not chunk:
            print(cool.fuchsia("[!] usage: leet code code2 code3 ...") + pyoptions.CRLF)
        else:
            pyoptions.leetmode_code = []
            for c in chunk:
                if str(c).isdigit() and (0 <= int(c) <= 2 or 11 <= int(c) <= 19 or 21 <= int(c) <= 29):
                    pyoptions.sedb_leet = True
                    pyoptions.leetmode_code.append(int(c))
                else:
                    print(cool.fuchsia("[!] code vaule:[0, 1, 2, 11-19, 21-29]") + pyoptions.CRLF)
            print("[+] leet code: {0}".format(cool.green(" ".join(map(str, pyoptions.leetmode_code)))) + pyoptions.CRLF)

    def do_output(self, key):
        chunk = key.split(' ')
        if len(chunk) != 1:
            print(cool.fuchsia("[!] usage: output store_path" + pyoptions.CRLF))
        elif not chunk[0]:
            print(cool.fuchsia("[!] usage: output store_path" + pyoptions.CRLF))
        else:
            try:
                if not os.path.isdir(chunk[0]):
                    tmp_dirpath, tmp_filename = os.path.split(chunk[0])
                    if '.' in tmp_filename:
                        if not os.path.isdir(tmp_dirpath):
                            os.makedirs(tmp_dirpath)
                        paths.results_path = tmp_dirpath
                        paths.results_file_name = tmp_filename
                    else:
                        if not os.path.isdir(chunk[0]):
                            os.makedirs(chunk[0])
                        paths.results_path = chunk[0]
                else:
                    paths.results_path = chunk[0]
            except WindowsError:
                print(pyoptions.CRLF + cool.red("[-] Cannot create result file: %s " % paths.results_path))
            finally:
                this_name = 'SEDB_%s%s' % (mybuildtime(), pyoptions.filextension) \
                    if paths.results_file_name == None else paths.results_file_name
                print("[+] store path: {0}".format(cool.green(os.path.join(paths.results_path, this_name
                if paths.results_file_name != None else ''))) + pyoptions.CRLF)

    def do_run(self, args):
        pystrs.startime = time.time()
        results = []
        paths.results_file_name = None
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
        for sd in SDrule(pystrs.sedb_dict[pystrs.sedb_range[0]], pystrs.sedb_dict[pystrs.sedb_range[3]]):
            results.append(sd)
        for sd in SDrule(pystrs.sedb_dict[pystrs.sedb_range[0]], pystrs.sedb_dict[pystrs.sedb_range[13]]):
            results.append(sd)
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

        @magic
        def sedb():
            for ur in results:
                yield "".join(ur)
