#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-11-30
#
# store some common public variable or simple function for others import
#
# This is a part of pydictor

import os
import sys
import time
from lib.encode import *
from lib.command import parse_args


# results store path as default
resultstorepath = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "results")
if not os.path.exists(resultstorepath):
    os.mkdir(resultstorepath)

args = parse_args()
if args.output:
    tmppath = ""
    if os.path.exists(args.output):
        tmppath = os.path.abspath(args.output)
    else:
        try:
            os.mkdir(args.output)
            tmppath = os.path.abspath(args.output)
            if not os.path.exists(tmppath):
                print "[-] %s is not a valid path, use default" % args.output
        except:
            print "[-] %s cannot create, use default" % args.output
            pass
    if os.path.isdir(tmppath):
        resultstorepath = tmppath


# format the time of build the dictionary
buildtime = str(time.strftime("%Y%m%d_%H.%M.%S", time.localtime(time.time())))

# encode operator
operator = {'b64': base64_encode, 'md5': md5_encode, 'md516': md5_16_encode, 'sha1': sha1_encode,
            'url': url_encode, 'sha256': sha256_encode, 'sha512': sha512_encode}


# finish print
def finishprint(count, storepath):
    print "[+] A total of %s lines\n" % str(count) +\
          "[+] Store in %s " % storepath