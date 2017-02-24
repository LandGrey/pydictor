#!/usr/bin/env python
# coding:utf-8
# pydictor dictionary-handler tool: shredder
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""


from __future__ import unicode_literals
import os
import stat
import string
import random
import shutil
import traceback
from lib.fun import range_compatible, cool
from lib.data import CRLF, dir_rewrite_count, file_rewrite_count, get_result_store_path,  prefix_range


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
            with open(filepath, "w"):
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
    print(cool.orange("[+] Completely!"))


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


def shredder_enter(*args):
    fnum = 0
    _ = "".join(args)
    if _ and os.path.isdir(_):
        shreder_dir(_)
    elif _ and os.path.isfile(_):
        shreder_file(_)
    elif _ and _.upper() in prefix_range:
        for filename in os.listdir(get_result_store_path()):
            if _.upper() in str(filename[0:10]).upper():
                fnum += 1
                shreder_file(os.path.join(get_result_store_path(), filename))
        if fnum == 0:
            exit(CRLF + cool.orange("[+] prefix %s files has been clean" % _.upper()))
    else:
        exit(CRLF + cool.red("[-] invalid shredder path_or_dir arguments"))
