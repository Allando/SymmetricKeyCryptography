#!/usr/bin/env python3
"""
code from https://www.youtube.com/watch?v=vPpRkHUPX_Q
"""

import string
import collections


def caesar(rotate_string, number_to_rotate_by):

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).\
        translate(str.maketrans(string.ascii_lowercase,lower))


print(caesar("Hello, World", 13))

