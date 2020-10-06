#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import sys
import argparse
from lib.fun.fun import lengthchecker, cool
from lib.data.data import paths, pystrs, pyoptions


def parse_args():
    parser = argparse.ArgumentParser(prog='pydictor',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description=cool.green('*[+] A Useful Hacker Dictionary  Builder. [+]*') +
                                                 pyoptions.CRLF +
                                                 cool.green(' [+] Build by LandGrey    email:LandGrey@qq.com') +
                                                 pyoptions.CRLF,
                                     usage=cool.orange('''
pydictor.py [options]
           -base        [type]
           -char        [custom_char]
           -chunk       [chunk1] [chunk2] ...
           -extend      [string_or_file]
           -plug        [{plugin}]
           --conf       [expression_or_file]
           --pattern    [expression_or_file]
           --sedb
           -o,--output  [directory]
           -tool        [{tool}]
           --len        [minlen] [maxlen]
           --head       [prefix_string]
           --tail       [suffix_string]
           --encode     [{encode}]
           --occur      [letter] [digital] [special]
           --types      [letter] [digital] [special]
           --repeat     [letter] [digital] [special]
           --regex      [regex]
           --level      [code]
           --leet       [code]
           --dmy'''.format(plugin=",".join(pyoptions.plug_range), encode=",".join(pyoptions.encode_range),
                                         tool=",".join(pyoptions.tool_range))))

    parser.add_argument('-base', dest='base', choices=[pystrs.base_dic_type[0], pystrs.base_dic_type[1],
                                                       pystrs.base_dic_type[2], pystrs.base_dic_type[3],
                                                       pystrs.base_dic_type[4], pystrs.base_dic_type[5],
                                                       pystrs.base_dic_type[6]], metavar='Type',
                        default='', help=cool.yellow('''Choose from  ({0}, {1}, {2}, {3}, {4}, {5}, {6})
    {0}     digital             [0 - 9]
    {1}     lowercase letters   [a - z]
    {2}     capital letters     [A - Z]
    {3}    Mix {0} and {1}         [0-9 a-z]
    {4}    Mix {0} and {2}         [0-9 A-Z]
    {5}    Mix {1} and {2}         [a-z A-Z]
    {6}   Mix {0}, {1} and {3}     [0-9 a-z A-Z]'''.format(pystrs.base_dic_type[0], pystrs.base_dic_type[1],
                                                           pystrs.base_dic_type[2], pystrs.base_dic_type[3],
                                                           pystrs.base_dic_type[4], pystrs.base_dic_type[5],
                                                           pystrs.base_dic_type[6])))

    parser.add_argument('-char', dest='char', metavar='character', default='',
                        help=cool.yellow('Use Custom Character build the dictionary'))

    parser.add_argument('-chunk', dest='chunk', metavar='arg', nargs='+', type=str, default='',
                        help=cool.yellow('Use the multi-chunk build the dictionary'))

    parser.add_argument('-extend', dest='extend', metavar='arg', nargs='+', type=str, default='',
                        help=cool.yellow('Extend the string list or file'))

    parser.add_argument('-plug', dest='plug', metavar='arg', nargs='+', type=str, default='',
                        help=cool.yellow('''{plugins_desc}'''.format(plugins_desc=pyoptions.plugins_desc)))

    parser.add_argument('--conf', dest='conf', nargs='?', metavar='file_path', default='default', const='const',
                        help=cool.yellow("Use the configuration string or file build the dictionary"))

    parser.add_argument('--pattern', dest='pattern', nargs='?', metavar='file_path', default='default', const='const',
                        help=cool.yellow("Use pattern string build the dictionary"))

    parser.add_argument('--sedb', dest='sedb', default='',  action="store_true",
                        help=cool.yellow('Enter the Social Engineering Dictionary Builder'))

    parser.add_argument('-o', '--output', dest='output', metavar='path', type=str, default=paths.results_path,
                        help=cool.yellow('''Set the output directory path
    default: %s''' % paths.results_path))

    parser.add_argument('-tool', dest='tool', metavar='arg', nargs='+', type=str, default='',
                        help=cool.yellow('''{tools_desc}'''.format(tools_desc=pyoptions.tools_desc)))

    parser.add_argument('--len', dest='len', metavar=('minlen', 'maxlen'), nargs=2, type=int,
                        default=(pyoptions.minlen, pyoptions.maxlen),
                        help=cool.yellow('''Default: min=%s  max=%s''' % (pyoptions.minlen, pyoptions.maxlen)))

    parser.add_argument('--head', dest='head', metavar='prefix', type=str, default='',
                        help=cool.yellow('Add string head for the items'))

    parser.add_argument('--tail', dest='tail', metavar='suffix', type=str, default='',
                        help=cool.yellow('Add string tail for the items'))

    parser.add_argument('--encode', dest='encode', metavar='encode', default='none',
                        choices=pyoptions.encode_range,
                        help=cool.yellow('''{encode_desc}'''.format(encode_desc=pyoptions.encode_desc)))

    parser.add_argument('--occur', dest='occur', metavar=('letter', 'digital', 'special'), nargs=3, type=str,
                        default=(pyoptions.letter_occur, pyoptions.digital_occur, pyoptions.special_occur),
                        help=cool.yellow('''Default: letter "%s" digital "%s" special "%s"''' %
                                         (pyoptions.letter_occur, pyoptions.digital_occur, pyoptions.special_occur)))

    parser.add_argument('--types', dest='types', metavar=('letter', 'digital', 'special'), nargs=3, type=str,
                        default=(pyoptions.letter_types, pyoptions.digital_types, pyoptions.special_types),
                        help=cool.yellow('''Default: letter "%s"  digital "%s"  special "%s"''' %
                                         (pyoptions.letter_types, pyoptions.digital_types, pyoptions.special_types)))

    parser.add_argument('--repeat', dest='repeat', metavar=('letter', 'digital', 'special'), nargs=3, type=str,
                        default=(pyoptions.letter_repeat, pyoptions.digital_repeat, pyoptions.special_repeat),
                        help=cool.yellow('''Default: letter "%s"  digital "%s"  special "%s"''' %
                                         (pyoptions.letter_repeat, pyoptions.digital_repeat, pyoptions.special_repeat)))

    parser.add_argument('--regex', dest='regex', metavar='regex', type=str,
                        default=pyoptions.filter_regex, help=cool.yellow('''Filter by regex, Default: (%s)''' %
                                                                         pyoptions.filter_regex))

    parser.add_argument('--level', dest='level', metavar='code', default=pyoptions.level, type=int,
                        help=cool.yellow('''Use code [1-5] to filter results, default: {0}'''.format(pyoptions.level)))

    parser.add_argument('--leet', dest='leet', metavar='code', nargs='+', type=int, default=pyoptions.leetmode_code,
                        help=cool.yellow('Choose leet mode code (0, 1, 2, 11-19, 21-29)'))

    parser.add_argument('--more', dest='more', default='',  action="store_true",
                        help=cool.yellow('Append more simple word list to extend function results, default: false'))

    parser.add_argument('--dmy', dest='dmy', default='',  action="store_true",
                        help=cool.yellow('Use ddMMyyyy format date, default date format: yyyyMMdd'))

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    check_args(args)
    return args


def check_args(args):
    lengthchecker(args.len[0], args.len[1])
