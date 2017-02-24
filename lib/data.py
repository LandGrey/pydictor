#!/usr/bin/env python
# coding:utf-8
# Store some common public variable, data structs and simple function
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import os
import sys
import time
from lib.encode import *

# start time
startime = time.time()

# project root path
root_path = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])))


# ---------------------------------- you can modify it ----------------------------------

# output file prefix
BASE_prefix = "BASE"
CHAR_prefix = "CHAR"
CHUNK_prefix = "CHUNK"
CONF_prefix = "CONF"
SEDB_prefix = "SEDB"
IDCARD_prefix = "IDCARD"
EXTEND_prefix = "EXTEND"
PASSCRAPER_prefix = "PASSCRAPER"
UNIQIFER_prefix = "UNIQIFER"
COUNTER_prefix = "COUNTER"
COMBINER_prefix = "COMBINER"
UNIQBINER_prefix = "UNIQBINER"

# default length
minimum_length = 2
maximum_length = 4

# filename extension
filextension = ".txt"

# allowed maximum length
maxlen_switcher = 11

# allowed maximum generated items
count_switcher = 100000000

# shredded file rewrite counts
file_rewrite_count = 1

# shredded dir rewrite counts
dir_rewrite_count = 1

# view the 'counter' tool counts
view_counter_switcher = 100

# counter tool split word
counter_split = "\n"

# default configuration file path
conf_path = os.path.join(root_path, "build.conf")

# default scrabble site file path
scrabble_site_path = os.path.join(root_path, 'scraper.site')

# default results store directory
result_store_path = os.path.join(root_path, "results")

# extend_enter replace string, k:v -> before:after
extend_replace = {"s": "5", "S": "5", "l": "1", "1": "l", "o": "0",
                  "0": "o", "p": "P", "i": "1", "q": "9"}

# passcratch plug useless string white list(lowercase), string length >= 5 will work, but don not add too much string
passcratch_white_list = (
    "a1ert", "about", "academic", "action", "actions", "alerts", "align", "alphanum", "analyze", "android",
    "apache", "application", "archives", "author", "baidu", "banner", "before", "bigger", "blank", "board",
    "bootcss", "border", "bottle", "bottom", "build", "button", "calendar", "center", "change", "changing",
    "charset", "china", "chinese", "chrome", "class", "classroom", "clear", "click", "color", "colored",
    "colorful", "coming", "complete", "contain", "content", "context", "cookie", "copyright", "correct", "count",
    "crete", "database", "datetime", "default", "describe", "description", "device", "digital", "disp1ay", "django",
    "doctype", "document", "dotted", "download", "eclipse", "element", "email", "english", "equiv", "error", "event",
    "every", "expand", "expanded", "export", "extend_enter", "extended", "failed", "favicon", "firefox", "focus",
    "footer", "format", "friend", "friendly", "friends", "function", "github", "handheld", "handle", "header", "hello",
    "house", "https", "image", "images", "import", "index", "initial", "input", "insert", "jquery", "keyword",
    "keywords", "large", "length", "letter", "links", "linux", "listen", "listening", "lookup", "margin", "maximum",
    "media", "method", "minimum", "mssql", "mysql", "nginx", "notice", "onmouse", "other", "output", "padded", "pages",
    "parent", "people", "powered", "press", "privacy", "public", "publish", "python", "query", "quote", "readme",
    "regex", "report", "reports", "request", "requests", "restrict", "result", "results", "right", "scale", "school",
    "script", "search", "section", "service", "services", "share", "shortcut", "shtml", "sizes", "static", "status",
    "strict", "string", "style", "styles", "stylesheet", "submit", "success", "suggestion", "table", "target",
    "template", "themes", "think", "thinking", "title", "today", "tomorrow", "topic", "upload", "uploads", "value",
    "version", "views", "website", "weibo", "weight", "welcome", "width", "windows", "windows", "without", "wordpress",
    "world", "writing", "wrong", "xhtml", "xhtml1", "xmlns",
)

# ---------------------------------- better not to  modify it ----------------------------------

# global CRLF
CRLF = "\n"

prefix_range = (BASE_prefix, CHAR_prefix, CHUNK_prefix, CONF_prefix, SEDB_prefix, IDCARD_prefix, EXTEND_prefix,
                UNIQIFER_prefix, COUNTER_prefix, COMBINER_prefix, UNIQBINER_prefix, PASSCRAPER_prefix)

# default counter view items
default_view_items = 10

# configuration file split char
chars_split = ","
char_range_split = "-"
length_split = ":"

# configuration file and scratch site file annotator
annotator = '#'

# ---------------------------------- don not modify it ----------------------------------
build_in_dict_path = os.path.join(root_path, "build-in dict")

# configuration file element description
head = "head"
char = "char"
minlen = "minlen"
maxlen = "maxlen"
encode = "encode"
tail = "tail"

# configuration dicts
dicts = {head: [], char: [], minlen: [], maxlen: [], encode: [], tail: []}

# default sex(range <m, f, all>)
sex_range = ("m", "f", "all")
default_sex = sex_range[2]

# base dict type flag
base_dic_type = ("d", "L", "c", "dL", "dc", "Lc", "dLc")

# counter command string
just_view_counter = "v"
just_save_counter = "s"
save_and_view = "vs"
counter_cmd_range = (just_save_counter, just_view_counter, save_and_view)

# tool's function string
tool_range = ("shredder", "uniqifer", "counter", 'combiner', 'uniqbiner')

# plug's function string
plug_range = ("pid6", "pid8", "extend", "passcraper")

# encode function string
encode_range = ("none", "b64", "md5", "md516", "sha1", "url", "sha256", "sha512")

# encode operator
operator = {'none': none_encode, 'b64': base64_encode, 'md5': md5_encode, 'md516': md5_16_encode, 'sha1': sha1_encode,
            'url': url_encode, 'sha256': sha256_encode, 'sha512': sha512_encode}

# social engineering dictionary elements
sedb_range = ("cname", "ename", "sname", "birth", "usedpwd",
              "phone", "uphone", "hphone", "email", "postcode",
              "nickname", "idcard", "jobnum", "otherdate", "usedchar")


# get the current format the time of build the dictionary
def get_buildtime():
    return str(time.strftime("%Y%m%d_%H.%M.%S", time.localtime(time.time())))


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

