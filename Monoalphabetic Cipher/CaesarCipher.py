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
        if validate == int():
            return True
    except ValueError:
        print("Error: The key must be an int:")

    return message, key


def caesar(message, key):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(key)
    lower.rotate(key)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return message.translate(str.maketrans(string.ascii_uppercase, upper)). \
        translate(str.maketrans(string.ascii_lowercase, lower))


def encrypt(key):
    key = int(key) * -1
    return key


def decrypt(key):
    key = int(key) * 1
    return key


def main(mode, message, key):
    if mode == "E" or mode == "e":
        key = encrypt(key)
        user_input(message, key)
    elif mode == "D" or mode == "d":
        key = decrypt(key)
        user_input(message, key)
    else:
        print("Error: Command not recognized")

    print(caesar(message, int(key)))


main(mode, message, key)

