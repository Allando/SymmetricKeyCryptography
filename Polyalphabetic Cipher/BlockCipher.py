#!/usr/bin/env python3
"""
Based on code from https://www.youtube.com/watch?v=vPpRkHUPX_Q

So this is basically the same as the normal Caesar Cipher, except is better!!
"""

import string
import collections
import time

mode = input("Would you like to encrypt(e) or decrypt(d)?: ")
message = input("Enter the message: ")
key_one = input("Enter the first key: ")
key_two = input("Enter the second key: ")


def user_input(input_text, key_one, key_two):
    input_text.split(' ')
    try:
        validate_one = int(key_one)
        validate_two = int(key_two)
        if validate_one == int() and validate_two == int():
            return True
    except ValueError:
        print("Error: The key must be an int:")

    return input_text, key_one, key_two


def cipher_one(plain_text, key_one):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(key_one)
    lower.rotate(key_one)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return plain_text.translate(str.maketrans(string.ascii_uppercase, upper)). \
        translate(str.maketrans(string.ascii_lowercase, lower))


def cipher_two(cipher_text, key_two):
    upper = collections.deque(string.ascii_uppercase)
    lower = collections.deque(string.ascii_lowercase)

    upper.rotate(key_two)
    lower.rotate(key_two)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return cipher_text.translate(str.maketrans(string.ascii_uppercase, upper)). \
        translate(str.maketrans(string.ascii_lowercase, lower))


def encrypt(key):
    key = int(key) * -1
    return key


def decrypt(key):
    key = int(key) * 1
    return key


def main(cipher_mode, input_text, key_one, key_two):
    if cipher_mode == "E" or cipher_mode == "e":
        user_input(input_text, key_one, key_two)
        crypto_key_one = encrypt(key_one)
        crypto_key_two = encrypt(key_two)

        print("Cipher text:", cipher_two(cipher_one(input_text, int(crypto_key_one)), crypto_key_two))
    elif cipher_mode == "D" or cipher_mode == "d":
        user_input(input_text, key_one, key_two)
        crypto_key_one = decrypt(key_one)
        crypto_key_two = decrypt(key_two)

        print("Plain text:", cipher_two(cipher_one(input_text, int(crypto_key_one)), crypto_key_two))
    else:
        print("Error: Command not recognized")
        # time.sleep(0.5)


main(mode, message, key_one, key_two)

