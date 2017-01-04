#!/usr/bin/env python
# coding:utf-8
# build a common dictionary
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

import re
import string
from lib.data import head, char, minlen, maxlen, encode, tail
from lib.data import dicts, char_range_split, chars_split, length_split, conf_annotator


def confmatcher(confpath):
    configures = []
    with open(confpath) as f:
        for item in f.readlines():
            confline = item.strip()
            if len(confline) >= 1 and confline[0] == conf_annotator:
                pass
            else:
                matches = re.findall('(.*?)\[(.*?)\]\{(.*?)\}\<(.*?)\>([^[]*)', confline)
                for match in matches:
                    for m in match:
                        configures.append(m)
    if configures:
        if len(configures) / 5 > 10:
            print '[-] Max support 10 parser'
            exit()
        else:
            return configures
    else:
        print '[-] Match configuration file for nothing'
        exit()


def confparser(configures):
    for x in range(1, len(configures) + 1):
        count = x - 1
        x %= 5
        if x == 1:
            dicts[head].append(configures[count])
        elif x == 2:
            _ = []
            for i in range(len(configures[count].split(chars_split))):
                if char_range_split in configures[count].split(chars_split)[i] and \
                                len(configures[count].split(chars_split)[i].split(char_range_split)) == 2:
                    start = configures[count].split(chars_split)[i].split(char_range_split)[0]
                    end = configures[count].split(chars_split)[i].split(char_range_split)[1]
                    for c in string.printable:
                        if start <= c <= end:
                            _.append(c)
                else:
                    _.append(configures[count].split(chars_split)[i])
            dicts[char].append(_)
        elif x == 3:
            dicts[minlen].append(configures[count].split(length_split)[0])
            dicts[maxlen].append(configures[count].split(length_split)[1])
        elif x == 4:
            dicts[encode].append(configures[count])
        elif x == 0:
            dicts[tail].append(configures[count])
    return dicts

