#!/usr/bin/env python3

import os
import sys
import stat
from stat import *

if len(sys.argv) >= 2:
    filename = str(sys.argv[1])
else:
    print('Not enough arguments!!!')
    sys.exit(0)

fileMetadata = [(filename, os.lstat(filename))]

for name, meta in fileMetadata:
    if S_ISDIR(meta.st_mode):
        print('It is a directory')
    else:
        print('It is a regular file')
    print(name, 'take', meta.st_size, 'bytes')

print('File Permission', stat.filemode(os.stat(filename).st_mode))
