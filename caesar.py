"""Module name.

Copyright (c) 2021 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""

#
# Coder l'algorithme de César
#

# - Demander la chaine de caractère à chiffer à l'utilisateur : input()
# - Demander à l'utilisateur le décalage à appliquer au chiffrement
# - Afficher la chaine chiffrée
#

# Exemple :
#
# Texte en clair : "ABCDXYZ"
# Décalage : 2
# Texte chiffré : "CDEFG...ZAB"
#
# ABCDE
# CDEAB
#

import string


def main():
    """The main function
    Will
    """
    user_string = "0"
    shift = ""
    while True:
        user_string = input("Please input a string to encrypt: ")
        if user_string.isalpha():
            break

    while True:
        shift = input("Please input an offset to use for the encryption: ")
        if shift.isdigit():
            break

    encrypt(user_string, shift)


def encrypt(user_string, shift):
    """The encryption function
    Will
    """
    char_list = string.ascii_lowercase
    cyphered_string = []
    for character in user_string:
        print("first loop")
        for index, ascii_char in enumerate(char_list):
            print("in list: ", ascii_char)
            #
            # For each character from the user's string, we browse the ascii list
            # to get the corresponding character with all it's info
            #
            if ascii_char == character:
                print(shift)
                print(index)
                print((int(index) + int(shift)))
                if (int(ascii_char.index()) + int(shift)) > char_list.len():
                    shift = int(shift % char_list.len())
            new_char = char_list(int(char_list.index(index)) + shift)
            cyphered_string.append(new_char)



if __name__ == '__main__':
    main()
