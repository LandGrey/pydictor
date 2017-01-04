#!/usr/bin/env python
# coding:utf-8
# A useful hacker dictionary  builder
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

import os
from lib.fun import cleaner
from lib.text import pydictor_ascii_text_2 as pydictor_art_text
from lib.data import set_result_store_path, get_result_store_path, set_conf_path, get_conf_path, CRLF
from lib.command import parse_args
from core.BASE import get_base_dic
from core.BASE import getchars
from core.CHUNK import get_chunk_dic
from core.CONF import build_conf_dic
from core.SEDB import SEDB
from plugins.idcard import getIDCardPost


if __name__ == '__main__':
    print pydictor_art_text
    args = parse_args()
    try:
        if not os.path.exists(get_result_store_path()):
            os.mkdir(get_result_store_path())
    except:
        print CRLF + "[-] Cannot create %s " % get_result_store_path()
        exit()
    if args.output:
        if os.path.exists(args.output):
            tmppath = os.path.abspath(args.output)
        else:
            try:
                os.mkdir(args.output)
                tmppath = os.path.abspath(args.output)
            except:
                tmppath = ""
                print CRLF + "[-] Cannot create %s, default use %s" % (args.output, get_result_store_path())
        if os.path.isdir(tmppath):
            set_result_store_path(tmppath)


    if args.type:
        get_base_dic(args.len[0], args.len[1], getchars(args.type), args.encode, args.head, args.tail)
    elif args.customchar:
        get_base_dic(args.len[0], args.len[1], args.customchar, args.encode, args.head, args.tail)
    elif args.chunk:
        chunk = []
        for item in args.chunk:
            if item != '':
                chunk.append(item)
        get_chunk_dic(chunk, args.encode, args.head, args.tail)
    elif args.plugins:
        if args.plugins == 'pid6':
            getIDCardPost('pid6', args.encode, args.head, args.tail, args.sex)
        elif args.plugins == 'pid8':
            getIDCardPost('pid8', args.encode, args.head, args.tail, args.sex)
    elif args.sedb:
        try:
            shell = SEDB()
            shell.cmdloop()
        except:
            exit()
    elif args.conf != 'default':
        if args.conf == 'const':
            if os.path.exists(get_conf_path()):
                build_conf_dic()
        elif os.path.exists(args.conf):
            set_conf_path(args.conf)
            build_conf_dic()
        else:
            print CRLF + "[-] Please specified the exists configuration file"
            exit()

    if args.clean != 'default':
        if args.clean == 'const':
            cleaner(get_result_store_path())
        else:
            cleaner(args.clean)
