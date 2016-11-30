#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-11-27
#
# Chinese identity card post 6/8 numbers build plugins base on sex
#
# This is a part of pydictor

from lib.data import *


def getIDCardPost(posflag, encodeflag, head, tail, sex):
    count = 0
    storepath = os.path.join(resultstorepath, "IdCardPost%s_%s_%s.txt" %
                            (str(posflag)[-1:], buildtime, encodeflag))
    posrule = lambda _: str(_) if _ >= 10 else "0" + str(_)
    # month
    value1112 = " ".join(posrule(x) for x in xrange(1, 13))
    # day
    value1314 = " ".join(posrule(x) for x in xrange(1, 32))
    value1516 = " ".join(posrule(x) for x in xrange(1, 100))
    post18 = "0 1 2 3 4 5 6 7 8 9 X"
    value1718 = ""
    if sex == 'm':
        rand = "1 3 5 7 9"
        for _ in rand.split(' '):
            for _p in post18.split(' '):
                value1718 += _ + _p + " "
    elif sex == 'f':
        rand = "0 2 4 6 8"
        for _ in rand.split(' '):
            for _p in post18.split(' '):
                value1718 += _ + _p + " "
    else:
        rand = " ".join(str(_) for _ in xrange(10))
        for _ in rand.split(' '):
            for _p in post18.split(' '):
                value1718 += _ + _p + " "
    with open(storepath, "w") as f:
        if posflag == 'pid8':
            for v1112 in value1112.split(' '):
                for v1314 in value1314.split(' '):
                    for v1516 in value1516.split(' '):
                        for v1718 in value1718.split(' '):
                            if v1718 != "":
                                if encodeflag == "":
                                    f.write(head + v1112 + v1314 + v1516 + v1718 + tail + "\n")
                                    count += 1
                                else:
                                    f.write(operator.get(encodeflag)(head + v1112 + v1314 + v1516 + v1718 + tail) + "\n")
                                    count += 1
        elif posflag == 'pid6':
                for v1314 in value1314.split(' '):
                    for v1516 in value1516.split(' '):
                        for v1718 in value1718.split(' '):
                            if v1718 != "":
                                if encodeflag == "":
                                    f.write(head + v1314 + v1516 + v1718 + tail + "\n")
                                    count += 1
                                else:
                                    f.write(operator.get(encodeflag)(head + v1314 + v1516 + v1718 + tail) + "\n")
                                    count += 1
    finishprint(count, storepath)

