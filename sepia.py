import data
import ppmdiff
import utility
import sys

if __name__ == '__main__':
    try:
        with open(sys.argv[0]) as file:
            print('Success')

    except FileNotFoundError:
        print("Error")

