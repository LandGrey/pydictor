#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

from lib.fun.fun import walk_pure_file
from lib.data.data import paths, pystrs, pyoptions


def sedb_tricks():
    for line in walk_pure_file(paths.sedbtrick_path, pure=False):
        trick = line.split(pyoptions.key_value_split)
        if len(trick) == 2:
            if trick[0].strip() == pystrs.sedb_trick_prefix:
                for _ in trick[1].strip().split(pyoptions.trick_split):
                    pyoptions.sedb_trick_pre.append(_)
            elif trick[0].strip() == pystrs.sedb_trick_suffix:
                for _ in trick[1].strip().split(pyoptions.trick_split):
                    pyoptions.sedb_trick_suf.append(_)
            elif trick[0].strip() == pystrs.sedb_trick_middle:
                for _ in trick[1].strip().split(pyoptions.trick_split):
                    pyoptions.sedb_trick_mid.append(_)
