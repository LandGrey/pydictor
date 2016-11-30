#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-11-30
#
# store some common public data or simple function for others import
#
# This is a part of pydictor

import os
import sys
import time
from lib.encode import *

# results store path
resultstorepath = os. path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "results")

# format the time of build the dictionary
buildtime = str(time.strftime("%Y%m%d_%H.%M.%S", time.localtime(time.time())))

# encode operator
operator = {'b64': base64_encode, 'md5': md5_encode, 'md516': md5_16_encode, 'sha1': sha1_encode,
            'url': url_encode, 'sha256': sha256_encode, 'sha512': sha512_encode}


# finish print
def finishprint(count, storepath):
    print "[+] A total of %s lines" % str(count) + "\n" +\
          "[+] Store in %s " % storepath