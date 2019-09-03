#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

import os
import sys
import traceback

js_cache = None


def execjs_encode(item):
    """execute js function and need modify code"""
    global js_cache

    # 1. please change js_call_function name. modify local js file path or modify js code string
    js_call_function = 'hex_md5'
    js_file_local_path = r"js_md5.js"
    js_code_for_string = """   """

    if js_cache:
        resource = js_cache
    elif os.path.isfile(js_file_local_path):
        with open(js_file_local_path, 'r') as f:
            resource = f.read()
    else:
        resource = js_code_for_string

    if "execjs" not in sys.modules:
        try:
            import execjs
        except ImportError:
            exit("[-] Please: pip install PyExecJS")
    exec_compile = __import__("execjs").compile(resource.encode('utf8').decode('utf8'))
    try:
        # 2. if need use can add extra parameters like:
        # return exec_compile.call(js_call_function, item, "param1", "param2")
        return exec_compile.call(js_call_function, item,)
    except:
        print("[-] execjs error:\n")
        exit(traceback.print_exc())
