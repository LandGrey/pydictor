#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import sys
import argparse
from lib.fun.fun import lengthchecker, cool
from lib.data.data import paths, pystrs,  pyoptions


def parse_args():
    parser = argparse.ArgumentParser(prog='pydictor',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description=cool.green('*[+] A Useful Hacker Dictionary  Builder. [+]*') +
                                                 pyoptions.CRLF +
                                                 cool.green(' [+] Build by LandGrey    email:LandGrey@qq.com') +
                                                 pyoptions.CRLF,
                                     usage=cool.orange('''
pydictor.py [options]
           -base     [type]
           -char     [custom_char]
           -chunk    [chunk1] [chunk2] ...
           -extend   [str_or_file]
           -plug     [{plug0},{plug1},{plug2}]
           --conf    [config_file]
           --sedb
           -o        [output_path]
           -tool     [{tool0},{tool1},{tool2},{tool3},{tool4}] [args] ...
           --len     [minlen] [maxlen]
           --head    [prefix_string]
           --tail    [suffix_string]
           --encode  [{en0},{en1},{en2},{en3},{en4},{en5},{en6},{en7}]
           --level   [code]
           --leet    [code]'''.format(plug0=pystrs.plug_range[0], plug1=pystrs.plug_range[1], plug2=pystrs.plug_range[2],
                                      tool0=pystrs.tool_range[0], tool1=pystrs.tool_range[1],
                                      tool2=pystrs.tool_range[2], tool3=pystrs.tool_range[3], tool4=pystrs.tool_range[4],
                                      en0=pystrs.encode_range[0], en1=pystrs.encode_range[1], en2=pystrs.encode_range[2],
                                      en3=pystrs.encode_range[3], en4=pystrs.encode_range[4], en5=pystrs.encode_range[5],
                                      en6=pystrs.encode_range[6], en7=pystrs.encode_range[7]))
)

    parser.add_argument('-base', dest='base', choices=[pystrs.base_dic_type[0], pystrs.base_dic_type[1],
                                                       pystrs.base_dic_type[2], pystrs.base_dic_type[3],
                                                       pystrs.base_dic_type[4], pystrs.base_dic_type[5],
                                                       pystrs.base_dic_type[6]], metavar='Type',
                        default='', help=cool.yellow('''
Choose from  ({0}, {1}, {2}, {3}, {4}, {5}, {6})
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

    parser.add_argument('-chunk', dest='chunk', metavar='chunk', nargs='+', type=str, default='',
                        help=cool.yellow('Use the multi-chunk build the dictionary'))

    parser.add_argument('-extend', dest='extend', metavar='target', nargs='+', type=str, default='',
                        help=cool.yellow('Extend the string list or file'))

    parser.add_argument('-plug', dest='plug', metavar='plug', nargs='+', type=str, default='',
                        help=cool.yellow('''
Choose from    ({0}, {1}, {2}, {3})
    {0:10} [idcard_last_6_digit]   default sex:{3}
    {1:10} [idcard_last_8_digit]   default sex:{3}
    {2:10} [url_or_file_path]'''.format(pystrs.plug_range[0], pystrs.plug_range[1], pystrs.plug_range[2], pystrs.default_sex)))

    parser.add_argument('--conf', dest='conf', nargs='?', metavar='file_path', default='default', const='const',
                        help=cool.yellow('''
Use the configuration file build the dictionary
    Default: %s''' % paths.buildconf_path))

    parser.add_argument('--sedb', dest='sedb', default='',  action="store_true",
                        help=cool.yellow('Enter the Social Engineering Dictionary Builder'))

    parser.add_argument('-o', dest='output', metavar='output', type=str, default=paths.results_path,
                        help=cool.yellow('''
Set the output directory path
    default: %s''' % paths.results_path))

    parser.add_argument('-tool', dest='tool', metavar='name', nargs='+', type=str, default='',
                        help=cool.yellow('''
Choose from    ({0}, {1}, {2},
                {3}, {4})
    {0:10} [file_or_dir]
    {1:10} [file_path]
    {2:10} ['{5}','{6}','{7}'] [file_path] [view_num]
    {3:10} [dir]
    {4:10} [dir]'''.format(pystrs.tool_range[0], pystrs.tool_range[1], pystrs.tool_range[2], pystrs.tool_range[3],
                           pystrs.tool_range[4], pystrs.just_view_counter, pystrs.just_save_counter,
                           pystrs.save_and_view)))

    parser.add_argument('--len', dest='len', metavar=('minlen', 'maxlen'), nargs=2, type=int,
                        default=(pyoptions.minlen, pyoptions.maxlen), help=cool.yellow('''
[Minimun_Length]  [Maximun_Length]
    Default: min=%s  max=%s''' % (pyoptions.minlen, pyoptions.maxlen)))

    parser.add_argument('--head', dest='head', metavar='prefix', type=str, default='',
                        help=cool.yellow('Add string head for the items'))

    parser.add_argument('--tail', dest='tail', metavar='suffix', type=str, default='',
                        help=cool.yellow('Add string tail for the items'))

    parser.add_argument('--encode', dest='encode', metavar='encode', default='none',
                        choices=[pystrs.encode_range[0], pystrs.encode_range[1], pystrs.encode_range[2],
                                 pystrs.encode_range[3], pystrs.encode_range[4], pystrs.encode_range[5],
                                 pystrs.encode_range[6], pystrs.encode_range[7]],
                        help=cool.yellow('''
From (%s, %s, %s, %s, %s, %s, %s, %s)''' % (pystrs.encode_range[0], pystrs.encode_range[1], pystrs.encode_range[2],
                                            pystrs.encode_range[3], pystrs.encode_range[4], pystrs.encode_range[5],
                                            pystrs.encode_range[6], pystrs.encode_range[7])))

    parser.add_argument('--level', dest='level', metavar='code', default=pyoptions.level, type=int,
                        help=cool.yellow('''Use code [1-5] to filter results, default: {0}'''.format(pyoptions.level)))

    parser.add_argument('--leet', dest='leet', metavar='code', nargs='+', type=int, default=pyoptions.leetmode_code,
                        help=cool.yellow('Choose leet mode code (0, 1, 2, 11-19, 21-29)'))

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    check_args(args)
    return args


def check_args(args):
    lengthchecker(args.len[0], args.len[1])
