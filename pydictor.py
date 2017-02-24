#!/usr/bin/env python
# coding:utf-8
# A useful hacker dictionary builder for a brute-force attack
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import time
from lib.fun import cool
from lib.command import parse_args
from core.BASE import get_base_dic
from core.CHAR import get_char_dic
from core.CHUNK import get_chunk_dic
from core.CONF import build_conf_dic
from core.SEDB import SEDB
from tools.shredder import shredder_enter
from tools.uniqifer import uniqifer_enter
from tools.counter import counter_enter
from tools.combiner import combiner_enter
from tools.uniqbiner import uniqbiner_enter
from plugins.idcard import get_idcard_post
from plugins.extend import get_extend_dic
from plugins.passcraper import get_passcratch_dic
from lib.text import pydictor_ascii_text as pydictor_art_text
from lib.data import set_result_store_path, get_result_store_path, set_conf_path, get_conf_path, tool_range, plug_range,\
    CRLF, scrabble_site_path, startime


if __name__ == '__main__':
    print("{}".format(cool.green(pydictor_art_text)))
    args = parse_args()
    try:
        if not os.path.exists(get_result_store_path()):
            os.mkdir(get_result_store_path())
    except IOError:
        exit(CRLF + cool.red("[-] Cannot create %s " % get_result_store_path()))
    if args.output:
        if os.path.exists(args.output):
            tmppath = os.path.abspath(args.output)
        else:
            try:
                os.mkdir(args.output)
                tmppath = os.path.abspath(args.output)
            except IOError:
                tmppath = ""
                print(CRLF + cool.red("[-] Cannot create %s, default %s" % (args.output, get_result_store_path())))
        if os.path.isdir(tmppath):
            set_result_store_path(tmppath)
    if args.base:
        get_base_dic(args.len[0], args.len[1], args.base, args.encode, args.head, args.tail)
    elif args.customchar:
        get_char_dic(args.len[0], args.len[1], args.customchar, args.encode, args.head, args.tail)
    elif args.chunk:
        chunk = []
        for item in args.chunk:
            if item != '':
                chunk.append(item)
        get_chunk_dic(chunk, args.encode, args.head, args.tail)
    elif args.plugins:
        if args.plugins[0] not in plug_range:
            exit("[!] Choose plug from ({0}, {1}, {2}, {3})".format
                 (cool.fuchsia(plug_range[0]), cool.fuchsia(plug_range[1]), cool.fuchsia(plug_range[2]),
                  cool.fuchsia(plug_range[3])))
        else:
            # id card plugin
            if len(args.plugins) == 1 and args.plugins[0] == plug_range[0]:
                get_idcard_post(plug_range[0], args.encode, args.head, args.tail, args.sex)
            elif len(args.plugins) == 1 and args.plugins[0] == plug_range[1]:
                get_idcard_post(plug_range[1], args.encode, args.head, args.tail, args.sex)
            # extend_enter plugin
            elif len(args.plugins) == 2 and args.plugins[0] == plug_range[2]:
                if os.path.isfile(args.plugins[1]):
                    with open(args.plugins[1], 'r') as f:
                        get_extend_dic(f.readlines(), encodeflag=args.encode)
                else:
                    exit(CRLF + cool.red("[-] File:%s don't exists" % args.plugins[1]))
            # passcraper plugin
            elif len(args.plugins) == 1 and args.plugins[0] == plug_range[3] and os.path.isfile(scrabble_site_path):
                get_passcratch_dic(encodeflag=args.encode)
            elif len(args.plugins) == 2 and args.plugins[0] == plug_range[3]:
                get_passcratch_dic(args.plugins[1], encodeflag=args.encode)
            elif len(args.plugins) == 1:
                exit(CRLF + "[-] Plug %s need other arguments" % cool.red(args.plugins[0]))
            else:
                exit(CRLF + cool.red("[-] Argument option error"))
    elif args.sedb:
        try:
            shell = SEDB()
            shell.cmdloop()
        except Exception as e:
            exit(e)
    elif args.conf != 'default':
        if args.conf == 'const':
            if os.path.isfile(get_conf_path()):
                build_conf_dic()
        elif os.path.isfile(args.conf):
            set_conf_path(args.conf)
            build_conf_dic()
        else:
            exit(CRLF + cool.red("[-] Please specify the exists configuration file"))
    elif args.tool:
        if len(args.tool) >= 1:
            if args.tool[0] in tool_range:
                # shredder
                if args.tool[0] == tool_range[0]:
                    if len(args.tool) == 1 and os.listdir(get_result_store_path()):
                        shredder_enter(get_result_store_path())
                    elif len(args.tool) == 1:
                        exit(CRLF + cool.orange("[+] %s has been clean" % get_result_store_path()))
                    elif len(args.tool) == 2:
                        shredder_enter(args.tool[1])
                    else:
                        exit(CRLF + cool.red("[-] %s arguments wrong" % tool_range[0]))
                    print("[+] Cost    :{} seconds".format(cool.orange(str(time.time() - startime)[:6])))
                # uniqifer
                elif len(args.tool) == 2 and args.tool[0] == tool_range[1]:
                    if os.path.isfile(args.tool[1]):
                        uniqifer_enter(args.tool[1])
                    else:
                        exit(CRLF + "[-] Please specify the exists file for %s" % cool.red(tool_range[1]))
                # counter
                elif len(args.tool) >= 2 and args.tool[0] == tool_range[2]:
                    counter_enter(args.encode, args.head, args.tail, args.tool)
                # combiner
                elif len(args.tool) == 2 and args.tool[0] == tool_range[3]:
                    combiner_enter(args.tool[1])
                # uniqbiner
                elif len(args.tool) == 2 and args.tool[0] == tool_range[4]:
                    uniqbiner_enter(args.tool[1])
                else:
                    exit(CRLF + cool.red("[-] Need other extra arguments"))
            else:
                exit(CRLF + cool.red("[-] No tool named %s" % args.tool[0]) +
                     CRLF + "[!] Choose tool from  ({0}, {1}, {2}, {3}, {4})".format(cool.fuchsia(tool_range[0]),
                                                                                     cool.fuchsia(tool_range[1]),
                                                                                     cool.fuchsia(tool_range[2]),
                                                                                     cool.fuchsia(tool_range[3]),
                                                                                     cool.fuchsia(tool_range[4])))
        else:
            exit(CRLF + cool.red("[-] Please specified tool name"))

