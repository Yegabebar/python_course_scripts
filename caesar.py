"""Caesar algorithm

Copyright (c) 2021 Mathieu Barbe-gayet
All Rights Reserved.
Released under the MIT license

"""

import string


def main():
    """The main function
    Will ask the user for a string and a shift value until the values are correct,
    then print the result of one of the chosen encrypt() functions.
    """

    #
    # The following two while loop will keep asking the user for an input
    # until the next two conditions are true
    #
    while True:
        user_string = input("Please input a string to encrypt: ")
        if user_string.isalpha():
            break
    while True:
        shift = input("Please input an offset to use for the encryption: ")
        if shift.isdigit():
            break
    #
    # Directly prints the results of the chosen encoding function (v1 or v2), here I've chosen to use the version 2
    #
    print("Caesar-encoded string:", encrypt_v2(user_string, shift))


def encrypt_v1(user_string, shift):
    """The encryption function
    Will give us a string composed with the n+x of each character from the original string,
    according to the caesar algorithm
    """
    ascii_list = string.ascii_lowercase
    cyphered_string = []
    #
    # For each character from the user's string
    #
    for character in user_string:
        #
        # get the index where is stored the given character
        #
        ascii_char_index = ascii_list.index(character)
        #
        # create a new index with the int-converted shift value provided by the user
        #
        shifted_index = (int(shift) + ascii_char_index) % len(ascii_list)
        #
        # use this index to get the encoded character
        #
        resulting_char = ascii_list[shifted_index]
        #
        # add the character to the final string to give to the user
        #
        cyphered_string.append(resulting_char)
    return "".join(cyphered_string)


def encrypt_v2(user_string, shift):
    """The encryption function
    Will give us a string composed with the n+x of each character from the original string.
    This version 2 is basically a one-liner version of the version 1 above.
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
