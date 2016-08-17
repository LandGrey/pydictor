#!/usr/bin/env python
# coding:utf-8
# Build by LandGrey 2016-08-17
#
# build a common dictionary
#

import os
import time
import string
import itertools
from lib.encode import *

operator = {'b64': base64_encode, 'md5': md5_encode, 'sha1': sha1_encode,
            'url': url_encode, 'sha256': sha256_encode,'sha512': sha512_encode}


# get the dictionary type
def getchars(typefalg):
    falg = str(typefalg)
    chars = []
    if falg == "d":
        chars = string.printable[:10]
    elif falg == "L":
        chars = string.printable[10:36]
    elif falg == "c":
        chars = string.printable[36:62]
    elif falg == "dL":
        chars = string.printable[:36]
    elif falg == "dc":
        chars = string.printable[:10]+string.printable[36:62]
    elif falg == "Lc":
        chars = string.printable[10:62]
    elif falg == "dLc":
        chars = string.printable[:62]
    return chars


# create the dictionary files
def get_base_dic(minlength, maxlength, objfalg, encodeflag, head, tail):
    count = 0
    storepath=os.path.join(os.getcwd(), "results", "[len_%s_%s]_[%s]_%s.txt" %
                           (minlength, maxlength, str(time.strftime("%Y%m%d_%H.%M.%S", time.localtime(time.time()))), encodeflag))
    with open(storepath, "w") as f:
        for i in xrange(minlength, maxlength+1):
            for item in itertools.product(objfalg, repeat=i):
                if encodeflag == "":
                    f.write(head+"".join(item)+tail+"\n")
                    count += 1
                else:
                    f.write(operator.get(encodeflag)(head+"".join(item)+tail)+"\n")
                    count += 1
    print "[+] A total of %s lines" % str(count)
    print "[+] Store in %s " % storepath
