#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import itertools
from lib.parse.confparse import elementparser, confmatcher
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.fun import finishprinter, finishcounter, countchecker, lengthchecker, range_compatible, cool, mybuildtime


def get_conf_dic(minlength, maxlength, objflag, encodeflag, head, tail):
    diclist = []
    for i in range_compatible(minlength, maxlength+1):
        for item in itertools.product(objflag, repeat=i):
            if encodeflag in pyoptions.operator.keys():
                diclist.append(pyoptions.operator.get(encodeflag)(head + "".join(item) + tail))
            else:
                exit(pyoptions.CRLF + cool.red('[-] wrong encode type'))
    # items count check
    countchecker(-1, len(diclist))
    return diclist


# if you have better way to actualize it, please pull request
def build_conf_dic():
    try:
        confdicts = elementparser(confmatcher(paths.buildconf_path))
    except IndexError:
        exit(cool.red("[-] parse element error, please check your parsing element"))

    finalen = len(confdicts[pystrs.conf_head])
    alllist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    storepath = os.path.join(paths.results_path, "%s_%s%s" %
                             (pystrs.CONF_prefix, mybuildtime(), pyoptions.filextension))
    for x in range(0, finalen):
        lengthchecker(confdicts[pystrs.conf_minlen][x], confdicts[pystrs.conf_maxlen][x])
        alllist[x] = get_conf_dic(int(confdicts[pystrs.conf_minlen][x]), int(confdicts[pystrs.conf_maxlen][x]),
                                  confdicts[pystrs.conf_char][x], confdicts[pystrs.conf_encode][x],
                                  confdicts[pystrs.conf_head][x], confdicts[pystrs.conf_tail][x])
    if finalen == 1:
        countchecker(-1, len(alllist[0]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0]):
                f.write("".join(item) + pyoptions.CRLF)
    elif finalen == 2:
        countchecker(-1, len(alllist[0]), len(alllist[1]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1]):
                f.write("".join(item) + pyoptions.CRLF)
    elif finalen == 3:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2]):
                f.write("".join(item) + pyoptions.CRLF)
    elif finalen == 4:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3]):
                f.write("".join(item) + pyoptions.CRLF)
    elif finalen == 5:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4]):
                f.write("".join(item) + pyoptions.CRLF)
    elif finalen == 6:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]),
                     len(alllist[5]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4], alllist[5]):
                f.write("".join(item) + pyoptions.CRLF)
    elif finalen == 7:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]),
                     len(alllist[5]), len(alllist[6]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4], alllist[5],
                                          alllist[6]):
                f.write("".join(item) + pyoptions.CRLF)
    elif finalen == 8:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]),
                     len(alllist[5]), len(alllist[6]), len(alllist[7]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4], alllist[5],
                                          alllist[6], alllist[7]):
                f.write("".join(item) + pyoptions.CRLF)
    elif finalen == 9:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]),
                     len(alllist[5]), len(alllist[6]), len(alllist[7]), len(alllist[8]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4], alllist[5],
                                          alllist[6], alllist[7], alllist[8]):
                f.write("".join(item) + pyoptions.CRLF)
    elif finalen == 10:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]),
                     len(alllist[5]), len(alllist[6]), len(alllist[7]), len(alllist[8]), len(alllist[9]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4], alllist[5],
                                          alllist[6], alllist[7], alllist[8], alllist[9]):
                f.write("".join(item) + pyoptions.CRLF)

    finishprinter(finishcounter(storepath), storepath)
