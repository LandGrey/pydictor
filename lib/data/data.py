#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import sys
import time
from lib.fun.encode import *
from lib.fun.osjudger import py_ver_egt_3
from collections import OrderedDict
from lib.data.datatype import AttribDict


def init_paths():
    try:
        root_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0]))).encode('utf-8').decode() \
            if py_ver_egt_3 else os.path.dirname(os.path.abspath(sys.argv[0])).decode('utf-8')
    except:
        root_path = 'fake path'
        exit("\n[-] Please ensure pydictor directory path name is english characters\n")

    paths.root_path = root_path
    paths.results_path = os.path.abspath(os.path.join(paths.root_path, "results"))
    paths.results_file_name = None

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
    paths.scrapersites_path = os.path.join(paths.funcfg_path, 'passcraper.sites')
    paths.scraperwhitelist_path = os.path.join(paths.funcfg_path, "passcraper_blacklist.conf")
    paths.sedbtrick_path = os.path.join(paths.funcfg_path, "sedb_tricks.conf")


def init_pystrs():
    # start time
    pystrs.startime = time.time()

    pystrs.version = '2.0.1#dev'

    # file prefix strings
    pystrs.BASE_prefix = "BASE"
    pystrs.CHAR_prefix = "CHAR"
    pystrs.CHUNK_prefix = "CHUNK"
    pystrs.CONF_prefix = "CONF"
    pystrs.SEDB_prefix = "SEDB"
    pystrs.IDCARD_prefix = "IDCARD"
    pystrs.EXTEND_prefix = "EXTEND"
    pystrs.SCFATCH_prefix = "SCRATCH"
    pystrs.PASSCRAPER_prefix = "PASSCRAPER"
    pystrs.HANDLER_prefix = "HANDLER"
    pystrs.UNIQIFER_prefix = "UNIQIFER"
    pystrs.COUNTER_prefix = "COUNTER"
    pystrs.COMBINER_prefix = "COMBINER"
    pystrs.UNIQBINER_prefix = "UNIQBINER"
    pystrs.prefix_range = (pystrs.BASE_prefix, pystrs.CHAR_prefix, pystrs.CHUNK_prefix, pystrs.CONF_prefix,
                           pystrs.SEDB_prefix, pystrs.IDCARD_prefix, pystrs.EXTEND_prefix, pystrs.SCFATCH_prefix,
                           pystrs.PASSCRAPER_prefix, pystrs.HANDLER_prefix, pystrs.UNIQIFER_prefix, pystrs.COUNTER_prefix,
                           pystrs.COMBINER_prefix,  pystrs.UNIQBINER_prefix)

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

    # tool function string
    pystrs.tool_range = ("shredder", "uniqifer", "counter", 'combiner', 'uniqbiner', "handler", )

    # plug function string
    pystrs.plug_range = ("pid6", "pid8", "passcraper")

    # encode function string
    pystrs.encode_range = ("none", "b64", "md5", "md516", "sha1", "url", "sha256", "sha512")

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
    pyoptions.count_switcher = 1000000000000

    # shredded file rewrite counts
    pyoptions.file_rewrite_count = 1

    # shredded dir rewrite counts
    pyoptions.dir_rewrite_count = 1

    # counter tool max count
    pyoptions.vs_counter_switcher = 10000

    # counter tool split word
    pyoptions.counter_split = "\n"

    # default counter view items
    pyoptions.default_vs_items = 50

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
    pyoptions.default_occurs = "<=99"
    pyoptions.letter_occur = pyoptions.default_occurs
    pyoptions.digital_occur = pyoptions.default_occurs
    pyoptions.special_occur = pyoptions.default_occurs
    pyoptions.default_types = ">=0"
    pyoptions.letter_types = pyoptions.default_types
    pyoptions.digital_types = pyoptions.default_types
    pyoptions.special_types = pyoptions.default_types
    pyoptions.filter_regex = ".*?"

    # the lower the more items
    pyoptions.level = 3

    # leet mode
    pyoptions.extend_leet = False
    pyoptions.passcraper_leet = False
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

    # encode operator
    pyoptions.operator = {'none': none_encode, 'b64': base64_encode, 'md5': md5_encode, 'md516': md5_16_encode,
                          'sha1': sha1_encode, 'url': url_encode, 'sha256': sha256_encode, 'sha512': sha512_encode}

    # pattern for passcraper scratch website words
    pyoptions.passcraper_filter = r'(^(\d){1,4}px$)|' \
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
