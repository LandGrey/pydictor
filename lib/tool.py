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
from lib.data import CRLF, filextension, get_result_store_path, get_buildtime, tool_fun_str, prefix_range
from lib.fun import finishcounter, cool
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
    storepath = os.path.join(get_result_store_path(), "%s_%s%s" % (tool_fun_str[1].upper(), get_buildtime(), filextension))
    with open(original_file_path) as o_f:
        with open(storepath, 'a') as s_f:
            for _ in fast_uniqify(o_f.readlines()):
                s_f.write(_)
    print("[+] Start   : {0:10} lines".format(cool.orange(finishcounter(original_file_path))))
    print("[+] Current : {0:10} lines".format(cool.orange(finishcounter(storepath))))
    print("[+] Cost    : {0:} seconds".format(cool.orange(str(time.time() - start)[:6])))
    print("[+] Store in: {0}".format(cool.orange(storepath)))


def cleaner(*args):
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
