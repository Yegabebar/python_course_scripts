"""Caesar algorithm

Copyright (c) 2021 Mathieu Barbe-gayet
All Rights Reserved.
Released under the MIT license

"""

import string


def main():
    """The main function
    Will ask the user for a string and a shift value until the values are correct,
    then print the result of the encrypt() function
    """
    user_string = "0"
    while True:
        user_string = input("Please input a string to encrypt: ")
        if user_string.isalpha():
            break
    shift = ""
    while True:
        shift = input("Please input an offset to use for the encryption: ")
        if shift.isdigit():
            break

    print("Caesar-encoded string:", encrypt_v2(user_string, shift))


def encrypt_v1(user_string, shift):
    """The encryption function
    Will give us a string composed with the n+x of each character from the original string
    """
    ascii_list = string.ascii_lowercase
    cyphered_string = []
    for character in user_string:
        #
        # For each character from the user's string, we get the corresponding index in the ascii array
        # - get the index where is stored the given character
        # - create a new index with the int-converted shift value provided by the user
        # - use this index to get the encoded character
        # - add the character to the final string to give to the user
        #
        ascii_char_index = ascii_list.index(character)
        shifted_index = (int(shift) + ascii_char_index) % len(ascii_list)
        resulting_char = ascii_list[shifted_index]
        cyphered_string.append(resulting_char)
    return "".join(cyphered_string)


def encrypt_v2(user_string, shift):
    """The encryption function
    Will give us a string composed with the n+x of each character from the original string
    """
    ascii_list = string.ascii_lowercase
    cyphered_string = []
    for character in user_string:
        #
        # For each character from the user's string, we get the corresponding index in the ascii array
        # - get the index where is stored the given character
        # - create a new index with the int-converted shift value provided by the user
        # - use this index to get the encoded character
        # - add the character to the final string to give to the user
        #
        cyphered_string.append(ascii_list[(int(shift) + ascii_list.index(character)) % len(ascii_list)])
    return "".join(cyphered_string)


if __name__ == '__main__':
    main()
