#!/usr/bin/env python
# coding:utf-8
# A powerful and useful hacker dictionary builder for a brute-force attack
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
from lib.fun.fun import cool
from core.SEDB import SEDB
from core.BASE import get_base_dic
from core.CHAR import get_char_dic
from core.CHUNK import get_chunk_dic
from core.EXTEND import get_extend_dic
from lib.fun.handle import get_handle_dic
from lib.data.data import paths, pystrs, pyoptions
from lib.data.text import pydictor_art_text
from lib.parse.command import parse_args
from lib.parse.tricksparse import sedb_tricks
from lib.parse.argsparse import plug_parser, conf_parser, tool_parser


def init():
    args = parse_args()
    pyoptions.leetmode_code = args.leet

    if not (args.len[0] == pyoptions.minlen and args.len[1] == pyoptions.maxlen):
        pyoptions.args_pick = True
    if pyoptions.leetmode_code:
        pyoptions.extend_leet = True
        pyoptions.passcraper_leet = True
        pyoptions.sedb_leet = True

    paths.results_path = os.path.abspath(args.output)

    pyoptions.head = args.head
    pyoptions.tail = args.tail
    pyoptions.encode = args.encode
    pyoptions.minlen = args.len[0]
    pyoptions.maxlen = args.len[1]
    pyoptions.letter_occur = args.occur[0]
    pyoptions.digital_occur = args.occur[1]
    pyoptions.letter_types = args.types[0]
    pyoptions.digital_types = args.types[1]
    pyoptions.filter_regex = args.regex

    pyoptions.args_base = args.base
    pyoptions.args_char = args.char
    pyoptions.args_chunk = args.chunk
    pyoptions.args_extend = args.extend
    pyoptions.args_handle = args.handle
    pyoptions.args_plug = args.plug
    pyoptions.args_sedb = args.sedb
    pyoptions.args_conf = args.conf
    pyoptions.args_tool = args.tool
    pyoptions.level = args.level

    try:
        if not os.path.exists(paths.results_path):
            if os.path.exists(os.path.split(paths.results_path)[0]):
                paths.results_file_name = os.path.split(paths.results_path)[1]
                paths.results_path = os.path.split(paths.results_path)[0]
            else:
                os.mkdir(paths.results_path)
    except WindowsError:
        exit(pyoptions.CRLF + cool.red("[-] Cannot create result file: %s " % paths.results_path))


if __name__ == '__main__':
    print("{}".format(cool.green(pydictor_art_text)))
    init()
    if pyoptions.args_base:
        get_base_dic(pyoptions.args_base)
    elif pyoptions.args_char:
        get_char_dic(pyoptions.args_char)
    elif pyoptions.args_chunk:
        get_chunk_dic(pyoptions.args_chunk)
    elif pyoptions.args_extend:
        get_extend_dic(pyoptions.args_extend)
    elif pyoptions.args_plug:
        plug_parser()
    elif pyoptions.args_handle:
        get_handle_dic(pyoptions.args_handle)
    elif pyoptions.args_sedb:
        try:
            sedb_tricks()
            shell = SEDB()
            shell.cmdloop()
        except Exception as e:
            exit(e)
    elif pyoptions.args_conf != 'default':
        conf_parser()
    elif pyoptions.args_tool:
        tool_parser()
