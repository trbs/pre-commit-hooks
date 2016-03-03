# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys
import argparse


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:
        if os.path.isfile(filename) and os.access(filename, os.X_OK):
            print('{0}: is executable'.format(filename))
            retval = 1
    return retval


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
