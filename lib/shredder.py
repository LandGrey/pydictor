#!/usr/bin/env python
# coding:utf-8
# function: shredding single file or directory
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import stat
import random
import shutil
import string
import traceback
from lib.data import CRLF, dir_rewrite_count, file_rewrite_count
from lib.fun import range_compatible, cool


def rewrite(filepath):
    try:
        filesize = os.path.getsize(filepath)
        with open(filepath, "w+b") as f:
            f.write("".join(chr(random.randint(0, 255)) for _ in range_compatible(0, filesize)))
    except:
        pass


def truncating(filepath):
    # default: 2 times
    for _ in range_compatible(0, 2):
        try:
            with open(filepath, 'w') as f:
                pass
        except:
            pass


def renamefile(filepath):
    newname = os.path.join(os.path.dirname(filepath), "".join(random.sample(string.ascii_letters, random.randint(4, 8))))
    try:
        os.rename(filepath, newname)
    except:
        pass
    return newname


def renamedir(dirpaths):
    # equals python 2 version: dirpaths.sort(cmp=lambda x, y: y.count(os.path.sep) - x.count(os.path.sep))
    dirpaths.sort()
    for dirpath in dirpaths:
        try:
            os.rename(dirpath, os.path.join(os.path.dirname(dirpath), "".join(random.sample(string.ascii_letters, random.randint(4, 8)))))
        except:
            pass


def shreder_dir(directory, rewritecounts=dir_rewrite_count):
    filepaths = []
    dirpaths = []
    print(CRLF + "[+] Shredding '%s' ..." % cool.orange(directory))
    try:
        newdirectoryname = os.path.join(os.path.dirname(directory), "".join(chr(random.randint(97, 122))
                                                                            for _ in range_compatible(1, 6)))
        os.rename(directory, newdirectoryname)
        directory = newdirectoryname
    except:
        traceback.print_exc()
        exit(CRLF + cool.red("[-] Error: cannot rename root directory name, Please check permissions"))

    for rootpath, subdirsname, filenames in os.walk(directory):
        # get all directories
        dirpaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in subdirsname])
        # get all absolute file path
        filepaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in filenames])

    for filepath in filepaths:
        try:
            os.chmod(filepath, stat.S_IREAD | stat.S_IWRITE)
        except:
            pass

    for _ in range_compatible(0, rewritecounts):
        print("[+] Rewrite count: %d" % (_+1))
        for filepath in filepaths:
            rewrite(filepath)
    for filepath in filepaths:
        truncating(filepath)
    for filepath in filepaths:
        renamefile(filepath)
    renamedir(dirpaths)
    os.chdir(os.path.join(directory, ".."))
    try:
        shutil.rmtree(directory)
    except OSError as ex:
        print(cool.fuchsia("[!] Error: Cannot removing directory: '%s' " % directory))
        traceback.print_exc()
    print(cool.orange("[+] Completely!") + CRLF)


def shreder_file(filepath, rewritecounts=file_rewrite_count):
    try:
        os.chmod(filepath, stat.S_IREAD | stat.S_IWRITE)
    except:
        pass
    for _ in range_compatible(0, rewritecounts):
        rewrite(filepath)
    truncating(filepath)
    newname = renamefile(filepath)
    os.remove(newname)
    print("[+] Shredded %s Completely!" % cool.orange(filepath))
