import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("please enter your name.")