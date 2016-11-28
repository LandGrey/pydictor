#!/usr/bin/env python
# coding:utf-8
# Build by: LandGrey 2016-08-25
#
# A useful hacker dictionary  builder
#
# This is a part of belonging to pydictor


from core.Base import get_base_dic
from core.Base import getchars
from core.Chunk import get_chunk_dic
from core.SEDB import SEDB
from lib.command import parse_args


if __name__ == '__main__':
    args = parse_args()
    if args.type:
        get_base_dic(args.len[0], args.len[1], getchars(args.type), args.encode, args.head, args.tail)
    if args.customchar:
        get_base_dic(args.len[0], args.len[1], args.customchar, args.encode, args.head, args.tail)
    if args.chunk:
        chunk = []
        for item in args.chunk:
            if item != '':
                chunk.append(item)
        get_chunk_dic(chunk, args.encode, args.head, args.tail)
    if args.sedb:
        try:
            shell = SEDB()
            shell.cmdloop()
        except:
            exit()


