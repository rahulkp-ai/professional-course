"""
scripts
"""

import sys

def main(arguments):
    print("this is the main function, and it has access to the following variables:")
    for argument in arguments:
        print(argument)
    print(type(argument))
    print(argument)


if __name__ == '__main__':
    main(sys.argv)