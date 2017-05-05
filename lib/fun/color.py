#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2017 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals

import os
from lib.fun.osjudger import *


class Colored(object):
    if is_Windows():
        os.system("color")
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    ORANGE = '\033[0;33;1m'
    BLUE = '\033[34m'
    FUCHSIA = '\033[35m'
    WHITE = '\033[37m'

    #: no color
    RESET = '\033[0m'

    def color_str(self, color, s):
        if is_higher_win10_v1511() or is_Linux() or is_Mac():
            return '{}{}{}'.format(getattr(self, color), s, self.RESET)
        else:
            return '{}'.format(s)

    def red(self, s):
        return self.color_str('RED', s)

    def green(self, s):
        return self.color_str('GREEN', s)

    def yellow(self, s):
        return self.color_str('YELLOW', s)

    def orange(self, s):
        return self.color_str('ORANGE', s)

    def blue(self, s):
        return self.color_str('BLUE', s)

    def fuchsia(self, s):
        return self.color_str('FUCHSIA', s)

    def white(self, s):
        return self.color_str('WHITE', s)
