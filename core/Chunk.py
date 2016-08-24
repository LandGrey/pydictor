#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-08-10
#
# build a chunk multiplication dictionary
#

import os
import time
import itertools
from lib.encode import *

operator = {'b64': base64_encode, 'md5': md5_encode, 'md516': md5_16_encode, 'sha1': sha1_encode,
            'url': url_encode, 'sha256': sha256_encode, 'sha512': sha512_encode}


# create the dictionary files
def get_chunk_dic(objflag, encodeflag, head, tail):
    count = 0
    storepath = os.path.join(os.getcwd(), "results", "[ChunkMulti]_[date_%s]_%s.txt" %
                           (str(time.strftime("%Y%m%d_%H.%M.%S",time.localtime(time.time()))), encodeflag))
    with open(storepath, "w") as f:
        for item in itertools.permutations(objflag, len(objflag)):
            if encodeflag == "":
                f.write(head+"".join(item)+tail+"\n")
                count += 1
            else:
                f.write(operator.get(encodeflag)(head + "".join(item) + tail) + "\n")
                count += 1
    print "[+] A total of %s lines" % str(count)
    print "[+] Store in %s " % storepath
