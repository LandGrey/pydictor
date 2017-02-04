#!/usr/bin/env python
# coding:utf-8
# A useful hacker dictionary  builder
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
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
from plugins.extend import getExtendDic


if __name__ == '__main__':
    print(pydictor_art_text)
    args = parse_args()

    try:
        if not os.path.exists(get_result_store_path()):
            os.mkdir(get_result_store_path())
    except IOError:
        exit(CRLF + "[-] Cannot create %s " % get_result_store_path())
    if args.output:
        if os.path.exists(args.output):
            tmppath = os.path.abspath(args.output)
        else:
            try:
                os.mkdir(args.output)
                tmppath = os.path.abspath(args.output)
            except IOError:
                tmppath = ""
                print(CRLF + "[-] Cannot create %s, default %s" % (args.output, get_result_store_path()))
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
        if len(args.plugins) == 1 and args.plugins[0] == 'pid6':
            getIDCardPost('pid6', args.encode, args.head, args.tail, args.sex)
        elif len(args.plugins) == 1 and args.plugins[0] == 'pid8':
            getIDCardPost('pid8', args.encode, args.head, args.tail, args.sex)
        elif len(args.plugins) == 1 and args.plugins[0] == 'extend':
            exit(CRLF + "[-] extend file don't specified")
        elif len(args.plugins) == 2 and args.plugins[0] == 'extend':
            if os.path.isfile(args.plugins[1]):
                with open(args.plugins[1], 'r') as f:
                    getExtendDic(f.readlines(), encodeflag=args.encode, )
            else:
                exit(CRLF + "[-] file:%s don't exists" % args.plugins[1])
        else:
            exit(CRLF + "[-] argument option error")
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
            exit(CRLF + "[-] Please specified the exists configuration file")

    if args.clean != 'default':
        if args.clean == 'const':
            if os.listdir(get_result_store_path()):
                cleaner(get_result_store_path())
            else:
                exit(CRLF + "[+] %s has been clean" % get_result_store_path())
        else:
            cleaner(args.clean)
