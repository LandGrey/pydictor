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
from lib.data import CRLF, minimum_length, maximum_length, default_sex, get_result_store_path, \
    get_conf_path, tool_fun_str
from lib.fun import lengthchecker, Colored

cool = Colored()


def parse_args():
    parser = argparse.ArgumentParser(prog='pydictor',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description=cool.green('*[+] A Useful Hacker Dictionary  Builder. [+]*') + CRLF +
                                                 cool.green(' [+] Build by LandGrey    email:LandGrey@qq.com') + CRLF,
                                     usage=cool.blue('''
pydictor.py [options]
               -base     type
               -char     customchar
               -chunk    <chunk1> <chunk2> ...
               -plug     <pid6, pid8, extend>
               -o        output_path
               -tool     [tool_name] <arguments ...>
               --sex     <m, f, all>
               --len     minlen maxlen
               --head    prefix_string
               --tail    suffix_string
               --encode  <b64,md5,md516,sha1,url,sha256,sha512>
               --conf    configuration_file_path
               --sedb'''))

    parser.add_argument('-base', dest='type', choices=['d', 'L', 'c', 'dL', 'dc', 'Lc', 'dLc'], metavar='Type',
                        default='', help=cool.yellow('''
Choose from  (d, L, c, dL, dc, Lc, dLc)
    d     digital             [0 - 9]
    L     lowercase letters   [a - z]
    c     capital letters     [A - Z]
    dL    Mix d and L         [0-9 a-z]
    dc    Mix d and c         [0-9 A-Z]
    Lc    Mix L and c         [a-z A-Z]
    dLc   Mix d, L and c      [0-9 a-z A-Z]'''))

    parser.add_argument('-char', dest='customchar', metavar='Character', default='',
                        help=cool.yellow('Use   [Custom Character]  build the dictionary'))

    parser.add_argument('-chunk', dest='chunk', metavar='Chunk', nargs='+', type=str, default='',
                        help=cool.yellow('Use the string [Chunk Multiplication] build the dictionary'))

    parser.add_argument('-plug', dest='plugins', metavar='Plug', nargs='+', type=str, default='',
                        help=cool.yellow('''
Choose from  (pid6, pid8, extend)
    pid6   [Id Card post 6 number]     default sex:%s
    pid8   [Id Card post 8 number]     default sex:%s
    extend [file_path]''' % (default_sex, default_sex)))

    parser.add_argument('-o', dest='output', metavar='Output', type=str, default='',
                        help=cool.yellow('''
Set the directory output path
    default: %s''' % get_result_store_path()))

    parser.add_argument('-tool', dest='tool', metavar='Tool', nargs='+', type=str, default='',
                        help=cool.yellow('''
Choose from  ({0}, {1})
    {0:4} [file_path_or_dir]
    {1:4} [file_path]'''.format(tool_fun_str[0], tool_fun_str[1])))

    parser.add_argument('--sex', dest='sex', choices=['m', 'f', 'all'],
                        metavar='Sex', type=str, default=default_sex,
                        help=cool.yellow('''
Choose from  (m, f, all)
    m: Male        f: Female   all: Male and Female
    Provided for   [pid6 | pid8]'''))

    parser.add_argument('--len', dest='len', metavar=('Minlen', 'Maxlen'), nargs=2, type=int,
                        default=(minimum_length, maximum_length), help=cool.yellow('''
[Minimun_Length]  [Maximun_Length]
                    Default: min=%s  max=%s''' % (minimum_length, maximum_length)))

    parser.add_argument('--head', dest='head', metavar='Prefix', type=str, default='',
                        help=cool.yellow('Add string head for the items'))

    parser.add_argument('--tail', dest='tail', metavar='Suffix', type=str, default='',
                        help=cool.yellow('Add string tail for the items'))

    parser.add_argument('--encode', dest='encode', metavar='Encode', default='',
                        choices=['b64', 'md5', 'md516', 'sha1', 'url', 'sha256', 'sha512'],
                        help=cool.yellow('''
    b64     base64 encode
    md5     md5 encryption (32)
    md516   md5 encryption (16)
    sha1    sha1 encryption
    url     urlencode
    sha256  sha256 encrytion
    sha512  sha512 encrytion'''))

    parser.add_argument('--conf', dest='conf', nargs='?', metavar='Conf_file_path', default='default', const='const',
                        help=cool.yellow('''
Use the configuration file build the dictionary
    Default: %s''' % get_conf_path()))

    parser.add_argument('--sedb', dest='sedb', default='',  action="store_true",
                        help=cool.yellow('Enter the Social Engineering Dictionary Builder'))

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    check_args(args)
    return args


def check_args(args):
    lengthchecker(args.len[0], args.len[1])
