#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
from lib.fun.leetmode import leet_mode_magic
from lib.data.data import paths, pystrs, pyoptions
from lib.fun.fun import cool, finishprinter, finishcounter, walks_all_files, walk_pure_file, mybuildtime


def raw_extend(_):
    yield _
    yield _ + _
    yield _[::-1]
    yield _ + _[::-1]
    yield _ + _.upper()
    yield _.capitalize()[::-1]
    yield _[::-1].capitalize()[::-1]
    yield _.capitalize() + _.capitalize()
    for h_t in walk_pure_file(paths.extendheadtail_path, pure=False):
        try:
            ht = str(h_t).split(' ')
            yield ht[0] + _ + ht[1]
        except:
            pass
    for prefix in walk_pure_file(paths.extendprefix_path):
        yield prefix + _
    for suffix in walk_pure_file(paths.extendsuffix_path):
        yield _ + suffix


def extend_enter(results, leet=True):
    for _ in results:
        _ = _.strip()
        # strange string
        if not _.isalpha():
            for x in raw_extend(_):
                yield x
        # mix lower and upper
        elif not (_.isupper() or _.islower()):
                for x in raw_extend(_):
                    yield x
        # lower string
        for x in raw_extend(_.lower()):
            yield x
        # upper string
        for x in raw_extend(_.upper()):
            yield x
        for x in raw_extend(_.capitalize()):
            yield x

        # use leet mode
        if leet:
            # strange string extend_enter directly
            if not _.isalpha():
                for x in raw_extend(leet_mode_magic(_)):
                    yield x
            elif not (_.isupper() or _.islower()):
                    for x in raw_extend(leet_mode_magic(_)):
                        yield x
            for x in raw_extend(leet_mode_magic(_.lower())):
                yield x


def extend_magic(rawlist, encodeflag='none', need_passcratch=False):
    prefix = pystrs.EXTEND_prefix
    if rawlist == []:
        exit(pyoptions.CRLF + cool.red("[-] raw extend_enter file cannot be empty"))

    leet = pyoptions.extend_leet
    if need_passcratch:
        prefix = pystrs.PASSCRAPER_prefix
        leet = pyoptions.passcraper_leet
        rawstorepath = os.path.join(paths.results_path, "%s_%s%s" % (pystrs.SCFATCH_prefix, mybuildtime(), pyoptions.filextension))
        with open(rawstorepath, "a") as f:
            for line in rawlist:
                f.write(str(line) + pyoptions.CRLF)

    finalstorepath = os.path.join(paths.results_path, "%s_%s%s" % (prefix, mybuildtime(), pyoptions.filextension))
    with open(finalstorepath, "a") as f:
        try:
            if not pyoptions.args_pick:
                for _ in walks_all_files(paths.weblist_path):
                    f.write(pyoptions.operator.get(encodeflag)(str(_) + pyoptions.CRLF))
                for _ in extend_enter(rawlist, leet=leet):
                    f.write(pyoptions.operator.get(encodeflag)(str(_) + pyoptions.CRLF))
            else:
                for _ in walks_all_files(paths.weblist_path):
                    if pyoptions.minlen <= len(_) <= pyoptions.maxlen:
                        f.write(pyoptions.operator.get(encodeflag)(str(_) + pyoptions.CRLF))
                for _ in extend_enter(rawlist, leet=leet):
                    if pyoptions.minlen <= len(_) <= pyoptions.maxlen:
                        f.write(pyoptions.operator.get(encodeflag)(str(_) + pyoptions.CRLF))
        except:
            exit(pyoptions.CRLF + cool.red("[-] Some error"))
    finishprinter(finishcounter(finalstorepath), finalstorepath)
