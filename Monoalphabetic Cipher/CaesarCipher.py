#!/usr/bin/env python3
"""
Based on code from https://www.youtube.com/watch?v=vPpRkHUPX_Q
"""

import string
import collections

mode = input("Would you like to encrypt(e) or decrypt(d)?: ")
message = input("Enter the message: ")
key = input("Enter the key: ")
"""
Figure out the order!
"""


def user_input(message, key):
    try:
        validate = int(key)
        if validate == int():
            return True
    except ValueError:
        print("Error: The key must be an int:")

    return message, key


def caesar(rotate_string, rotate_key):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(rotate_key)
    lower.rotate(rotate_key)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(str.maketrans(string.ascii_uppercase, upper)). \
        translate(str.maketrans(string.ascii_lowercase, lower))


def encrypt(key):
    key = int(key) * -1
    return key


def decrypt(key):
    key = int(key) * 1
    return key


def main(mode, message, key):
    if mode == "E":
        key = encrypt(key)
        user_input(message, key)
    elif mode == "D":
        key = decrypt(key)
        user_input(message, key)
    else:
        print("Error")

    print(caesar(message, int(key)))


main(mode, message, key)

