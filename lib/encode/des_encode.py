#!/usr/bin/env python
# coding:utf-8
#
"""
Copyright (c) 2016-2019 LandGrey (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""
from __future__ import unicode_literals


def des_encode(item):
    """des algorithm and need modify code"""
    # replace your first key value, and replace second key and third key if it's exists
    first_key = "123456"
    second_key = ""
    third_key = ""

    length = len(item)
    middle_data = ""
    remainder = 0
    if length < 1:
        return ''

    def get_key_bytes(key):
        keyBytes = []
        leng = len(key)
        iterator = int(leng / 4)
        remainder = leng % 4
        i = 0
        for i in range(0, iterator):
            keyBytes.append(str_to_byte(key[i * 4 + 0:i * 4 + 4]))
            i += 1
        if remainder > 0:
            keyBytes.append(str_to_byte(key[i * 4 + 0:leng]))
        return keyBytes

    def str_to_byte(strs):
        leng = len(strs)
        bt = [None] * 64
        if leng < 4:
            for i in range(0, leng):
                k = ord(strs[i])
                for j in range(0, 16):
                    pow = 1
                    for m in range(15, j, -1):
                        pow *= 2
                    bt[16 * i + j] = int(k / pow) % 2
            for p in range(leng, 4):
                k = 0
                for q in range(0, 16):
                    pow = 1
                    for m in range(15, q, -1):
                        pow *= 2
                    bt[16 * p + q] = int(k / pow) % 2
        else:
            for i in range(0, 4):
                k = ord(strs[i])
                for j in range(0, 16):
                    pow = 1
                    for m in range(15, j, -1):
                        pow *= 2
                    bt[16 * i + j] = int(k / pow) % 2
        return bt

    def encode(data_byte, key_byte):
        keys = generate_keys(key_byte)

        ip_byte = init_permute(data_byte)
        ip_left = [None] * 32
        ip_right = [None] * 32
        temp_left = [None] * 32
        i = 0
        j = 0
        k = 0
        m = 0
        n = 0
        for k in range(0, 32):
            ip_left[k] = ip_byte[k]
            ip_right[k] = ip_byte[32 + k]
        for i in range(0, 16):
            for j in range(0, 32):
                temp_left[j] = ip_left[j]
                ip_left[j] = ip_right[j]
            key = [None] * 48
            for m in range(0, 48):
                key[m] = keys[i][m]

            temp_right = xor(p_permute(s_box_permute(xor(expand_permute(ip_right), key))), temp_left)
            for n in range(0, 32):
                ip_right[n] = temp_right[n]

        final_data = [None] * 64
        for i in range(0, 32):
            final_data[i] = ip_right[i]
            final_data[32 + i] = ip_left[i]
        return finally_permute(final_data)

    def generate_keys(key_byte):
        key = [None] * 56
        keys = [None] * 16
        keys[0] = []
        keys[1] = []
        keys[2] = []
        keys[3] = []
        keys[4] = []
        keys[5] = []
        keys[6] = []
        keys[7] = []
        keys[8] = []
        keys[9] = []
        keys[10] = []
        keys[11] = []
        keys[12] = []
        keys[13] = []
        keys[14] = []
        keys[15] = []
        loop = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

        for i in range(0, 7):
            k = 7
            for j in range(0, 8):
                key[i * 8 + j] = key_byte[8 * k + i]
                k -= 1

        for i in range(0, 16):
            temp_left = 0
            temp_right = 0
            for j in range(0, loop[i]):
                temp_left = key[0]
                temp_right = key[28]
                for k in range(0, 27):
                    key[k] = key[k + 1]
                    key[28 + k] = key[29 + k]
                key[27] = temp_left
                key[55] = temp_right
            tempKey = [None] * 48
            tempKey[0] = key[13]
            tempKey[1] = key[16]
            tempKey[2] = key[10]
            tempKey[3] = key[23]
            tempKey[4] = key[0]
            tempKey[5] = key[4]
            tempKey[6] = key[2]
            tempKey[7] = key[27]
            tempKey[8] = key[14]
            tempKey[9] = key[5]
            tempKey[10] = key[20]
            tempKey[11] = key[9]
            tempKey[12] = key[22]
            tempKey[13] = key[18]
            tempKey[14] = key[11]
            tempKey[15] = key[3]
            tempKey[16] = key[25]
            tempKey[17] = key[7]
            tempKey[18] = key[15]
            tempKey[19] = key[6]
            tempKey[20] = key[26]
            tempKey[21] = key[19]
            tempKey[22] = key[12]
            tempKey[23] = key[1]
            tempKey[24] = key[40]
            tempKey[25] = key[51]
            tempKey[26] = key[30]
            tempKey[27] = key[36]
            tempKey[28] = key[46]
            tempKey[29] = key[54]
            tempKey[30] = key[29]
            tempKey[31] = key[39]
            tempKey[32] = key[50]
            tempKey[33] = key[44]
            tempKey[34] = key[32]
            tempKey[35] = key[47]
            tempKey[36] = key[43]
            tempKey[37] = key[48]
            tempKey[38] = key[38]
            tempKey[39] = key[55]
            tempKey[40] = key[33]
            tempKey[41] = key[52]
            tempKey[42] = key[45]
            tempKey[43] = key[41]
            tempKey[44] = key[49]
            tempKey[45] = key[35]
            tempKey[46] = key[28]
            tempKey[47] = key[31]
            switch = {i: [keys[i].append(tempKey[m]) for m in range(0, 48)]}
            switch.get(i)
        return keys

    def init_permute(origin_data):
        ip_byte = [None] * 64
        m = 1
        n = 0

        for i in range(0, 4):

            k = 0
            for j in range(7, -1, -1):
                ip_byte[i * 8 + k] = origin_data[j * 8 + m]
                ip_byte[i * 8 + k + 32] = origin_data[j * 8 + n]
                k += 1
            m += 2
            n += 2
        return ip_byte

    def xor(byte_one, byte_two):
        xorByte = [None] * len(byte_one)
        for i in range(0, len(byte_one)):
            xorByte[i] = byte_one[i] ^ byte_two[i]
        return xorByte

    def p_permute(s_box_byte):
        pBoxPermute = [None] * 32
        pBoxPermute[0] = s_box_byte[15]
        pBoxPermute[1] = s_box_byte[6]
        pBoxPermute[2] = s_box_byte[19]
        pBoxPermute[3] = s_box_byte[20]
        pBoxPermute[4] = s_box_byte[28]
        pBoxPermute[5] = s_box_byte[11]
        pBoxPermute[6] = s_box_byte[27]
        pBoxPermute[7] = s_box_byte[16]
        pBoxPermute[8] = s_box_byte[0]
        pBoxPermute[9] = s_box_byte[14]
        pBoxPermute[10] = s_box_byte[22]
        pBoxPermute[11] = s_box_byte[25]
        pBoxPermute[12] = s_box_byte[4]
        pBoxPermute[13] = s_box_byte[17]
        pBoxPermute[14] = s_box_byte[30]
        pBoxPermute[15] = s_box_byte[9]
        pBoxPermute[16] = s_box_byte[1]
        pBoxPermute[17] = s_box_byte[7]
        pBoxPermute[18] = s_box_byte[23]
        pBoxPermute[19] = s_box_byte[13]
        pBoxPermute[20] = s_box_byte[31]
        pBoxPermute[21] = s_box_byte[26]
        pBoxPermute[22] = s_box_byte[2]
        pBoxPermute[23] = s_box_byte[8]
        pBoxPermute[24] = s_box_byte[18]
        pBoxPermute[25] = s_box_byte[12]
        pBoxPermute[26] = s_box_byte[29]
        pBoxPermute[27] = s_box_byte[5]
        pBoxPermute[28] = s_box_byte[21]
        pBoxPermute[29] = s_box_byte[10]
        pBoxPermute[30] = s_box_byte[3]
        pBoxPermute[31] = s_box_byte[24]
        return pBoxPermute

    def finally_permute(end_byte):
        fpByte = [None] * 64
        fpByte[0] = end_byte[39]
        fpByte[1] = end_byte[7]
        fpByte[2] = end_byte[47]
        fpByte[3] = end_byte[15]
        fpByte[4] = end_byte[55]
        fpByte[5] = end_byte[23]
        fpByte[6] = end_byte[63]
        fpByte[7] = end_byte[31]
        fpByte[8] = end_byte[38]
        fpByte[9] = end_byte[6]
        fpByte[10] = end_byte[46]
        fpByte[11] = end_byte[14]
        fpByte[12] = end_byte[54]
        fpByte[13] = end_byte[22]
        fpByte[14] = end_byte[62]
        fpByte[15] = end_byte[30]
        fpByte[16] = end_byte[37]
        fpByte[17] = end_byte[5]
        fpByte[18] = end_byte[45]
        fpByte[19] = end_byte[13]
        fpByte[20] = end_byte[53]
        fpByte[21] = end_byte[21]
        fpByte[22] = end_byte[61]
        fpByte[23] = end_byte[29]
        fpByte[24] = end_byte[36]
        fpByte[25] = end_byte[4]
        fpByte[26] = end_byte[44]
        fpByte[27] = end_byte[12]
        fpByte[28] = end_byte[52]
        fpByte[29] = end_byte[20]
        fpByte[30] = end_byte[60]
        fpByte[31] = end_byte[28]
        fpByte[32] = end_byte[35]
        fpByte[33] = end_byte[3]
        fpByte[34] = end_byte[43]
        fpByte[35] = end_byte[11]
        fpByte[36] = end_byte[51]
        fpByte[37] = end_byte[19]
        fpByte[38] = end_byte[59]
        fpByte[39] = end_byte[27]
        fpByte[40] = end_byte[34]
        fpByte[41] = end_byte[2]
        fpByte[42] = end_byte[42]
        fpByte[43] = end_byte[10]
        fpByte[44] = end_byte[50]
        fpByte[45] = end_byte[18]
        fpByte[46] = end_byte[58]
        fpByte[47] = end_byte[26]
        fpByte[48] = end_byte[33]
        fpByte[49] = end_byte[1]
        fpByte[50] = end_byte[41]
        fpByte[51] = end_byte[9]
        fpByte[52] = end_byte[49]
        fpByte[53] = end_byte[17]
        fpByte[54] = end_byte[57]
        fpByte[55] = end_byte[25]
        fpByte[56] = end_byte[32]
        fpByte[57] = end_byte[0]
        fpByte[58] = end_byte[40]
        fpByte[59] = end_byte[8]
        fpByte[60] = end_byte[48]
        fpByte[61] = end_byte[16]
        fpByte[62] = end_byte[56]
        fpByte[63] = end_byte[24]
        return fpByte

    def s_box_permute(expand_byte):
        sBoxByte = [None] * 32
        binary = ""
        s1 = [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

        s2 = [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

        s3 = [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

        s4 = [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

        s5 = [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

        s6 = [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

        s7 = [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

        s8 = [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

        for m in range(0, 8):
            i = 0
            j = 0
            i = expand_byte[m * 6 + 0] * 2 + expand_byte[m * 6 + 5]
            j = expand_byte[m * 6 + 1] * 2 * 2 * 2 + expand_byte[m * 6 + 2] * 2 * 2 \
                + expand_byte[m * 6 + 3] * 2 + expand_byte[m * 6 + 4]

            switch = {0: get_box_binary(s1[i][j]),
                      1: get_box_binary(s2[i][j]),
                      2: get_box_binary(s3[i][j]),
                      3: get_box_binary(s4[i][j]),
                      4: get_box_binary(s5[i][j]),
                      5: get_box_binary(s6[i][j]),
                      6: get_box_binary(s7[i][j]),
                      7: get_box_binary(s8[i][j])}
            binary = switch.get(m)
            sBoxByte[m * 4 + 0] = int(binary[0:1])
            sBoxByte[m * 4 + 1] = int(binary[1:2])
            sBoxByte[m * 4 + 2] = int(binary[2:3])
            sBoxByte[m * 4 + 3] = int(binary[3:4])
        return sBoxByte

    def get_box_binary(i):
        binary = ""
        switch = {0: "0000",
                  1: "0001",
                  2: "0010",
                  3: "0011",
                  4: "0100",
                  5: "0101",
                  6: "0110",
                  7: "0111",
                  8: "1000",
                  9: "1001",
                  10: "1010",
                  11: "1011",
                  12: "1100",
                  13: "1101",
                  14: "1110",
                  15: "1111"}
        binary = switch.get(i)
        return binary

    def expand_permute(right_data):
        epByte = [None] * 48
        for i in range(0, 8):
            if i == 0:
                epByte[i * 6 + 0] = right_data[31]
            else:
                epByte[i * 6 + 0] = right_data[i * 4 - 1]
            epByte[i * 6 + 1] = right_data[i * 4 + 0]
            epByte[i * 6 + 2] = right_data[i * 4 + 1]
            epByte[i * 6 + 3] = right_data[i * 4 + 2]
            epByte[i * 6 + 4] = right_data[i * 4 + 3]
            if i == 7:
                epByte[i * 6 + 5] = right_data[0]
            else:
                epByte[i * 6 + 5] = right_data[i * 4 + 4]
        return epByte

    def bt64_to_hex(byte_data):
        hex = ""
        for i in range(0, 16):
            bt = ""
            for j in range(0, 4):
                bt += str(byte_data[i * 4 + j])
            hex += bt4_to_hex(bt)
        return hex

    def bt4_to_hex(binary):
        switch = {"0000": "0",
                  "0001": "1",
                  "0010": "2",
                  "0011": "3",
                  "0100": "4",
                  "0101": "5",
                  "0110": "6",
                  "0111": "7",
                  "1000": "8",
                  "1001": "9",
                  "1010": "A",
                  "1011": "B",
                  "1100": "C",
                  "1101": "D",
                  "1110": "E",
                  "1111": "F",
                  }
        hex = switch.get(binary)
        return hex

    first_key_byte = second_key_byte = third_key_byte = ""
    first_length = second_length = third_length = 0
    if first_key is not None and first_key != "":
        first_key_byte = get_key_bytes(first_key)
        first_length = len(first_key_byte)
    if second_key is not None and second_key != "":
        second_key_byte = get_key_bytes(second_key)
        second_length = len(second_key_byte)
    if third_key is not None and third_key != "":
        third_key_byte = get_key_bytes(third_key)
        third_length = len(third_key_byte)

    if length < 4:
        iterator = 0
        bt = str_to_byte(item)
        if first_key is not None and first_key != "" and second_key is not None and second_key != "" and third_key is not None and third_key != "":
            temp_byte = bt
            for x in range(0, first_length):
                temp_byte = encode(temp_byte, first_key_byte[x])

            for y in range(0, second_length):
                temp_byte = encode(temp_byte, second_key_byte[y])

            for z in range(0, third_length):
                temp_byte = encode(temp_byte, third_key_byte[z])

            enc_byte = temp_byte
        elif first_key is not None and first_key != "" and second_key is not None and second_key != "":
            temp_byte = bt
            for x in range(0, first_length):
                temp_byte = encode(temp_byte, first_key_byte[x])

            for y in range(0, second_length):
                temp_byte = encode(temp_byte, second_key_byte[y])

            enc_byte = temp_byte
        elif first_key is not None and first_key != "":
            temp_byte = bt
            for x in range(0, first_length):
                temp_byte = encode(temp_byte, first_key_byte[x])
            enc_byte = temp_byte
        else:
            enc_byte = ""
        middle_data = bt64_to_hex(enc_byte)
    else:
        iterator = int(length / 4)
        remainder = length % 4
        for i in range(0, iterator):
            temp_data = item[i * 4 + 0:i * 4 + 4]
            temp_byte = str_to_byte(temp_data)
            if first_key is not None and first_key != "" and second_key is not None and second_key != "" and third_key is not None and third_key != "":
                temp_byte = temp_byte
                for x in range(0, first_length):
                    temp_byte = encode(temp_byte, first_key_byte[x])

                for y in range(0, second_length):
                    temp_byte = encode(temp_byte, second_key_byte[y])

                for z in range(0, third_length):
                    temp_byte = encode(temp_byte, third_key_byte[z])
                enc_byte = temp_byte
            elif first_key is not None and first_key != "" and second_key is not None and second_key != "":
                temp_byte = temp_byte
                for x in range(0, first_length):
                    temp_byte = encode(temp_byte, first_key_byte[x])

                for y in range(0, second_length):
                    temp_byte = encode(temp_byte, second_key_byte[y])
                enc_byte = temp_byte
            elif first_key is not None and first_key != "":
                temp_byte = temp_byte
                for x in range(0, first_length):
                    temp_byte = encode(temp_byte, first_key_byte[x])
                enc_byte = temp_byte
            else:
                enc_byte = ""
            middle_data += bt64_to_hex(enc_byte)

    if remainder > 0:
        remainder_data = item[iterator * 4 + 0:length]
        temp_byte = str_to_byte(remainder_data)
        if first_key is not None and first_key != "" and second_key is not None and second_key != "" and third_key is not None and third_key != "":
            temp_byte = temp_byte
            for x in range(0, first_length):
                temp_byte = encode(temp_byte, first_key_byte[x])
            for y in range(0, second_length):
                temp_byte = encode(temp_byte, second_key_byte[y])
            for z in range(0, third_length):
                temp_byte = encode(temp_byte, third_key_byte[z])
            enc_byte = temp_byte
        elif first_key is not None and first_key != "" and second_key is not None and second_key != "":
            temp_byte = temp_byte
            for x in range(0, first_length):
                temp_byte = encode(temp_byte, first_key_byte[x])

            for y in range(0, second_length):
                temp_byte = encode(temp_byte, second_key_byte[y])
            enc_byte = temp_byte
        elif first_key is not None and first_key != "":
            temp_byte = temp_byte
            for x in range(0, first_length):
                temp_byte = encode(temp_byte, first_key_byte[x])
            enc_byte = temp_byte
        else:
            enc_byte = ""
        middle_data += bt64_to_hex(enc_byte)

    return middle_data
