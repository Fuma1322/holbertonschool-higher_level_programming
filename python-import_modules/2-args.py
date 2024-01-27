#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print("0 arguments.")
else:
    print("{:d} argument{}:".format(len(argv) - 1, 's' if len(argv) > 2 else ''))
    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))
