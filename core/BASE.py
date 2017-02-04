#!/usr/bin/env python
# coding:utf-8
# build a common dictionary 
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import string
import itertools
from lib.data import get_result_store_path, get_buildtime, operator, CRLF, BASE_prefix, filextension, range_compatible
from lib.fun import finishprinter, finishcounter
from lib.fun import countchecker

# dictionary type
description = " "


# get the dictionary list
def getchars(typeflag):
    global description
    flag = str(typeflag)
    chars = []
    if flag == "d":
        chars = string.digits
        description = 'digits'
    elif flag == "L":
        chars = string.ascii_lowercase
        description = 'lowercase'
    elif flag == "c":
        chars = string.ascii_uppercase
        description = 'uppercase'
    elif flag == "dL":
        chars = string.printable[:36]
        description = 'digits_lowercase'
    elif flag == "dc":
        chars = string.digits + string.ascii_uppercase
        description = 'digits_uppercase'
    elif flag == "Lc":
        chars = string.ascii_letters
        description = 'letters'
    elif flag == "dLc":
        chars = string.printable[:62]
        description = 'digits_letters'
    return chars


# create the dictionary files
def get_base_dic(minlength, maxlength, objflag, encodeflag, head, tail):
    countchecker(len(objflag), minlength, maxlength)
    global description
    storepath = os.path.join(get_result_store_path(), "%s_%s_%s_%s_%s_%s%s" %
                             (BASE_prefix, minlength, maxlength, description, get_buildtime(), encodeflag, filextension))
    with open(storepath, "w") as f:
        for i in range_compatible(minlength, maxlength+1):
            for item in itertools.product(objflag, repeat=i):
                if encodeflag == "":
                    f.write(head+"".join(item)+tail + CRLF)
                else:
                    f.write(operator.get(encodeflag)(head + "".join(item) + tail) + CRLF)
    finishprinter(finishcounter(storepath), storepath)
