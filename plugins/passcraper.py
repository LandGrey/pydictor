#!/usr/bin/env python
# coding:utf-8
# A web pass scraper for generating password based on plain text found using 'extend' plug
# Referred: https://github.com/cheetz/brutescrape
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals
import os
import re
import traceback
from collections import OrderedDict
from lib.fun import cool
from lib.fun import py_ver_egt_3
from plugins.extend import get_extend_dic
from lib.data import scrabble_site_path, passcratch_white_list, CRLF, annotator


# in python3: urllib + urilib2 -> urllib, and
# urllib2.urlopen() -> urllib.request.urlopen(), urllib2.Request() -> urllib.request.Request()
try:
    if py_ver_egt_3():
        from urllib.request import urlopen
    else:
        from urllib2 import urlopen
except ImportError:
    print(cool.red('[-] can not import urllib or urllib2 module:') + CRLF)
    exit(traceback.print_exc())


def stripHTMLTags(html):
    text = html
    rules = [
        {r'>\s+': '>'},                                # Remove spaces after a tag opens or closes.
        {r'\s+': ' '},                                 # Replace consecutive spaces.
        {r'\s*<br\s*/?>\s*': '\n'},                    # Newline after a <br>.
        {r'</(div)\s*>\s*': '\n'},                     # Newline after </p> and </div> and <h1/>.
        {r'</(p|h\d)\s*>\s*': '\n\n'},                 # Newline after </p> and </div> and <h1/>.
        {r'<head>.*<\s*(/head|body)[^>]*>': ''},       # Remove <head> to </head>.
        {r'<a\s+href="([^"]+)"[^>]*>.*</a>': r'\1'},    # Show links instead of texts.
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
    special = {
        '&nbsp;': ' ', '&amp;': '&', '&quot;': '"',
        '&lt;': '<', '&gt;': '>'
    }
    for (k, v) in special.items():
        text = text.replace(k, v)
    return text


def scratchword(siteList):
    scrabbler = "scrabbler"
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
            x = stripHTMLTags(response.read().decode('utf-8') + site)
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
                    if ((y[0] == '2') and (y[1] == 'F')) or ((y[0] == '2') and (y[1] == '3')) or ((y[0] == '3') and (y[1] == 'F')) or ((y[0] == '3') and (y[1] == 'D')):
                        y = y[2:]
                    if len(y) <= 8 and y.lower() not in passcratch_white_list:
                        y_arr.append(y)
                    elif 9 <= len(y) <= 25 and True if scrabbler in passcratch_white_list and y not in scrabbler else False:
                        y_arr.append(y)
        except Exception:
            print(CRLF + cool.red("[-] Process abort, please check url and looking error info: ") + CRLF)
            traceback.print_exc()
            exit(CRLF)
    y_arr_unique = OrderedDict.fromkeys(y_arr).keys()
    for yy in y_arr_unique:
        if yy.strip().isdigit():
            pass
        else:
            resluts.append(yy.strip())
    return resluts


def checkurl(urlike):
    try:
        if not str(urlike).startswith('http'):
            return 'http://' + urlike.split('/')[0]
        else:
            return urlike
    except:
        exit("[-] Incorrect url/uri: {0}".format(cool.red(urlike)))


def get_passcratch_dic(target=scrabble_site_path, encodeflag='none'):
    sites = []
    if os.path.isfile(target):
        with open(target, 'r') as f:
            for _ in f.readlines():
                if _.startswith(annotator):
                    pass
                else:
                    sites.append(checkurl(_))
    else:
        sites.append(checkurl(target))
    get_extend_dic(scratchword(sites), encodeflag=encodeflag, need_passcratch=True)
