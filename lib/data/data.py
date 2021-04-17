#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2020 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import sys
import time
from collections import OrderedDict
from lib.data.datatype import AttribDict
from lib.fun.osjudger import py_ver_egt_3


def init_paths():
    try:
        root_path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0]))).encode('utf-8').decode() \
            if py_ver_egt_3 else os.path.dirname(os.path.realpath(sys.argv[0])).decode('utf-8')
    except:
        root_path = 'fake path'
        exit("\n[-] Please ensure pydictor directory path name is english characters\n")

    paths.root_path = root_path
    paths.results_path = os.path.abspath(os.path.join(paths.root_path, "results"))
    paths.results_file_name = None
    paths.core_path = os.path.abspath(os.path.join(paths.root_path, "core"))
    paths.tools_path = os.path.abspath(os.path.join(paths.root_path, "tools"))
    paths.plugins_path = os.path.abspath(os.path.join(paths.root_path, "plugins"))
    paths.encode_function_path = os.path.abspath(os.path.join(paths.root_path, "lib", "encode"))

    # wordlist path
    paths.wordlist_path = os.path.join(paths.root_path, "wordlist")
    paths.applist_path = os.path.join(paths.wordlist_path, "App")
    paths.iotlist_path = os.path.join(paths.wordlist_path, "IoT")
    paths.niplist_path = os.path.join(paths.wordlist_path, "NiP")
    paths.sedblist_path = os.path.join(paths.wordlist_path, "SEDB")
    paths.syslist_path = os.path.join(paths.wordlist_path, "Sys")
    paths.weblist_path = os.path.join(paths.wordlist_path, "Web")
    paths.wifilist_path = os.path.join(paths.wordlist_path, "WiFi")

    # function cfg path
    paths.funcfg_path = os.path.join(paths.root_path, "funcfg")
    paths.buildconf_path = os.path.join(paths.funcfg_path, "build.conf")
    paths.extendconf_path = os.path.join(paths.funcfg_path, "extend.conf")
    paths.leetmode_path = os.path.join(paths.funcfg_path, "leet_mode.conf")
    paths.scrapersites_path = os.path.join(paths.funcfg_path, 'scratch.sites')
    paths.scratch_blacklist = os.path.join(paths.funcfg_path, "scratch_blacklist.conf")
    paths.sedbtrick_path = os.path.join(paths.funcfg_path, "sedb_tricks.conf")


def init_pystrs():
    # start time
    pystrs.startime = time.time()

    pystrs.version = '2.1.5.4#dev'

    # build configuration file element description
    pystrs.conf_head = "head"
    pystrs.conf_char = "char"
    pystrs.conf_minlen = "minlen"
    pystrs.conf_maxlen = "maxlen"
    pystrs.conf_encode = "encode"
    pystrs.conf_tail = "tail"

    pystrs.sex_range = ("m", "f", "all")
    pystrs.default_sex = "all"

    # base dict type flag
    pystrs.base_dic_type = ("d", "L", "c", "dL", "dc", "Lc", "dLc")

    # counter command string
    pystrs.just_view_counter = "v"
    pystrs.just_save_counter = "s"
    pystrs.save_and_view = "vs"
    pystrs.counter_cmd_range = (pystrs.just_save_counter, pystrs.just_view_counter, pystrs.save_and_view)

    pystrs.sedb_trick_prefix = "sedb_trick_prefix_strings"
    pystrs.sedb_trick_suffix = "sedb_trick_suffix_strings"
    pystrs.sedb_trick_middle = "sedb_trick_middle_strings"

    # social engineering dictionary elements
    pystrs.sedb_range = ("cname", "ename", "sname", "birth", "usedpwd", "phone", "uphone", "hphone", "email",
                         "postcode", "nickname", "idcard", "jobnum", "otherdate", "usedchar")

    pystrs.sedb_dict = OrderedDict([
        (pystrs.sedb_range[0], []), (pystrs.sedb_range[1], []), (pystrs.sedb_range[2], []), (pystrs.sedb_range[3], []),
        (pystrs.sedb_range[4], []), (pystrs.sedb_range[5], []), (pystrs.sedb_range[6], []), (pystrs.sedb_range[7], []),
        (pystrs.sedb_range[8], []), (pystrs.sedb_range[9], []), (pystrs.sedb_range[10], []), (pystrs.sedb_range[11], []),
        (pystrs.sedb_range[12], []), (pystrs.sedb_range[13], []), (pystrs.sedb_range[14], [])
    ]
    )


