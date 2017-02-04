#!/usr/bin/env python
# coding:utf-8
# Parse command line arguments
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
import sys
import argparse
from lib.data import CRLF, prefix_range, minimum_length, maximum_length, default_sex, get_result_store_path, \
    get_conf_path
from lib.fun import lengthchecker


def parse_args():
    parser = argparse.ArgumentParser(prog='pydictor',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description='*[+] A Useful Hacker Dictionary  Builder. [+]*' + CRLF +
                                                 ' [+] Build by LandGrey    email:LandGrey@qq.com' + CRLF,
                                     usage='''
pydictor.py [options]
               -base     type
               -char     customchar
               -chunk    <chunk1> <chunk2> ...
               -plug     <pid6, pid8, extend>
               -o        output path
               --sex     <m, f, all>
               --len     minlen maxlen
               --head    prefix string
               --tail    suffix string
               --encode  <b64,md5,md516,sha1,url,sha256,sha512>
               --conf    configuration file path
               --sedb
               --shred   <prefix | file path | directory path>''')

    parser.add_argument('-base', dest='type', choices=['d', 'L', 'c', 'dL', 'dc', 'Lc', 'dLc'], metavar='Type',
                        default='', help='''
Choose from  [d L c dL dc Lc dLc]
d     digital             [0 - 9]
L     lowercase letters   [a - z]
c     capital letters     [A - Z]
dL    Mix d and L         [0-9 a-z]
dc    Mix d and c         [0-9 A-Z]
Lc    Mix L and c         [a-z A-Z]
dLc   Mix d, L and c      [0-9 a-z A-Z]''')

    parser.add_argument('-char', dest='customchar', metavar='Character', default='',
                        help='Use   [Custom Character]  build the dictionary')

    parser.add_argument('-chunk', dest='chunk', metavar='Chunk', nargs='+', type=str, default='',
                        help='Use the string [Chunk Multiplication] build the dictionary')

    parser.add_argument('-plug', dest='plugins', metavar='Plug', nargs='+', type=str, default='',
                        help='''
Choose plug from  [pid6 pid8 extend]
    pid6 [Id Card post 6 number]     default sex:%s
    pid8 [Id Card post 8 number]     default sex:%s
    extend [file path]''' % (default_sex, default_sex))

    parser.add_argument('-o', dest='output', metavar='Output', type=str, default='',
                        help='''
Set the directory output path
    default: %s''' % get_result_store_path())

    parser.add_argument('--sex', dest='sex', choices=['m', 'f', 'all'],
                        metavar='Sex', type=str, default=default_sex,
                        help='''
Choose sex from    [m f all]
    m: Male        f: Female   all: Male and Female
    Provided for   [pid6 | pid8]''')

    parser.add_argument('--len', dest='len', metavar=('Minlen', 'Maxlen'), nargs=2, type=int,
                        default=(minimum_length, maximum_length), help='''
Minimun Length  Maximun Length (excluded head | tail | encode)
                Default: min=%s  max=%s''' % (minimum_length, maximum_length))

    parser.add_argument('--head', dest='head', metavar='Prefix', type=str, default='',
                        help='Add string head for the dictionary')

    parser.add_argument('--tail', dest='tail', metavar='Suffix', type=str, default='',
                        help='Add string tail for the dictionary')

    parser.add_argument('--encode', dest='encode', metavar='Encode', default='',
                        choices=['b64', 'md5', 'md516', 'sha1', 'url', 'sha256', 'sha512'],
                        help='''
Choose encode or encrytion from:
    b64     base64 encode
    md5     md5 encryption (32)
    md516   md5 encryption (16)
    sha1    sha1 encryption
    url     urlencode
    sha256  sha256 encrytion
    sha512  sha512 encrytion''')

    parser.add_argument('--conf', dest='conf', nargs='?', metavar='Conf file', default='default', const='const',
                        help='''
Use the configuration file build the dictionary
    Default: %s''' % get_conf_path())

    parser.add_argument('--sedb', dest='sedb', default='',  action="store_true",
                        help='Enter the Social Engineering Dictionary Builder')

    parser.add_argument('--shred', dest='clean', nargs='?', metavar='target', default='default', const='const',
                        help='''
Safe shredded the [target]:
                            [!!! Warning !!!]
    Once this function is enabled, the data will be shredded
    default              %s
    common file          specified the complete file path
    prefix file          <prefix> choice from %s types as follow:
                         [%s | %s | %s | %s | %s | %s]
    directory            specified the complete directory''' % (get_result_store_path(), str(len(prefix_range)),
                                                                prefix_range[0].lower(), prefix_range[1].lower(),
                                                                prefix_range[2].lower(), prefix_range[3].lower(),
                                                                prefix_range[4].lower(), prefix_range[5].lower()))

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    check_args(args)
    return args


def check_args(args):
    lengthchecker(args.len[0], args.len[1])
