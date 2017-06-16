#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import string
from lib.fun.osjudger import py_ver_egt_3
from lib.data.data import paths, pyoptions
from lib.fun.fun import walk_pure_file, rreplace


def get_leet_cfg():
    leet_mode = dict()
    leets = walk_pure_file(paths.leetmode_path, pure=False)
    for _ in leets:
        chunk = _.split(pyoptions.key_value_split)
        leet_mode[chunk[0].strip()] = chunk[1].strip()
    return leet_mode.items()


# leet mode magic function
def leet_mode_magic(strings, code, *args):
    intab = outtab = ""
    if code == 0:
        for leet in get_leet_cfg():
            intab += leet[0]
            outtab += leet[1]
        if not py_ver_egt_3():
            maptab = string.maketrans(intab, outtab)
            ret = str(strings).translate(maptab)
        else:
            maptab = str.maketrans(intab, outtab)
            ret = strings.translate(maptab)
        return ret
    elif 11 <= code <= 29 or 1 <= code <= 2:
        if 21 <= code <= 29 or code == 2:
            searchstrs = strings[::-1]
        else:
            searchstrs = strings

        search = 0
        ret = strings
        searchover = len(searchstrs)
        for s in searchstrs:
            search += 1
            for leet in get_leet_cfg():
                if leet[0] == s:
                    if code == 1:
                        ret = strings.replace(leet[0], leet[1])
                        return ret
                    elif code == 2:
                        ret = rreplace(strings, leet[0], leet[1])
                        return ret
                    elif 11 <= code <= 19:
                        ret = strings.replace(leet[0], leet[1], code % 10)
                        return ret
                    elif 21 <= code <= 29:
                        ret = rreplace(strings, leet[0], leet[1], code % 20)
                        return ret
                    else:
                        return strings
            if search >= searchover:
                return ret
    else:
        return strings
