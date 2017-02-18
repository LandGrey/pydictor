#!/usr/bin/env python
# coding:utf-8
# A extra tool for uniqify list, count words, combine
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import time
import string
from collections import Counter
from lib.data import operator, CRLF, filextension, get_result_store_path, get_buildtime, prefix_range, UNIQIFY_prefix, \
    COUNTER_prefix, view_counter_switcher, default_view_items, counter_cmd_str, just_view_counter, just_save_counter, \
    save_and_view, tool_fun_str, counter_split
from lib.fun import finishcounter, finishprinter, cool
from lib.shredder import shreder_file, shreder_dir

start = time.time()


# order preserving
def fast_uniqify(seq, idfun=None):
    if idfun is None:
        def idfun(x): return x
    seen = {}
    results = []
    for item in seq:
        marker = idfun(item)
        if marker in seen:
            continue
        seen[marker] = 1
        results.append(item)
    return results


def uniqify_enter(original_file_path):
    storepath = os.path.join(get_result_store_path(), "%s_%s%s" % (UNIQIFY_prefix, get_buildtime(), filextension))
    with open(original_file_path) as o_f:
        with open(storepath, 'a') as s_f:
            for _ in fast_uniqify(o_f.readlines()):
                s_f.write(_)
    print("[+] Start   : {0:10} lines".format(cool.orange(finishcounter(original_file_path))))
    print("[+] Current : {0:10} lines".format(cool.orange(finishcounter(storepath))))
    print("[+] Cost    : {0:} seconds".format(cool.orange(str(time.time() - start)[:6])))
    print("[+] Store in: {0}".format(cool.orange(storepath)))


def shredder_enter(*args):
    _ = "".join(args)
    if _ and os.path.isdir(_):
        shreder_dir(_)
    elif _ and os.path.isfile(_):
        shreder_file(_)
    elif _ and _.upper() in prefix_range:
        for filename in os.listdir(get_result_store_path()):
            if _.upper() in str(filename[0:8]).upper():
                shreder_file(os.path.join(get_result_store_path(), filename))
    else:
        exit(CRLF + cool.red("[-] invalid shredder path_or_dir arguments"))


def counter_enter(encodeflag, head, tail, *args):
    args = args[0]
    # counter lack file argument
    if len(args) == 2 and args[0] == tool_fun_str[2] and args[1] in counter_cmd_str:
        exit(CRLF + cool.red("[-] {0} need specify the file path".format(tool_fun_str[2])))
    # counter error "vf" argument
    elif len(args) >= 2 and args[0] == tool_fun_str[2] and args[1] not in counter_cmd_str:
        exit(CRLF + cool.red("[-] Need {0}'s options, choose from '{1}' or '{2}' or '{3}'".
                  format(tool_fun_str[2], counter_cmd_str[0], counter_cmd_str[1], counter_cmd_str[2])))
    # counter
    elif len(args) >= 3 and args[0] == tool_fun_str[2] and args[1] in counter_cmd_str:
        if os.path.isfile(args[2]):
            # counter f file
            if len(args) == 3 and args[1] == just_save_counter:
                counter_operator(args[2], True, False, encodeflag, head, tail)
            # counter v file
            elif len(args) == 3 and args[1] == just_view_counter:
                counter_operator(args[2], False, True, encodeflag, head, tail)
            # counter fv file
            elif len(args) == 3 and args[1] == save_and_view:
                counter_operator(args[2], False, False, encodeflag, head, tail)
            # counter v file 100
            elif len(args) == 4 and args[1] == just_view_counter and str(args[3]).isdigit():
                counter_operator(args[2], False, True, encodeflag, head, tail, view_count=int(args[3]))
            # counter fv file 100
            elif len(args) == 4 and args[1] == save_and_view and str(args[3]).isdigit():
                counter_operator(args[2], False, False, encodeflag, head, tail, view_count=int(args[3]))
            else:
                exit(CRLF + cool.red("[-] Some unexpected input"))


def counter_operator(original_file_path, justsave, justview, encodeflag, head, tail, view_count=default_view_items):
    items = Counter(open(original_file_path, 'r').read().replace(string.punctuation, "").split(counter_split)).most_common(view_count)
    items_length = len(items)
    storepath = os.path.join(get_result_store_path(), "%s_%s%s" % (COUNTER_prefix, get_buildtime(), filextension))
    if view_count > view_counter_switcher:
        exit(CRLF + cool.fuchsia("[!] view items should leq {0}".format(view_counter_switcher)))
    elif items_length < view_count:
        exit(CRLF + cool.fuchsia("[!] max items is {0}".format(items_length)))
    print("{0}WELCOME TO THE COUNTER TOOL".format("   "*8))
    if justsave:
        with open(storepath, 'a') as f:
            for _ in items:
                if encodeflag == "":
                    f.write(head + _[0] + tail + CRLF)
                else:
                    f.write(operator.get(encodeflag)(head + _[0] + tail) + CRLF)
        finishprinter(finishcounter(storepath), storepath)
    elif justview:
        print(CRLF * 2)
        for item in items:
            print("{0}Word:{2:20} -> {1:10} times".format("     "*5, cool.orange(item[1]), cool.orange(item[0])))
    else:
        print(CRLF * 2)
        for item in items:
            print("{0}Word:{2:20} -> {1:10} times".format("     "*5, cool.orange(item[1]), cool.orange(item[0])))
        print(CRLF)
        with open(storepath, 'a') as f:
            for _ in items:
                if encodeflag == "":
                    f.write(head + _[0] + tail + CRLF)
                else:
                    f.write(operator.get(encodeflag)(head + _[0] + tail) + CRLF)
        finishprinter(finishcounter(storepath), storepath)