def init_pyoptions():
    # global CRLF
    pyoptions.CRLF = "\n"

    # filename extension
    pyoptions.filextension = ".txt"

    # allowed maximum length
    pyoptions.maxlen_switcher = 20

    # allowed maximum generated items
    pyoptions.count_switcher = 100000000000

    # shredded file rewrite counts
    pyoptions.file_rewrite_count = 1

    # shredded dir rewrite counts
    pyoptions.dir_rewrite_count = 1

    # counter tool max count
    pyoptions.vs_counter_switcher = 100000

    # counter tool split word
    pyoptions.counter_split = "\n"

    # default counter view items
    pyoptions.default_vs_items = 50

    # format date ymd_format: yyyMMdd   dmy_format: ddMMyyyy
    pyoptions.ymd_format = True

    # command options
    pyoptions.args_base = ""
    pyoptions.args_char = ""
    pyoptions.args_chunk = []
    pyoptions.args_extend = []
    pyoptions.args_plug = []
    pyoptions.args_sedb = ""
    pyoptions.args_conf = ""
    pyoptions.args_tool = []
    pyoptions.args_sedb = False
    pyoptions.args_pick = False

    # command arguments
    pyoptions.head = ""
    pyoptions.tail = ""
    pyoptions.encode = "none"
    pyoptions.minlen = 0
    pyoptions.maxlen = 4
    pyoptions.buffer_size = 256

    pyoptions.default_occur = "<=99"
    pyoptions.occur_is_filter = False
    pyoptions.letter_occur = pyoptions.default_occur
    pyoptions.digital_occur = pyoptions.default_occur
    pyoptions.special_occur = pyoptions.default_occur

    pyoptions.default_types = ">=0"
    pyoptions.types_is_filter = False
    pyoptions.letter_types = pyoptions.default_types
    pyoptions.digital_types = pyoptions.default_types
    pyoptions.special_types = pyoptions.default_types

    pyoptions.default_repeat = ">=0"
    pyoptions.repeat_is_filter = False
    pyoptions.letter_repeat = pyoptions.default_repeat
    pyoptions.digital_repeat = pyoptions.default_repeat
    pyoptions.special_repeat = pyoptions.default_repeat

    pyoptions.filter_regex = ".*?"
    pyoptions.regex_is_filter = False

    # the lower the more items
    pyoptions.level = 3

    # leet mode
    pyoptions.extend_leet = False
    pyoptions.scratch_leet = False
    pyoptions.sedb_leet = False
    pyoptions.leetmode_code = []

    # LEQ middle_switcher will works on 'extend' plug
    pyoptions.middle_switcher = 5

    # configuration file split char
    pyoptions.chars_split = ","
    pyoptions.char_range_split = "-"
    pyoptions.length_split = ","
    pyoptions.rangepattern = '^\[.*?\]$'
    pyoptions.level_str_pattern = "^(\d)\s+(.*?)$"
    pyoptions.level_str_str_pattern = "^(\d)\s+(.*?)\s+(.*?)$"
    pyoptions.confpattern = '(.*?)\[(.*?)\]\{(.*?)\}\<(.*?)\>([^[]*)'

    # annotator
    pyoptions.annotator = '#'

    # sedb trick
    pyoptions.trick_split = ","
    pyoptions.sedb_trick_mid = []
    pyoptions.sedb_trick_pre = []
    pyoptions.sedb_trick_suf = []

    # cfg
    pyoptions.key_value_split = "="

    # characters map operator
    pyoptions.charmap = {'%space%': ' ', '%-%': '-',
                         '%|%': ',', '%||%': ':',
                         '%{%': '{', '%}%': '}',
                         '%[%': '[', '%]%': ']',
                         '%(%': '(', '%)%': ')',
                         '%<%': '<', '%>%': '>'}

    # core function string range
    pyoptions.core_range = [core[:-3].lower() for core in os.listdir(paths.core_path)
                            if core.endswith('.py') and not core.startswith('__')]

    # encode ending string format
    pyoptions.encode_ending = "_encode"

    # encode operator
    pyoptions.operator = {}
    for encode_file_name in os.listdir(paths.encode_function_path):
        encode_name = encode_file_name.split(".")[0]
        if encode_name.endswith(pyoptions.encode_ending):
            pyoptions.operator[encode_name[:-len(pyoptions.encode_ending)].lower()] = getattr(__import__('lib.encode.' + encode_name, fromlist=True), encode_name)

    # encode function string range
    pyoptions.encode_range = [key for key in pyoptions.operator.keys()]

    # encode info description
    pyoptions.encode_info = {}
    for encode_name in pyoptions.operator.keys():
        pyoptions.encode_info[encode_name] = getattr(pyoptions.operator.get(encode_name), "__doc__")
    try:
        pyoptions.encode_desc = "".join([str(key).ljust(10) + pyoptions.encode_info[key] + pyoptions.CRLF
                                         for key in sorted(pyoptions.encode_info.keys())])
    except TypeError as e:
        exit("[-] please check your modified encode function, something error")

    # tools_operator ending string format
    pyoptions.tool_ending = "_magic"

    # tool function string range
    pyoptions.tool_range = [tool[:-3].lower() for tool in os.listdir(paths.tools_path)
                            if tool.endswith('.py') and not tool.startswith('__')]

    # tools operator
    pyoptions.tools_operator = {}
    sys.path.append(paths.tools_path)
    for tool_name in pyoptions.tool_range:
        for tool_enter in dir(__import__(str(tool_name), globals(), locals(), [str(tool_name) + pyoptions.tool_ending], )):
            if tool_enter.endswith(pyoptions.tool_ending):
                pyoptions.tools_operator[tool_enter[:-len(pyoptions.tool_ending)].lower()] = \
                    getattr(__import__(tool_name), tool_enter)

    # tools info description
    pyoptions.tools_info = {}
    for tool_name in pyoptions.tools_operator.keys():
        pyoptions.tools_info[tool_name] = getattr(pyoptions.tools_operator.get(tool_name), "__doc__")
    pyoptions.tools_desc = "".join([str(key).ljust(10) + pyoptions.tools_info[key] + pyoptions.CRLF
                                    for key in sorted(pyoptions.tools_info.keys())])

    # plug ending string format
    pyoptions.plug_ending = "_magic"

    # plug function string range
    pyoptions.plug_range = [plug[:-3].lower() for plug in os.listdir(paths.plugins_path)
                            if plug.endswith('.py') and not plug.startswith('__')]
    # plugins operator
    pyoptions.plugins_operator = {}
    sys.path.append(paths.plugins_path)
    for plug_name in pyoptions.plug_range:
        for plug_magic in dir(__import__(str(plug_name), globals(), locals(), [str(plug_name) + pyoptions.plug_ending], )):
            if plug_magic.endswith(pyoptions.plug_ending):
                pyoptions.plugins_operator[plug_magic[:-len(pyoptions.plug_ending)].lower()] = \
                    getattr(__import__(plug_name), plug_magic)

    # plugins info description
    pyoptions.plugins_info = {}
    for plug_name in pyoptions.plugins_operator.keys():
        pyoptions.plugins_info[plug_name] = getattr(pyoptions.plugins_operator.get(plug_name), "__doc__")
    pyoptions.plugins_desc = "".join([str(key).ljust(10) + str(pyoptions.plugins_info[key]) + pyoptions.CRLF
                                     for key in sorted(pyoptions.plugins_info.keys())])

    # prefix range
    pyoptions.prefix_range = pyoptions.core_range + pyoptions.plug_range + pyoptions.tool_range

    # pattern for scratch scratch website words
    pyoptions.scratch_filter = r'(^(\d){1,4}px$)|' \
                               r'(^[0-9,a-z,A-Z]{18,}$)|' \
                               r'(^(\d){2,4}x(\d){2,4}$)|' \
                               r'(^[0-9,a-f,A-F]{5,8}$)|' \
                               r'(^(u|U|\\u|\\U|U\+)[0-9,a-f,A-F]{4}$)|' \
                               r'(^(0x|u0026|u003e|252C94|u003c|auto|252C94)[a-z,A-Z]{1,16}$)|' \
                               r'(^on(fo|dra|mouse|load|play|seek)[a-z]{0,5}$)|' \
                               r'(^(img|div|svg|vfl|span|font|form|case|label|index|level|image)(\d){1,4}$)|' \
                               r'(^[a-z,A-Z]{2,6}(id|bar|ico|div|pic|img|box|url|uri|span|menu|image|title|color' \
                               r'|class|images|icon)$)'

# pydictor paths
paths = AttribDict()
# object to store description strings
pystrs = AttribDict()
# object to store options
pyoptions = AttribDict()

init_paths()
init_pystrs()
init_pyoptions()
