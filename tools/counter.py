#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

import os
import time
import string
from collections import Counter
from lib.fun.filter import filterforfun
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.fun import finishcounter, finishprinter, cool, mybuildtime


def counter_operator(original_file_path, justsave, justview, encodeflag, head, tail, vs_count=pyoptions.default_vs_items):
    items = Counter(open(original_file_path, 'r').read().replace(string.punctuation, "").
                    split(pyoptions.counter_split)).most_common(vs_count)
    items_length = len(items)
    storepath = os.path.join(paths.results_path, "%s_%s%s" % (pystrs.COUNTER_prefix, mybuildtime(), pyoptions.filextension))
    if vs_count > pyoptions.vs_counter_switcher:
        exit(pyoptions.CRLF + cool.fuchsia("[!] view items should Leq {0}".format(pyoptions.vs_counter_switcher)))
    elif items_length < vs_count:
        exit(pyoptions.CRLF + cool.fuchsia("[!] max items is {0}".format(items_length)))
    print("{0}Welcome to the COUNTER tool".format("   "*8))
    if justsave:
        with open(storepath, "a") as f:
            for _ in items:
                item = filterforfun(_[0], head=pyoptions.head, tail=pyoptions.tail,
                                    lenght_is_filter=pyoptions.args_pick,
                                    minlen=pyoptions.minlen, maxlen=pyoptions.maxlen,
                                    regex_is_filter=True, regex=pyoptions.filter_regex,
                                    encode_is_filter=True, encode=pyoptions.encode,
                                    occur_is_filter=True,
                                    letter_occur=pyoptions.letter_occur,
                                    digital_occur=pyoptions.digital_occur,
                                    special_occur=pyoptions.special_occur,
                                    types_is_filter=True,
                                    letter_types=pyoptions.letter_types,
                                    digital_types=pyoptions.digital_types,
                                    special_types=pyoptions.special_types,
                                    )
                if item:
                    f.write(item + pyoptions.CRLF)
        finishprinter(finishcounter(storepath), storepath)
    elif justview:
        print(pyoptions.CRLF * 2)
        for item in items:
            print("{0}Word:{2:20} -> {1:10} times".format("     "*5, cool.orange(item[1]), cool.orange(item[0])))
        print("[+] Cost:{} seconds".format(cool.orange(str(time.time() - pystrs.startime)[:6])))
    else:
        print(pyoptions.CRLF * 2)
        for item in items:
            print("{0}Word:{2:20} -> {1:10} times".format("     "*5, cool.orange(item[1]), cool.orange(item[0])))
        print(pyoptions.CRLF)
        with open(storepath, 'a') as f:
            for _ in items:
                f.write(pyoptions.operator.get(encodeflag)(head + _[0] + tail) + pyoptions.CRLF)
        finishprinter(finishcounter(storepath), storepath)


def counter_enter(encodeflag, head, tail, *args):
    args = args[0]
    # counter lack file argument
    if len(args) == 2 and args[0] == pystrs.tool_range[2] and args[1] in pystrs.counter_cmd_range:
        exit(pyoptions.CRLF + cool.red("[-] {0} need specify the file path".format(pystrs.tool_range[2])))
    # counter error "vf" argument
    elif len(args) >= 2 and args[0] == pystrs.tool_range[2] and args[1] not in pystrs.counter_cmd_range:
        exit(pyoptions.CRLF + cool.red("[-] Need {0}'s options, choose from '{1}' or '{2}' or '{3}'".format(
            pystrs.tool_range[2], pystrs.counter_cmd_range[0], pystrs.counter_cmd_range[1], pystrs.counter_cmd_range[2])))
    # counter
    elif len(args) >= 3 and args[0] == pystrs.tool_range[2] and args[1] in pystrs.counter_cmd_range:
        if os.path.isfile(args[2]):
            # counter s file
            if len(args) == 3 and args[1] == pystrs.just_save_counter:
                counter_operator(args[2], True, False, encodeflag, head, tail)
            # counter v file
            elif len(args) == 3 and args[1] == pystrs.just_view_counter:
                counter_operator(args[2], False, True, encodeflag, head, tail)
            # counter vs file
            elif len(args) == 3 and args[1] == pystrs.save_and_view:
                counter_operator(args[2], False, False, encodeflag, head, tail)
            # counter v file 100
            elif len(args) == 4 and args[1] == pystrs.just_view_counter and str(args[3]).isdigit():
                counter_operator(args[2], False, True, encodeflag, head, tail, vs_count=int(args[3]))
            # counter s file 100
            elif len(args) == 4 and args[1] == pystrs.just_save_counter and str(args[3]).isdigit():
                counter_operator(args[2], True, False, encodeflag, head, tail, vs_count=int(args[3]))
            # counter vs file 100
            elif len(args) == 4 and args[1] == pystrs.save_and_view and str(args[3]).isdigit():
                counter_operator(args[2], False, False, encodeflag, head, tail, vs_count=int(args[3]))
            else:
                exit(pyoptions.CRLF + cool.red("[-] Some unexpected input"))
