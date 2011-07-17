#!/usr/bin/env python
from __future__ import print_function
import argparse
import cPickle
import functools
import logging
import logging.config
import os
import sys

from gzip import GzipFile
from bz2 import BZ2File
from lzma import LZMAFile

from bacparser.maintable import get_main_table_from_file
import bacparser.parsers


COMPRESSED_FILE_CLASSES = {'.gz': GzipFile,
                           '.bz2': BZ2File,
                           '.xz': LZMAFile}

def open_compressed_file(filename):
    """Open a possibly compressed file. '-' stands for stdin"""
    global COMPRESSED_FILE_CLASSES

    if filename == '-':
        return sys.stdin
    ext = os.path.splitext(filename)[1]
    f = COMPRESSED_FILE_CLASSES.get(ext, file)(filename)
    dir(f) # workaround for https://bugzilla.redhat.com/show_bug.cgi?id=720111
    return f


def get_data_from_file(f, year):
    parser = bacparser.parsers.get_parser(year)
    main_table = get_main_table_from_file(f, year)
    for i in parser.get_elev(main_table):
        yield i

def write_python(f, record):
    f.write(repr(record))
    f.write('\n#######################################################################\n')

def write_pickle(f, record):
    cPickle.dump(record, f, cPickle.HIGHEST_PROTOCOL)

def parse_args():
    parser = argparse.ArgumentParser(
            description='Extract results from bacalaureat')
    parser.add_argument('--year', metavar='YEAR', type=int,
            required=True, choices=bacparser.parsers.SUPPORTED_YEARS,
            help='Year of the exam')
    parser.add_argument('--format', metavar='FORMAT',
                        type=str, choices=('python', 'pickle'),
                        default='python')
    parser.add_argument('-o', '--output', metavar='OUTPUT',
                        type=lambda f: open(f, 'wb'), default=sys.stdout)
    parser.add_argument('filenames', metavar='FILE', type=str, nargs='+',
            help='Files to parse')
    return parser.parse_args()

def main():
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    args = parse_args()
    if args.format == 'python':
        write = functools.partial(write_python, args.output)
    else: # 'pickle'
        write = functools.partial(write_pickle, args.output)
    with args.output:
        for filename in args.filenames:
            with open_compressed_file(filename) as f:
                logging.info("Extracting from %s" % (filename,))
                for i in get_data_from_file(f, args.year):
                    write(i)

if __name__ == '__main__':
    main()
