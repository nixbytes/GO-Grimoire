import sys

from optparse import OptionParser


class unix_cat:

    def __init__(self):
        self.count = 1

    def run(self, i, options):
        # basic mod for print the line
        e = ""
        for line in i:
            if options.showend:
                line = line.rstrip()
                e = "$\n"
            if options.shownum:
                line = "{0} {1}".format(self.count, line)

            self.count += 1
            print(line, end=e)


def main():

    usage = "usage: %prog [option]... [file]..."

    parser = OptionParser(usage=usage)

    parser.add_option("-E", dest="showend", action="store_true",
                      help="Show $ at line endings")

    parser.add_option("-n", dest="shownum",
                      action="store_true", help="Show line numbers")

    (options, args) = parser.parse_args()

    c = unix_cat()

    # check if file name is given
    if len(args) > 1:
        for a in args:
            f = open(a, "r")
            c.run(f, options)
    else:
        c.run(sys.stdin, options)

if __name__ == '__main__':
	
    main()
