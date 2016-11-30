#!/usr/bin/env python
# coding:utf-8
# Build by LandGrey 2016-08-25
#
# build a common dictionary
#
# This is a part of pydictor


import string
import itertools
from lib.data import *


# dictionary type
description = " "


# get the dictionary list
def getchars(typeflag):
    global description
    falg = str(typeflag)
    chars = []
    if falg == "d":
        chars = string.digits
        description = 'digits'
    elif falg == "L":
        chars = string.lowercase
        description = 'lowercase'
    elif falg == "c":
        chars = string.uppercase
        description = 'uppercase'
    elif falg == "dL":
        chars = string.printable[:36]
        description = 'digits_lowercase'
    elif falg == "dc":
        chars = string.digits + string.uppercase
        description = 'digits_uppercase'
    elif falg == "Lc":
        chars = string.letters
        description = 'letters'
    elif falg == "dLc":
        chars = string.printable[:62]
        description = 'digits_letters'
    return chars


# create the dictionary files
def get_base_dic(minlength, maxlength, objflag, encodeflag, head, tail):
    global description
    count = 0
    storepath=os.path.join(resultstorepath, "%s_%s_%s_%s_%s.txt" %
                           (minlength, maxlength, description, buildtime, encodeflag))
    with open(storepath, "w") as f:
        for i in xrange(minlength, maxlength+1):
            for item in itertools.product(objflag, repeat=i):
                if encodeflag == "":
                    f.write(head+"".join(item)+tail+"\n")
                    count += 1
                else:
                    f.write(operator.get(encodeflag)(head+"".join(item)+tail)+"\n")
                    count += 1
    finishprint(count, storepath)
