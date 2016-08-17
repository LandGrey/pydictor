#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-08-17
#
# Parse command line arguments
#

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(prog='pydictor',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description='*[+] A useful hacker dictionary  builder. [+]*\n'
                                                 ' [+] Build by LandGrey\n',
                                     usage='pydictor.py [-t type] [-cc customchar] '
                                           '[-cm <str1> <str2> ...] [--len minlen maxlen] '
                                           '[--head  Prefix] [--tail Suffix] '
                                           '[--encode <b64,md5,sha1,url,sha256,sha512>]')

    parser.add_argument('-t', dest='type',choices=['d', 'L', 'c', 'dL', 'dc', 'Lc', 'dLc'],metavar='Type',default='',
                        help='Choose from  [d L c dL dc Lc dLc]'
                              '\nd     digital             [0 - 9]'
                              '\nL     lowercase letters   [a - z]'
                              '\nc     capital letters     [A - Z]'
                              '\ndL    Mix d and L         [0-9 a-z]'
                              '\ndc    Mix d and c         [0-9 A-Z]'
                              '\nLc    Mix L and c         [a-z A-Z]'
                              '\ndLc   Mix d, L and c      [0-9 a-z A-Z]')

    parser.add_argument('-cc', dest='customchar', metavar='Character', default='',
                        help='Use [Custom Character] build the dictionary')

    parser.add_argument('-cm', dest='chunk', metavar='Str', nargs='+', type=str, default='',
                        help='Use the string [Chunk Multiplication] build the dictionary')

    parser.add_argument('--len', dest='len', metavar=('Minlen','Maxlen'), nargs=2, type=int, default=(1, 4),
                        help='Minimun Length   Maximun Length (except head tail encode)\nDefault: min=1    max=4')

    parser.add_argument('--head', dest='head', metavar='Prefix', type=str, default='',
                        help='Add string head for the dictionary')

    parser.add_argument('--tail', dest='tail', metavar='Suffix', type=str, default='',
                        help='Add string tail for the dictionary')

    parser.add_argument('--encode', dest='encode', metavar='Encode', default='',
                        choices=['b64', 'md5', 'sha1', 'url', 'sha256', 'sha512'],
                        help='Choose the form of encrytion'
                             '\nb64     base64 encode'
                             '\nmd5     md5 encryption'
                             '\nsha1    sha1 encryption'
                             '\nurl     urlencode'
                             '\nsha256  sha256 encrytion'
                             '\nsha512  sha512 encrytion')

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    check_args(args)
    return args


def check_args(args):
    if args.len[0] > args.len[1]:
        print '\n[+]Pydictor   Build by LandGrey [+]\nMinimum length <= Maximum length'
        sys.exit()
    if len(args.chunk) > 11:
        print '\n[+]Pydictor   Build by LandGrey [+]\nSorry, too much string chunks and space may be insufficient'
        sys.exit()

