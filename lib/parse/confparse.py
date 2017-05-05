#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import re
import string
from lib.fun.fun import cool
from lib.data.data import pystrs, pyoptions


def confmatcher(confpath):
    configures = []
    with open(confpath) as f:
        for item in f.readlines():
            confline = item.strip()
            if len(confline) >= 1 and confline[0] == pyoptions.annotator:
                pass
            else:
                matches = re.findall('(.*?)\[(.*?)\]\{(.*?)\}\<(.*?)\>([^[]*)', confline)
                for match in matches:
                    for m in match:
                        configures.append(m)
    if configures:
        if len(configures) // 5 > 10:
            exit(pyoptions.CRLF + cool.red('[-] Max support 10 parser'))
        else:
            return configures
    else:
        exit(pyoptions.CRLF + cool.red('[-] Match configuration file for nothing'))


def elementparser(configures):
    for x in range(1, len(configures) + 1):
        count = x - 1
        x %= 5
        if x == 1:
            pystrs.dicts[pystrs.conf_head].append(configures[count])
        elif x == 2:
            _ = []
            for i in range(len(configures[count].split(pyoptions.chars_split))):
                if pyoptions.char_range_split in configures[count].split(pyoptions.chars_split)[i] and \
                                len(configures[count].split(pyoptions.chars_split)[i].split(pyoptions.char_range_split)) == 2:
                    start = configures[count].split(pyoptions.chars_split)[i].split(pyoptions.char_range_split)[0]
                    end = configures[count].split(pyoptions.chars_split)[i].split(pyoptions.char_range_split)[1]
                    for c in string.printable:
                        if start <= c <= end:
                            _.append(c)
                else:
                    _.append(configures[count].split(pyoptions.chars_split)[i])
            pystrs.dicts[pystrs.conf_char].append(_)
        elif x == 3:
            pystrs.dicts[pystrs.conf_minlen].append(configures[count].split(pyoptions.length_split)[0])
            pystrs.dicts[pystrs.conf_maxlen].append(configures[count].split(pyoptions.length_split)[1])
        elif x == 4:
            pystrs.dicts[pystrs.conf_encode].append(configures[count])
        elif x == 0:
            pystrs.dicts[pystrs.conf_tail].append(configures[count])
    return pystrs.dicts
