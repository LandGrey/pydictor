#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2021 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

import re
import string
from lib.fun.fun import cool
from itertools import groupby
from collections import Counter
from lib.data.data import pyoptions


def lenght_filter(item, minlen=pyoptions.minlen, maxlen=pyoptions.maxlen, lenght_is_filter=False):
    if item and lenght_is_filter:
        if minlen <= len(item) <= maxlen:
            return item
    else:
        return item


def headtail_filter(item, head='', tail=''):
    if item:
        return head + item + tail
    else:
        return item


def encode_filter(item, encode='none'):
    return pyoptions.operator.get(encode)(item)


def occur_filter(item, letter_occur=pyoptions.letter_occur, digital_occur=pyoptions.digital_occur,
                 special_occur=pyoptions.special_occur, occur_is_filter=False):
    l_count = d_count = s_count = 0

    def occur():
        l_op_inner = d_op_inner = s_op_inner = '<='
        l_wantcount = d_wantcount = s_wantcount = 99
        pattern = '((<|>|=)=?)(\d*)$'
        letter_match = re.match(pattern, letter_occur)
        digital_match = re.match(pattern, digital_occur)
        special_match = re.match(pattern, special_occur)
        if letter_match and letter_match.group():
            l_op_inner = letter_match.group(1)
            l_wantcount = int(letter_match.group(len(letter_match.groups())))
        if digital_match and digital_match.group():
            d_op_inner = digital_match.group(1)
            d_wantcount = int(digital_match.group(len(digital_match.groups())))
        if special_match and special_match.group():
            s_op_inner = special_match.group(1)
            s_wantcount = int(special_match.group(len(special_match.groups())))
        pyoptions.letter_occur = l_op_inner + str(l_wantcount)
        pyoptions.digital_occur = d_op_inner + str(d_wantcount)
        pyoptions.specail_occur = s_op_inner + str(s_wantcount)
        return l_op_inner, l_wantcount, d_op_inner, d_wantcount, s_op_inner, s_wantcount

    l_op, l_wantcount, d_op, d_wantcount, s_op, s_wantcount = occur()

    if item and occur_is_filter:
        for word in item:
            if word in string.ascii_letters:
                l_count += 1
            elif word in string.digits:
                d_count += 1
            elif word in string.printable[62:-5]:
                s_count += 1
        letter_map = {'<': l_count < l_wantcount, '<=': l_count <= l_wantcount,
                      '>': l_count > l_wantcount, '>=': l_count >= l_wantcount,
                      '=': l_count == l_wantcount, '==': l_count == l_wantcount, }
        digital_map = {'<': d_count < d_wantcount, '<=': d_count <= d_wantcount,
                       '>': d_count > d_wantcount, '>=': d_count >= d_wantcount,
                       '=': d_count == d_wantcount, '==': d_count == d_wantcount, }
        special_map = {'<': s_count < s_wantcount, '<=': s_count <= s_wantcount,
                       '>': s_count > s_wantcount, '>=': s_count >= s_wantcount,
                       '=': s_count == s_wantcount, '==': s_count == s_wantcount, }
        if letter_map[l_op] and digital_map[d_op] and special_map[s_op]:
            return item
    else:
        return item


def types_filter(item, letter_types=pyoptions.letter_types, digital_types=pyoptions.digital_types,
                 special_types=pyoptions.special_types, types_is_filter=False):
    if item and types_is_filter:
        l_types = d_types = s_types = 0
        l_op = d_op = s_op = '>='
        l_wanttypes = d_wanttypes = s_wanttypes = 0
        pattern = '((<|>|=)=?)(\d*)$'
        letter_match = re.match(pattern, letter_types)
        digital_match = re.match(pattern, digital_types)
        special_match = re.match(pattern, special_types)
        if letter_match and letter_match.group():
            l_op = letter_match.group(1)
            l_wanttypes = int(letter_match.group(len(letter_match.groups())))
        if digital_match and digital_match.group():
            d_op = digital_match.group(1)
            d_wanttypes = int(digital_match.group(len(digital_match.groups())))
        if special_match and special_match.group():
            s_op = special_match.group(1)
            s_wanttypes = int(special_match.group(len(special_match.groups())))
        wordicts = dict(Counter(item))
        for key in wordicts.keys():
            if key in string.ascii_letters:
                l_types += 1
            elif key in string.digits:
                d_types += 1
            elif key in string.printable[62:-5]:
                s_types += 1

        letter_map = {'<': l_types < l_wanttypes, '<=': l_types <= l_wanttypes,
                      '>': l_types > l_wanttypes, '>=': l_types >= l_wanttypes,
                      '=': l_types == l_wanttypes, '==': l_types == l_wanttypes, }
        digital_map = {'<': d_types < d_wanttypes, '<=': d_types <= d_wanttypes,
                       '>': d_types > d_wanttypes, '>=': d_types >= d_wanttypes,
                       '=': d_types == d_wanttypes, '==': d_types == d_wanttypes, }
        special_map = {'<': s_types < s_wanttypes, '<=': s_types <= s_wanttypes,
                       '>': s_types > s_wanttypes, '>=': s_types >= s_wanttypes,
                       '=': s_types == s_wanttypes, '==': s_types == s_wanttypes, }
        if letter_map[l_op] and digital_map[d_op] and special_map[s_op]:
            return item
    else:
        return item


