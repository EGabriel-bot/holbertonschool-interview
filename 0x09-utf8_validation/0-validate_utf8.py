#!/usr/bin/python3
"""Task 0"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    b_1 = 1 << 7
    b_2 = 1 << 6
    nbytes = 0
    if not data or len(data) == 0:
        return True
    for num in data:
        bit = 1 << 7
        if nbytes == 0:
            while (bit & num):
                nbytes += 1
                bit = bit >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (num & b_1 and not (num & b_2)):
                return False
        nbytes -= 1
    if nbytes:
        return False
    else:
        return True
