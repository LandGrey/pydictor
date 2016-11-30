#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-08-25
#
# build a chunk multiplication dictionary
#
# This is a part of pydictor


import itertools
from lib.data import *


# create the dictionary files
def get_chunk_dic(objflag, encodeflag, head, tail):
    count = 0
    storepath = os.path.join(resultstorepath, "Chunk_%s_%s.txt" %
                            (buildtime, encodeflag))
    with open(storepath, "w") as f:
        for item in itertools.permutations(objflag, len(objflag)):
            if encodeflag == "":
                f.write(head+"".join(item)+tail+"\n")
                count += 1
            else:
                f.write(operator.get(encodeflag)(head + "".join(item) + tail) + "\n")
                count += 1
    finishprint(count, storepath)
