"""leap.py

Copyright (c) 2021 Thierry P.G. DECKER
All Rights Reserved.
Released under the MIT license

"""


def main():
    """The main function

    Will test if a given year is leap
    """
    #
    # Test and display a text if a year is leap or not
    #
    year = 2016
    if year % 4 == 0 and year % 100 != 0:
        print(year, "is leap")
    else:
        print(year, "is not leap")


if __name__ == '__main__':
    main()
