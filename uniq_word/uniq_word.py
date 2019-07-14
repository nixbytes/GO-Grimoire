#!/usr/bin/python3
# import os
import sys

'''
this is a smaill program to find words that are uniq

'''

tm = open(str(sys.argv[1]), 'r')


for line in tm:
    # clean each read line
    line = line.strip()

    line = line.translate('!@#$%^&*()_+{}[]\|-=')

    line = line.lower()

    list = line.split(' ')

    print(list)

dict = {}

for word in list:
    dict[word] = 1

    if word in dict:
        count = dict[word]
        count += 1
        dict[word] = count
    else:
        dict[word] = 1

for word, count in dict.items():
    print(word + ":" + str(count))
