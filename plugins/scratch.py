#!/usr/bin/env python
# coding:utf-8
# Referred: https://github.com/cheetz/brutescrape
# author: LandGrey
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
import re
import ssl
from lib.fun.decorator import magic
from lib.fun.osjudger import py_ver_egt_3
from lib.data.data import paths, pyoptions
from lib.fun.fun import unique, cool, walk_pure_file

try:
    # ssl._create_unverified_context is present in Python 2.7.9 and later
    ssl._create_default_https_context = ssl._create_unverified_context
except:
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    except:
        pass

# in python3: urllib + urilib2 -> urllib, and
# urllib2.urlopen() -> urllib.request.urlopen(), urllib2.Request() -> urllib.request.Request()
try:
    if py_ver_egt_3():
        from urllib.request import urlopen
    else:
        from urllib2 import urlopen
except ImportError as e:
    print(e.message)
    exit(cool.red('[-] can not import urllib or urllib2 module:') + pyoptions.CRLF)

passcratch_black_list = walk_pure_file(paths.scratch_blacklist)


def stripHTMLTags(html):
    text = html
    rules = [
        {r'>\s+': '>'},                                # Remove spaces after a tag opens or closes.
        {r'\s+': ' '},                                 # Replace consecutive spaces.
        {r'\s*<br\s*/?>\s*': '\n'},                    # Newline after a <br>.
        {r'</(div)\s*>\s*': '\n'},                     # Newline after </p> and </div> and <h1/>.
        {r'</(p|h\d)\s*>\s*': '\n\n'},                 # Newline after </p> and </div> and <h1/>.
        {r'<head>.*<\s*(/head|body)[^>]*>': ''},       # Remove <head> to </head>.
        {r'<a\s+href="([^"]+)"[^>]*>.*</a>': r'\1'},   # Show links instead of texts.
        {r'[ \t]*<[^<]*?/?>': ''},                     # Remove remaining tags.
        {r'^\s+': ''}                                  # Remove spaces at the beginning.
    ]
    for rule in rules:
        for (k, v) in rule.items():
            try:
                regex = re.compile(k)
                text = str(regex.sub(v, text))
            except:
                pass
    htmlspecial = {
        '&nbsp;': ' ', '&amp;': '&', '&quot;': '"',
        '&lt;': '<', '&gt;': '>'
    }
    for (k, v) in htmlspecial.items():
        text = text.replace(k, v)
    return text


def scratchword(siteList):
    resluts = []
    # Create an empty list for generation logic.
    y_arr = []
    for site in siteList:
        try:
            site = site.strip()
            response = urlopen(site)
            response.addheaders = \
                [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0')]
            # if you don't decode('utf-8'), it will don't work both in python2 and python3
            try:
                x = stripHTMLTags(response.read().decode('utf-8') + site)
            except:
                try:
                    x = stripHTMLTags(response.read().decode('GBK') + site)
                except:
                    exit(cool.red("[-] Page coding parse error, please use 'extend' plug instead") + pyoptions.CRLF)

            # Replace junk found in our response
            x = x.replace('\n', ' ')
            x = x.replace(',', ' ')
            x = x.replace('.', ' ')
            x = x.replace('/', ' ')
            x = re.sub('[^A-Za-z0-9]+', ' ', x)
            x_arr = x.split(' ')
            for y in x_arr:
                y = y.strip()
                if y and (len(y) >= 5):
                    if ((y[0] == '2') and (y[1] == 'F')) \
                            or ((y[0] == '2') and (y[1] == '3')) \
                            or ((y[0] == '3') and (y[1] == 'F')) or ((y[0] == '3') and (y[1] == 'D')):
                        y = y[2:]
                    if len(y) <= 8 and True if y.lower() not in passcratch_black_list and len(y) >= 5 else False:
                        y_arr.append(y)
                    elif 9 <= len(y) <= 25 and True if y.lower() not in passcratch_black_list else False:
                        y_arr.append(y)
        except Exception:
            exit(cool.red("[-] Process abort, please check url and try use 'extend' function instead") + pyoptions.CRLF)

    for yy in unique(y_arr):
        if yy.strip().isdigit():
            pass
        else:
            if not re.findall(pyoptions.scratch_filter, yy.strip(), flags=re.I):
                resluts.append(yy.strip())
    return unique(resluts)


def checkurl(urlike):
    try:
        if not str(urlike).startswith('http'):
            return 'http://' + urlike.strip()
        else:
            return urlike
    except:
        exit(cool.red("[-] Incorrect url/uri: {0}".format(cool.red(urlike.strip()))))


def scratch_magic(*args):
    """[url_or_file]"""
    args = list(args[0])

    if len(args) == 1:
        target = paths.scrapersites_path
    elif len(args) == 2:
        target = args[1]
    else:
        exit(pyoptions.CRLF + cool.fuchsia("[!] Usage: {} {}".format(args[0], pyoptions.plugins_info.get(args[0]))))

    sites = []
    if os.path.isfile(target):
        with open(target, 'r') as f:
            for _ in f.readlines():
                if _.startswith(pyoptions.annotator):
                    pass
                else:
                    sites.append(checkurl(_))
    else:
        sites.append(checkurl(target))
    rawlist = scratchword(sites)

    @magic
    def scratch():
        return rawlist
