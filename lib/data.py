#!/usr/bin/env python
# coding:utf-8
# store some common public variable and structs
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

import os
import sys
import time
from lib.encode import *

# global CRLF
CRLF = "\n"

# filename extension
filextension = ".txt"

# default length
minimum_length = 2
maximum_length = 4

# allowed maximum length
maxlen_switcher = 11

# allowed maximum generated items
count_switcher = 100000000

# shredded file rewrite counts
file_rewrite_count = 1

# shredded dir rewrite counts
dir_rewrite_count = 1

# project root path
root_path = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])))

# default configuration file path
conf_path = os.path.join(root_path, "build.conf")

# default results store directory
result_store_path = os.path.join(root_path, "results")


# get the current format the time of build the dictionary
def get_buildtime():
    return str(time.strftime("%Y%m%d_%H.%M.%S", time.localtime(time.time())))

# default sex(range <m, f, all>)
default_sex = "all"

# encode operator
operator = {'b64': base64_encode, 'md5': md5_encode, 'md516': md5_16_encode, 'sha1': sha1_encode,
            'url': url_encode, 'sha256': sha256_encode, 'sha512': sha512_encode}

# directionary type prefix
BASE_prefix = "BASE"
CHUNK_prefix = "CHUNK"
CONF_prefix = "CONF"
SEDB_prefix = "SEDB"
IDCARD_prefix = "IDCARD"
EXTEND_prefix = "EXTEND"
prefix_range = [BASE_prefix, CHUNK_prefix, CONF_prefix, SEDB_prefix, IDCARD_prefix, EXTEND_prefix]

# configuration file element description
head = "head"
char = "char"
minlen = "minlen"
maxlen = "maxlen"
encode = "encode"
tail = "tail"

# configuration dicts
dicts = {head: [], char: [], minlen: [], maxlen: [], encode: [], tail: []}

# configuration file split char
chars_split = ","
char_range_split = "-"
length_split = ":"

# no encode flag in configuration file
no_encode_flag = "none"

# configuration file  annotator
conf_annotator = '#'


# share and access the globle path variable
def get_result_store_path():
    global result_store_path
    return result_store_path


def set_result_store_path(new_result_path):
    global result_store_path
    result_store_path = new_result_path


def get_conf_path():
    global conf_path
    return conf_path


def set_conf_path(new_conf_path):
    global conf_path
    conf_path = new_conf_path
