import os
import fileinput

for line in fileinput.input():
    print(line, end="")
