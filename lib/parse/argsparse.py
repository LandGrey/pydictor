#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import time

from core.CONF import build_conf_dic
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.fun import cool
from plugins.idcard import idcard_magic
from plugins.passcraper import scraper_magic
from tools.handler import get_handler_dic
from tools.combiner import combiner_enter
from tools.counter import counter_enter
from tools.shredder import shredder_enter
from tools.uniqbiner import uniqbiner_enter
from tools.uniqifer import uniqifer_enter


def plug_parser():
    if pyoptions.args_plug[0] not in pystrs.plug_range:
        exit("[!] Choose plug from ({0}, {1}, {2})".format
             (cool.fuchsia(pystrs.plug_range[0]), cool.fuchsia(pystrs.plug_range[1]),
              cool.fuchsia(pystrs.plug_range[2])))
    else:
        # id card plugin
        if len(pyoptions.args_plug) == 1 and pyoptions.args_plug[0] == pystrs.plug_range[0]:
            idcard_magic(pystrs.plug_range[0])
        elif len(pyoptions.args_plug) == 1 and pyoptions.args_plug[0] == pystrs.plug_range[1]:
            idcard_magic(pystrs.plug_range[1])
        # passcraper plugin
        elif len(pyoptions.args_plug) == 1 and pyoptions.args_plug[0] == pystrs.plug_range[2] and \
                os.path.isfile(paths.scrapersites_path):
            scraper_magic()
        elif len(pyoptions.args_plug) == 2 and pyoptions.args_plug[0] == pystrs.plug_range[2]:
            scraper_magic(pyoptions.args_plug[1])
        elif len(pyoptions.args_plug) == 1:
            exit(pyoptions.CRLF + "[-] Plug %s need other arguments" % cool.red(pyoptions.args_plug[0]))
        else:
            exit(pyoptions.CRLF + cool.red("[-] Argument option error"))


def conf_parser():
    if pyoptions.args_conf == 'const':
        if os.path.isfile(paths.buildconf_path):
            build_conf_dic()
    elif os.path.isfile(pyoptions.args_conf):
        paths.buildconf_path = pyoptions.args_conf
        build_conf_dic()
    else:
        exit(pyoptions.CRLF + cool.red("[-] Please specify the exists configuration file"))


def tool_parser():
    if len(pyoptions.args_tool) >= 1:
        if pyoptions.args_tool[0] in pystrs.tool_range:

            # shredder
            if pyoptions.args_tool[0] == pystrs.tool_range[0]:
                if len(pyoptions.args_tool) == 1 and os.listdir(paths.results_path):
                    shredder_enter(paths.results_path)
                elif len(pyoptions.args_tool) == 1:
                    exit(pyoptions.CRLF + cool.orange("[+] %s has been clean" % paths.results_path))
                elif len(pyoptions.args_tool) == 2:
                    shredder_enter(pyoptions.args_tool[1])
                else:
                    exit(pyoptions.CRLF + cool.red("[-] %s arguments wrong" % pystrs.tool_range[0]))
                print("[+] Cost    :{} seconds".format(cool.orange(str(time.time() - pystrs.startime)[:6])))
            # uniqifer
            elif len(pyoptions.args_tool) == 2 and pyoptions.args_tool[0] == pystrs.tool_range[1]:
                if os.path.isfile(pyoptions.args_tool[1]):
                    uniqifer_enter(pyoptions.args_tool[1])
                else:
                    exit(pyoptions.CRLF + "[-] Please specify the exists file for %s" % cool.red(pystrs.tool_range[1]))
            # counter
            elif len(pyoptions.args_tool) >= 2 and pyoptions.args_tool[0] == pystrs.tool_range[2]:
                counter_enter(pyoptions.encode, pyoptions.head, pyoptions.tail, pyoptions.args_tool)
            # combiner
            elif len(pyoptions.args_tool) == 2 and pyoptions.args_tool[0] == pystrs.tool_range[3]:
                combiner_enter(pyoptions.args_tool[1])
            # uniqbiner
            elif len(pyoptions.args_tool) == 2 and pyoptions.args_tool[0] == pystrs.tool_range[4]:
                uniqbiner_enter(pyoptions.args_tool[1])
            # handler
            elif len(pyoptions.args_tool) == 2 and pyoptions.args_tool[0] == pystrs.tool_range[5]:
                get_handler_dic(pyoptions.args_tool[1])
            else:
                exit(pyoptions.CRLF + cool.red("[-] Need other extra arguments"))
        else:
            exit(pyoptions.CRLF + cool.red("[-] No tool named %s" % pyoptions.args_tool[0]) +
                 pyoptions.CRLF + "[!] Choose tool from  ({0}, {1}, {2}, {3}, {4}, {5})".format(
                cool.fuchsia(pystrs.tool_range[0]),
                cool.fuchsia(pystrs.tool_range[1]),
                cool.fuchsia(pystrs.tool_range[2]),
                cool.fuchsia(pystrs.tool_range[3]),
                cool.fuchsia(pystrs.tool_range[4]),
                cool.fuchsia(pystrs.tool_range[5]),
            ))
    else:
        exit(pyoptions.CRLF + cool.red("[-] Please specified tool name"))
