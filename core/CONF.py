#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import itertools
from lib.fun.filter import filterforfun
from lib.data.data import paths, pystrs, pyoptions
from lib.parse.confparse import elementparser, confmatcher
from lib.fun.fun import finishprinter, finishcounter, countchecker, lengthchecker, range_compatible, cool, mybuildtime,\
    finalsavepath


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


def build_conf_dic(source="", file_prefix=pystrs.CONF_prefix):
    storepath = finalsavepath(paths.results_path, file_prefix, mybuildtime(), pyoptions.filextension, paths.results_file_name)
    with open(storepath, "a") as f:
        for item in confcore(source):
            item = filterforfun(item, head=pyoptions.head, tail=pyoptions.tail,
                                lenght_is_filter=pyoptions.args_pick,
                                minlen=pyoptions.minlen, maxlen=pyoptions.maxlen,
                                regex_is_filter=True, regex=pyoptions.filter_regex,
                                encode_is_filter=True, encode=pyoptions.encode,
                                occur_is_filter=True,
                                letter_occur=pyoptions.letter_occur,
                                digital_occur=pyoptions.digital_occur,
                                special_occur=pyoptions.special_occur,
                                types_is_filter=True,
                                letter_types=pyoptions.letter_types,
                                digital_types=pyoptions.digital_types,
                                special_types=pyoptions.special_types,
                                )
            if item:
                f.write(item + pyoptions.CRLF)
    finishprinter(finishcounter(storepath), storepath)


# if you have better way to actualize it, please pull request
def confcore(resource):
    try:
        confdicts = elementparser(confmatcher(resource))
    except IndexError:
        confdicts = {}
        exit(cool.red("[-] parse element error, please check your parsing element"))
    finalen = len(confdicts[pystrs.conf_head])
    listpool = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(0, finalen):
        lengthchecker(confdicts[pystrs.conf_minlen][x], confdicts[pystrs.conf_maxlen][x])
        listpool[x] = get_conf_dic(int(confdicts[pystrs.conf_minlen][x]), int(confdicts[pystrs.conf_maxlen][x]),
                                  confdicts[pystrs.conf_char][x], confdicts[pystrs.conf_encode][x],
                                  confdicts[pystrs.conf_head][x], confdicts[pystrs.conf_tail][x])
    if finalen == 1:
        countchecker(-1, len(listpool[0]))
        for item in itertools.product(listpool[0]):
            yield "".join(item)
    elif finalen == 2:
        countchecker(-1, len(listpool[0]), len(listpool[1]))
        for item in itertools.product(listpool[0], listpool[1]):
            yield "".join(item)
    elif finalen == 3:
        countchecker(-1, len(listpool[0]), len(listpool[1]), len(listpool[2]))
        for item in itertools.product(listpool[0], listpool[1], listpool[2]):
            yield "".join(item)
    elif finalen == 4:
        countchecker(-1, len(listpool[0]), len(listpool[1]), len(listpool[2]), len(listpool[3]))
        for item in itertools.product(listpool[0], listpool[1], listpool[2], listpool[3]):
            # print("".join(item) + '\n')
            yield "".join(item)
    elif finalen == 5:
        countchecker(-1, len(listpool[0]), len(listpool[1]), len(listpool[2]), len(listpool[3]), len(listpool[4]))
        for item in itertools.product(listpool[0], listpool[1], listpool[2], listpool[3], listpool[4]):
            yield "".join(item)
    elif finalen == 6:
        countchecker(-1, len(listpool[0]), len(listpool[1]), len(listpool[2]), len(listpool[3]), len(listpool[4]),
                     len(listpool[5]))
        for item in itertools.product(listpool[0], listpool[1], listpool[2], listpool[3], listpool[4], listpool[5]):
            yield "".join(item)
    elif finalen == 7:
        countchecker(-1, len(listpool[0]), len(listpool[1]), len(listpool[2]), len(listpool[3]), len(listpool[4]),
                     len(listpool[5]), len(listpool[6]))
        for item in itertools.product(listpool[0], listpool[1], listpool[2], listpool[3], listpool[4], listpool[5],
                                      listpool[6]):
            yield "".join(item)
    elif finalen == 8:
        countchecker(-1, len(listpool[0]), len(listpool[1]), len(listpool[2]), len(listpool[3]), len(listpool[4]),
                     len(listpool[5]), len(listpool[6]), len(listpool[7]))
        for item in itertools.product(listpool[0], listpool[1], listpool[2], listpool[3], listpool[4], listpool[5],
                                      listpool[6], listpool[7]):
            yield "".join(item)
    elif finalen == 9:
        countchecker(-1, len(listpool[0]), len(listpool[1]), len(listpool[2]), len(listpool[3]), len(listpool[4]),
                     len(listpool[5]), len(listpool[6]), len(listpool[7]), len(listpool[8]))
        for item in itertools.product(listpool[0], listpool[1], listpool[2], listpool[3], listpool[4], listpool[5],
                                      listpool[6], listpool[7], listpool[8]):
            yield "".join(item)
    elif finalen == 10:
        countchecker(-1, len(listpool[0]), len(listpool[1]), len(listpool[2]), len(listpool[3]), len(listpool[4]),
                     len(listpool[5]), len(listpool[6]), len(listpool[7]), len(listpool[8]), len(listpool[9]))
        for item in itertools.product(listpool[0], listpool[1], listpool[2], listpool[3], listpool[4], listpool[5],
                                      listpool[6], listpool[7], listpool[8], listpool[9]):
            yield "".join(item)
