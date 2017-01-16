#!/usr/bin/env python3
"""
Based on code from https://www.youtube.com/watch?v=vPpRkHUPX_Q
"""

import string
import collections


message = input("Enter you message: ")
key = input("Enter the key: ")
try:
    validate = int(key)
except ValueError:
    print("Error: The key must be an int:")


def caesar(rotate_string, number_to_rotate_by):

    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)).\
        translate(str.maketrans(string.ascii_lowercase, lower))


print(caesar(message, int(key)))


