#!/usr/bin/python3

def is_lower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        print("{} is a lowercase alphabet".format(c))
    else:
        print ("{} is not a lowercase alphabet".format(c))

ans = input("Enter a character: ")
is_lower(ans)
