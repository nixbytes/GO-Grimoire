#!/usr/bin/env python3

import os

import sys

if len(sys.argv) >= 2:
    what = str(sys.argv[1])
else:
    print('Not enough arguments!!!')
    sys.exit(0)

if os.path.isdir(what):
    print(what,'is a directory')
elif os.path.isfile(what):
    print(what,'is a file')