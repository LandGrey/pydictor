#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import re
from lib.fun.fun import cool, charanger
from lib.data.data import pystrs, pyoptions


def confmatcher(resource):
    configures = []
    if not os.path.isfile(resource):
        matches = re.findall(pyoptions.confpattern, resource.strip())
        for match in matches:
            for m in match:
                configures.append(m.strip())
    else:
        with open(resource) as f:
            for item in f.readlines():
                confline = item.strip()
                if len(confline) >= 1 and confline[0] == pyoptions.annotator:
                    pass
                else:
                    matches = re.findall(pyoptions.confpattern, confline)
                    for match in matches:
                        for m in match:
                            configures.append(m.strip())
    if configures:
        if len(configures) // 5 > 10:
            exit(pyoptions.CRLF + cool.red('[-] Max support 10 parser'))
        else:
            return configures
    else:
        exit(pyoptions.CRLF + cool.red('[-] Match configuration file for nothing'))


def elementparser(configures):
    dicts = {pystrs.conf_head: [], pystrs.conf_char: [], pystrs.conf_minlen: [], pystrs.conf_maxlen: [], 
             pystrs.conf_encode: [], pystrs.conf_tail: []}
    for x in range(1, len(configures) + 1):
        count = x - 1
        x %= 5
        if x == 1:
            dicts[pystrs.conf_head].append(configures[count].strip())
        elif x == 2:
            dicts[pystrs.conf_char].append(charanger(configures[count]))
        elif x == 3:
            dicts[pystrs.conf_minlen].append(configures[count].split(pyoptions.length_split)[0])
            dicts[pystrs.conf_maxlen].append(configures[count].split(pyoptions.length_split)[1])
        elif x == 4:
            dicts[pystrs.conf_encode].append(configures[count])
        elif x == 0:
            dicts[pystrs.conf_tail].append(configures[count].strip())
    return dicts
