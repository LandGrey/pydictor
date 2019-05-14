#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals

import traceback

js_cache = None


def execjs_encode(item):
    """execute js function and need modify code"""
    # please add local js file path or remote internet js address
    string_js = ''''''
    local_js_path = ""
    remote_js_url = "http://www.example.com/js/somefunction.js"

    resource = ""
    global js_cache
    if js_cache:
        resource = js_cache
    elif string_js:
        resource = string_js
    elif local_js_path:
        from os.path import isfile as exists_file
        if exists_file(local_js_path):
            with open(local_js_path, 'r') as f:
                resource = f.read()
    else:
        try:
            from urllib.request import urlopen
        except:
            from urllib2 import urlopen
        finally:
            try:
                resource = urlopen(remote_js_url).read()
            except:
                print("[-] occurred error:")
                exit(traceback.print_exc())
    if not js_cache:
        try:
            import execjs
        except ImportError:
            exit("[-] please: pip install pyexecjs")
        finally:
            js_cache = resource
    exec_compile = execjs.compile(resource.decode('utf8'))
    try:
        return exec_compile.call('fun_name', item, "parm1", "parm2_if_need")
    except:
        print("[-] occurred error:")
        exit(traceback.print_exc())