def repeat_filter(item, letter_repeat=pyoptions.letter_repeat, digital_repeat=pyoptions.digital_repeat,
                  special_repeat=pyoptions.special_repeat, repeat_is_filter=False):
    if item and repeat_is_filter:
        l_repeat = d_repeat = s_repeat = 0
        l_op = d_op = s_op = '>='
        l_wantrepeat = d_wantrepeat = s_wantrepeat = 0
        pattern = '((<|>|=)=?)(\d*)$'
        letter_match = re.match(pattern, letter_repeat)
        digital_match = re.match(pattern, digital_repeat)
        special_match = re.match(pattern, special_repeat)
        if letter_match and letter_match.group():
            l_op = letter_match.group(1)
            l_wantrepeat = int(letter_match.group(len(letter_match.groups())))
        if digital_match and digital_match.group():
            d_op = digital_match.group(1)
            d_wantrepeat = int(digital_match.group(len(digital_match.groups())))
        if special_match and special_match.group():
            s_op = special_match.group(1)
            s_wantrepeat = int(special_match.group(len(special_match.groups())))
        groups = groupby(item)
        repeat_dict = [{label: sum(1 for _ in group)} for label, group in groups]
        for r in repeat_dict:
            key = list(r.keys())[0]
            value = list(r.values())[0]
            if key in string.ascii_letters:
                l_repeat = max(l_repeat, value)
            elif key in string.digits:
                d_repeat = max(d_repeat, value)
            elif key in string.printable[62:-5]:
                s_repeat = max(s_repeat, value)

        letter_map = {'<': l_repeat < l_wantrepeat, '<=': l_repeat <= l_wantrepeat,
                      '>': l_repeat > l_wantrepeat, '>=': l_repeat >= l_wantrepeat,
                      '=': l_repeat == l_wantrepeat, '==': l_repeat == l_wantrepeat, }
        digital_map = {'<': d_repeat < d_wantrepeat, '<=': d_repeat <= d_wantrepeat,
                       '>': d_repeat > d_wantrepeat, '>=': d_repeat >= d_wantrepeat,
                       '=': d_repeat == d_wantrepeat, '==': d_repeat == d_wantrepeat, }
        special_map = {'<': s_repeat < s_wantrepeat, '<=': s_repeat <= s_wantrepeat,
                       '>': s_repeat > s_wantrepeat, '>=': s_repeat >= s_wantrepeat,
                       '=': s_repeat == s_wantrepeat, '==': s_repeat == s_wantrepeat, }
        if letter_map[l_op] and digital_map[d_op] and special_map[s_op]:
            return item
    else:
        return item


def regex_filter(item, regex='.*?', regex_is_filter=False):
    if item and regex_is_filter:
        try:
            if re.match(regex, item):
                return item
        except:
            pass
    else:
        return item


def cutout_filter(lists, start='pos-1', end='pos--1', cutout_is_filter=False):
    start_pos = 0
    end_pos = len(lists)

    def pos_change(position, init_pos, is_start=True):
        final_pos = init_pos
        try:
            match = re.match('pos-(\d*)', position)
            if match.group(1):
                final_pos = int(match.group(1)) - 1 if is_start else int(match.group(1))
            else:
                match = re.match('pos--(\d*)', position)
                if match.group(1):
                    pos = -int(match.group(1))
                    if is_start:
                        final_pos = pos - 1 if pos >= 1 else len(lists) + pos
                    else:
                        final_pos = pos if pos >= 1 else len(lists) + pos + 1
        except:
            pos = 0
            for _ in lists:
                if position == str(_):
                    final_pos = pos if is_start else pos + 1
                pos += 1
        return final_pos

    if lists and cutout_is_filter:
        start_pos = pos_change(start, start_pos, is_start=True)
        end_pos = pos_change(end, end_pos, is_start=False)

        if start_pos == 0 and start != 'pos-1':
            print(cool.fuchsia('[!] invalid start position changed' + pyoptions.CRLF))
        elif end_pos == len(lists) and end != 'pos--1':
            print(cool.fuchsia('[!] invalid end position changed' + pyoptions.CRLF))
        elif start_pos >= end_pos:
            start_pos = 0
            end_pos = len(lists)
            exit(cool.red('[!] start string behind from the end string' + pyoptions.CRLF))
        elif start_pos > len(lists) - 1:
            print(cool.fuchsia('[!] invalid position changed' + pyoptions.CRLF))
        elif end_pos > len(lists):
            print (cool.fuchsia('[!] end position beyond the scope' + pyoptions.CRLF))

        for _ in lists[start_pos:end_pos]:
            return _
    else:
        for _ in lists:
            return _


def filterforfun(item):
    item = headtail_filter(item, head=pyoptions.head, tail=pyoptions.tail)
    item = lenght_filter(item, minlen=pyoptions.minlen, maxlen=pyoptions.maxlen, lenght_is_filter=pyoptions.args_pick)
    item = occur_filter(item, letter_occur=pyoptions.letter_occur, digital_occur=pyoptions.digital_occur,
                        special_occur=pyoptions.special_occur, occur_is_filter=pyoptions.occur_is_filter)
    item = types_filter(item, letter_types=pyoptions.letter_types, digital_types=pyoptions.digital_types,
                        special_types=pyoptions.special_types, types_is_filter=pyoptions.types_is_filter)
    item = repeat_filter(item, letter_repeat=pyoptions.letter_repeat, digital_repeat=pyoptions.digital_repeat,
                         special_repeat=pyoptions.special_repeat, repeat_is_filter=pyoptions.repeat_is_filter)
    item = regex_filter(item, regex=pyoptions.filter_regex, regex_is_filter=pyoptions.regex_is_filter)
    item = encode_filter(item, encode=pyoptions.encode)
    return item
