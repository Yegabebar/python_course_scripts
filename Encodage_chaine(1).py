std_base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
chain = input("Enter a character string")


def main():
    pass


def change_string_to_list(p_chain, step):
    """step 1 & 7
    """
    #
    # Splitting a chain into chunks of the specified step
    #
    new_list = [p_chain[i:i + step] for i in range(0, len(p_chain), step)]
    return new_list


def change_to_unicode(p_list):
    """step 2
    """
    #
    # Converts each element in the list in its unicode index
    #
    new_list = []
    for elt in p_list:
        new_char = ord(elt)
        new_list.append(new_char)
    return new_list


def change_to_binary(p_unicode_list):
    """step 3
    """
    #
    # Changes every element in the list to its binary equivalent
    #
    new_list = []
    for elt in p_unicode_list:
        binary = bin(elt)
        new_list.append(binary)
    return new_list


def delete_0b_from_binary(p_binary_list):
    """step 4
    """
    #
    # Removes "0b" from the binary expressions
    #
    new_list = []
    for elt in p_binary_list:
        s_binary = elt[2:]
        new_list.append(s_binary)
    return new_list


def add_zeroes_left_side(p_s_binary_list):
    """step 5
    """
    #
    # Fills each expressions with 0s to reach 8 characters
    #
    new_list = []
    for elt in p_s_binary_list:
        a_0_binary = elt.zfill(8)
        new_list.append(a_0_binary)
    return new_list


def change_list_to_string(p_t_list):
    """step 6 & 11
    """
    #
    # ... It takes a list, and turns it into a string :upside_down:
    #
    new_string = "".join(p_t_list)
    return new_string


def fill_last_item(p_s_list):
    """step 8
    """
    #
    # Fills the last element of a list to reach the same size as the others
    #
    new_list = []
    for elt in p_s_list:
        new_list.append(elt.ljust(len(p_s_list[0]), "0"))
    return new_list


def change_from_binary(p_bin_list):
    """step 9
    """
    #
    # Turns binary number in decimal ones
    #
    new_list = []
    for elt in p_bin_list:
        new_int = int(elt, 2)
        new_list.append(new_int)
    return new_list


def convert_to_base64(p_int_list):
    """step 10
    """
    #
    # Uses ints to be used as a base64 index
    #
    new_list = []
    for elt in p_int_list:
        new_char = std_base64chars[elt]
        new_list.append(new_char)
    return new_list


def convert_string_to_base64_compatible(p_string):
    """step 12
    """
    #
    # base64 needs its elements to be multiples of 4, so we check how long our string is and add =s accordingly
    #
    chars_to_add = (4 - (len(p_string)%4))%4
    new_string = "".join(p_string)
    for i in range(chars_to_add):
        new_string += "="
    return new_string


if __name__ == '__main__':
    main()
    result1 = change_string_to_list(chain, 1)
    print(result1)
    result2 = change_to_unicode(result1)
    print(result2)
    result3 = change_to_binary(result2)
    print(result3)
    result4 = delete_0b_from_binary(result3)
    print(result4)
    result5 = add_zeroes_left_side(result4)
    print(result5)
    result6 = change_list_to_string(result5)
    print(result6)
    result7 = change_string_to_list(result6, 6)
    print(result7)
    result8 = fill_last_item(result7)
    print(result8)
    result9 = change_from_binary(result8)
    print(result9)
    result10 = convert_to_base64(result9)
    print(result10)
    result11 = change_list_to_string(result10)
    print(result11)
    result12 = convert_string_to_base64_compatible(result11)
    print(result12)
