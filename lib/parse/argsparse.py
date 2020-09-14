#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
from lib.fun.fun import cool
from core.CONF import build_conf_dic
from core.PATTERN import build_pattern_dic
from lib.data.data import paths, pyoptions


def plug_parser():
    if pyoptions.args_plug[0] not in pyoptions.plug_range:
        exit("[!] Choose plugin from ({0})".format(cool.fuchsia(",".join(pyoptions.plug_range))))
    else:
        pyoptions.plugins_operator.get(pyoptions.args_plug[0])(pyoptions.args_plug)


def conf_parser():
    if pyoptions.args_conf == 'const':
        if os.path.isfile(paths.buildconf_path):
            build_conf_dic(source=paths.buildconf_path)
    else:
        paths.buildconf_path = pyoptions.args_conf
        build_conf_dic(source=paths.buildconf_path)


def pattern_parser():
    build_pattern_dic(source=pyoptions.args_pattern)


def tool_parser():
    if len(pyoptions.args_tool) >= 1:
        if pyoptions.args_tool[0] in pyoptions.tool_range:
            pyoptions.tools_operator.get(pyoptions.args_tool[0])(pyoptions.args_tool)
        else:
            exit(pyoptions.CRLF + "[!] Choose tool from ({})".format(cool.fuchsia(" ".join(pyoptions.tool_range))))
    else:
        exit(pyoptions.CRLF + cool.red("[-] Please specified tool name"))
