#!/usr/bin/env python
# coding:utf-8
# Build a dictionary based on configuration file
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import itertools
from lib.confparse import confmatcher
from lib.confparse import confparser
from lib.fun import finishprinter, finishcounter, countchecker, lengthchecker, range_compatible, cool
from lib.data import get_result_store_path, get_conf_path, get_buildtime, operator, CRLF, CONF_prefix, filextension, \
    head, char, minlen, maxlen, encode, tail


def get_conf_dic(minlength, maxlength, objflag, encodeflag, head, tail):
    diclist = []
    for i in range_compatible(minlength, maxlength+1):
        for item in itertools.product(objflag, repeat=i):
            if encodeflag in operator.keys():
                diclist.append(operator.get(encodeflag)(head + "".join(item) + tail))
            else:
                exit(CRLF + cool.red('[-] wrong encode type'))

    # items count check
    countchecker(-1, len(diclist))
    return diclist


# if you have better way to actualize it, please pull request
def build_conf_dic():
    confdicts = confparser(confmatcher(get_conf_path()))
    finalen = len(confdicts[head])
    alllist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    storepath = os.path.join(get_result_store_path(), "%s_%s%s" % (CONF_prefix, get_buildtime(), filextension))
    for x in range(0, finalen):
        lengthchecker(confdicts[minlen][x], confdicts[maxlen][x])
        alllist[x] = get_conf_dic(int(confdicts[minlen][x]), int(confdicts[maxlen][x]), confdicts[char][x],
                                  confdicts[encode][x], confdicts[head][x], confdicts[tail][x])
    if finalen == 1:
        countchecker(-1, len(alllist[0]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0]):
                f.write("".join(item) + CRLF)
    elif finalen == 2:
        countchecker(-1, len(alllist[0]), len(alllist[1]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1]):
                f.write("".join(item) + CRLF)
    elif finalen == 3:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2]):
                f.write("".join(item) + CRLF)
    elif finalen == 4:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3]):
                f.write("".join(item) + CRLF)
    elif finalen == 5:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4]):
                f.write("".join(item) + CRLF)
    elif finalen == 6:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]),
                     len(alllist[5]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4], alllist[5]):
                f.write("".join(item) + CRLF)
    elif finalen == 7:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]),
                     len(alllist[5]), len(alllist[6]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4], alllist[5],
                                          alllist[6]):
                f.write("".join(item) + CRLF)
    elif finalen == 8:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]),
                     len(alllist[5]), len(alllist[6]), len(alllist[7]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4], alllist[5],
                                          alllist[6], alllist[7]):
                f.write("".join(item) + CRLF)
    elif finalen == 9:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]),
                     len(alllist[5]), len(alllist[6]), len(alllist[7]), len(alllist[8]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4], alllist[5],
                                          alllist[6], alllist[7], alllist[8]):
                f.write("".join(item) + CRLF)
    elif finalen == 10:
        countchecker(-1, len(alllist[0]), len(alllist[1]), len(alllist[2]), len(alllist[3]), len(alllist[4]),
                     len(alllist[5]), len(alllist[6]), len(alllist[7]), len(alllist[8]), len(alllist[9]))
        with open(storepath, "a") as f:
            for item in itertools.product(alllist[0], alllist[1], alllist[2], alllist[3], alllist[4], alllist[5],
                                          alllist[6], alllist[7], alllist[8], alllist[9]):
                f.write("".join(item) + CRLF)

    finishprinter(finishcounter(storepath), storepath)
