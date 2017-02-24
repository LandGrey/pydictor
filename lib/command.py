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
from lib.fun import lengthchecker, Colored
from lib.data import CRLF, sex_range, default_sex, get_result_store_path, get_conf_path, tool_range, just_view_counter, \
    just_save_counter, save_and_view, plug_range, minimum_length, maximum_length, encode_range, base_dic_type

cool = Colored()


def parse_args():
    parser = argparse.ArgumentParser(prog='pydictor',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     description=cool.green('*[+] A Useful Hacker Dictionary  Builder. [+]*') + CRLF +
                                                 cool.green(' [+] Build by LandGrey    email:LandGrey@qq.com') + CRLF,
                                     usage=cool.orange('''
pydictor.py [options]
           -o        output_path
           -base     type
           -char     custom_char
           -chunk    <chunk1> <chunk2> ...
           -plug     [%s,%s,%s,%s]
           -tool     [%s,%s,%s,%s,%s] <arguments ...>
           --len     minlen maxlen
           --sex     [%s, %s, %s]
           --head    prefix_string
           --tail    suffix_string
           --encode  [%s,%s,%s,%s,%s,%s,%s,%s]
           --conf    config_file_path
           --sedb''' % (plug_range[0], plug_range[1], plug_range[2], plug_range[3], tool_range[0], tool_range[1],
                            tool_range[2], tool_range[3], tool_range[4], sex_range[0], sex_range[1], sex_range[2],
                            encode_range[0], encode_range[1], encode_range[2], encode_range[3], encode_range[4],
                            encode_range[5], encode_range[6], encode_range[7]))
)

    parser.add_argument('-base', dest='base', choices=[base_dic_type[0], base_dic_type[1], base_dic_type[2],
                                                       base_dic_type[3], base_dic_type[4], base_dic_type[5],
                                                       base_dic_type[6]], metavar='Type',
                        default='', help=cool.yellow('''
Choose from  ({0}, {1}, {2}, {3}, {4}, {5}, {6})
    {0}     digital             [0 - 9]
    {1}     lowercase letters   [a - z]
    {2}     capital letters     [A - Z]
    {3}    Mix {0} and {1}         [0-9 a-z]
    {4}    Mix {0} and {2}         [0-9 A-Z]
    {5}    Mix {1} and {2}         [a-z A-Z]
    {6}   Mix {0}, {1} and {3}     [0-9 a-z A-Z]'''.format(base_dic_type[0], base_dic_type[1], base_dic_type[2],
                                                            base_dic_type[3], base_dic_type[4], base_dic_type[5],
                                                            base_dic_type[6])))

    parser.add_argument('-char', dest='customchar', metavar='Character', default='',
                        help=cool.yellow('Use Custom Character build the dictionary'))

    parser.add_argument('-chunk', dest='chunk', metavar='Chunk', nargs='+', type=str, default='',
                        help=cool.yellow('Use the string [Chunk Multiplication] build the dictionary'))

    parser.add_argument('-plug', dest='plugins', metavar='Plug', nargs='+', type=str, default='',
                        help=cool.yellow('''
Choose from    ({0}, {1}, {2}, {3})
    {0:10} [id_card_post_6_number]     default sex:{4}
    {1:10} [id_card_post_8_number]     default sex:{4}
    {2:10} [file_path]
    {3:10} [url_or_file_path]'''.format(plug_range[0], plug_range[1], plug_range[2], plug_range[3], default_sex)))

    parser.add_argument('-o', dest='output', metavar='Output', type=str, default='',
                        help=cool.yellow('''
Set the directory output path
    default: %s''' % get_result_store_path()))

    parser.add_argument('-tool', dest='tool', metavar='Tool', nargs='+', type=str, default='',
                        help=cool.yellow('''
Choose from    ({0}, {1}, {2}, {3}, {4})
    {0:10} [file_or_dir]
    {1:10} [file_path]
    {2:10} ['{5}','{6}','{7}'] [file_path] [view_num]
    {3:10} [dir]
    {4:10} [dir]'''.format(tool_range[0], tool_range[1], tool_range[2], tool_range[3], tool_range[4], just_view_counter,
                           just_save_counter, save_and_view)))

    parser.add_argument('--sex', dest='sex', choices=[sex_range[0], sex_range[1], sex_range[2]],
                        metavar='Sex', type=str, default=default_sex,
                        help=cool.yellow('''
Choose from  ({0}, {1}, {2})
    {0}: Male        {1}: Female   {2}: Male and Female'''.format(sex_range[0], sex_range[1], sex_range[2])))

    parser.add_argument('--len', dest='len', metavar=('Minlen', 'Maxlen'), nargs=2, type=int,
                        default=(minimum_length, maximum_length), help=cool.yellow('''
[Minimun_Length]  [Maximun_Length]
                    Default: min=%s  max=%s''' % (minimum_length, maximum_length)))

    parser.add_argument('--head', dest='head', metavar='Prefix', type=str, default='',
                        help=cool.yellow('Add string head for the items'))

    parser.add_argument('--tail', dest='tail', metavar='Suffix', type=str, default='',
                        help=cool.yellow('Add string tail for the items'))

    parser.add_argument('--encode', dest='encode', metavar='Encode', default='none',
                        choices=[encode_range[0], encode_range[1], encode_range[2], encode_range[3], encode_range[4],
                                 encode_range[5], encode_range[6], encode_range[7]],
                        help=cool.yellow('''
Choose from [%s, %s, %s, %s, %s, %s, %s, %s]''' % (encode_range[0], encode_range[1], encode_range[2],
                                                   encode_range[3], encode_range[4], encode_range[5],
                                                   encode_range[6], encode_range[7])))

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
