#!/usr/bin/env python3
"""
Based on code from https://www.youtube.com/watch?v=vPpRkHUPX_Q
"""

import string
import collections

mode = input("Would you like to encrypt(e) or decrypt(d)?: ")
message = input("Enter the message: ")
key = input("Enter the key: ")


def user_input(message, key):
    try:
        validate = int(key)
    except ValueError:
        print("Error: The key must be an int:")

    return message, key


def caesar(rotate_string, number_to_rotate_by):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(number_to_rotate_by)
    lower.rotate(number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)). \
        translate(str.maketrans(string.ascii_lowercase, lower))


if mode == "E" or "e":
    user_input(message, key)
    key = int(key) * -1
    # print(caesar(message, int(key)))
elif mode == "D" or "d":
    user_input(message, key)
    # print(caesar(message, int(key)))
else:
    print("Error")


print(caesar(message, int(key)))

