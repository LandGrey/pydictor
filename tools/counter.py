#!/usr/bin/env python
# coding:utf-8
# pydictor dictionary-handler tool: counter
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import time
import string
from collections import Counter
from lib.fun import finishcounter, finishprinter, cool
from lib.data import operator, CRLF, filextension, get_result_store_path, get_buildtime, COUNTER_prefix, \
    vs_counter_switcher, default_vs_items, counter_cmd_range, just_view_counter, just_save_counter, \
    save_and_view, tool_range, counter_split, startime


def counter_operator(original_file_path, justsave, justview, encodeflag, head, tail, vs_count=default_vs_items):
    items = Counter(open(original_file_path, 'r').read().replace(string.punctuation, "").split(counter_split)).most_common(vs_count)
    items_length = len(items)
    storepath = os.path.join(get_result_store_path(), "%s_%s%s" % (COUNTER_prefix, get_buildtime(), filextension))
    if vs_count > vs_counter_switcher:
        exit(CRLF + cool.fuchsia("[!] view items should Leq {0}".format(vs_counter_switcher)))
    elif items_length < vs_count:
        exit(CRLF + cool.fuchsia("[!] max items is {0}".format(items_length)))
    print("{0}Welcome to the COUNTER tool".format("   "*8))
    if justsave:
        with open(storepath, "a") as f:
            for _ in items:
                f.write(operator.get(encodeflag)(head + _[0] + tail) + CRLF)
        finishprinter(finishcounter(storepath), storepath)
    elif justview:
        print(CRLF * 2)
        for item in items:
            print("{0}Word:{2:20} -> {1:10} times".format("     "*5, cool.orange(item[1]), cool.orange(item[0])))
        print("[+] Cost:{} seconds".format(cool.orange(str(time.time() - startime)[:6])))
    else:
        print(CRLF * 2)
        for item in items:
            print("{0}Word:{2:20} -> {1:10} times".format("     "*5, cool.orange(item[1]), cool.orange(item[0])))
        print(CRLF)
        with open(storepath, 'a') as f:
            for _ in items:
                f.write(operator.get(encodeflag)(head + _[0] + tail) + CRLF)
        finishprinter(finishcounter(storepath), storepath)


def counter_enter(encodeflag, head, tail, *args):
    args = args[0]
    # counter lack file argument
    if len(args) == 2 and args[0] == tool_range[2] and args[1] in counter_cmd_range:
        exit(CRLF + cool.red("[-] {0} need specify the file path".format(tool_range[2])))
    # counter error "vf" argument
    elif len(args) >= 2 and args[0] == tool_range[2] and args[1] not in counter_cmd_range:
        exit(CRLF + cool.red("[-] Need {0}'s options, choose from '{1}' or '{2}' or '{3}'".
                             format(tool_range[2], counter_cmd_range[0], counter_cmd_range[1], counter_cmd_range[2])))
    # counter
    elif len(args) >= 3 and args[0] == tool_range[2] and args[1] in counter_cmd_range:
        if os.path.isfile(args[2]):
            # counter s file
            if len(args) == 3 and args[1] == just_save_counter:
                counter_operator(args[2], True, False, encodeflag, head, tail)
            # counter v file
            elif len(args) == 3 and args[1] == just_view_counter:
                counter_operator(args[2], False, True, encodeflag, head, tail)
            # counter vs file
            elif len(args) == 3 and args[1] == save_and_view:
                counter_operator(args[2], False, False, encodeflag, head, tail)
            # counter v file 100
            elif len(args) == 4 and args[1] == just_view_counter and str(args[3]).isdigit():
                counter_operator(args[2], False, True, encodeflag, head, tail, vs_count=int(args[3]))
            # counter s file 100
            elif len(args) == 4 and args[1] == just_save_counter and str(args[3]).isdigit():
                counter_operator(args[2], True, False, encodeflag, head, tail, vs_count=int(args[3]))
            # counter vs file 100
            elif len(args) == 4 and args[1] == save_and_view and str(args[3]).isdigit():
                counter_operator(args[2], False, False, encodeflag, head, tail, vs_count=int(args[3]))
            else:
                exit(CRLF + cool.red("[-] Some unexpected input"))
