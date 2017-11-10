#!/bin/python3

import sys
from optparse import OptionParser


class unix_cat:
	def __init__(self):
		self.count = 1

# for line in sys.stdin:
#     print(line, end="")


def main():
	usage = "usage: %prog [option]... file..."

	parser = OptionParser(usage=usage)

	parser.add_option("-E",dest="showend",action="store_true",help="Show $ at line endings")

	parser.add_option("-n",dest="shownend",action="store_true",help="Show line numbers")

	(options,args) = parser.parser_args()


if __name__ == '__main__':
	main()