#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szablon.py

def main(args):
    a = input("Podaj 1. liczbę: ")
    print(a)
    b = input("Podaj 2. liczbę: ")
    print(b)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
