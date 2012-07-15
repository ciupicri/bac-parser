#!/usr/bin/env python
from __future__ import print_function
import argparse
import cPickle
import functools
import logging
import logging.config
import sys
import time

from utils import open_compressed_file

from bacparser.maintable import get_main_table_from_file
import bacparser.parsers

def write_python(f, record):
    f.write(repr(record))
    f.write('\n#######################################################################\n')

def write_pickle(f, record):
    cPickle.dump(record, f, cPickle.HIGHEST_PROTOCOL)

def parse_args():
    parser = argparse.ArgumentParser(
            description='Extract results from http://bacalaureat.edu.ro pages')
    parser.add_argument('--year', metavar='YEAR', type=int,
            choices=bacparser.parsers.SUPPORTED_YEARS,
            default=time.localtime(time.time()).tm_year,
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
    parser = bacparser.parsers.get_parser(args.year)
    if args.format == 'python':
        write = functools.partial(write_python, args.output)
    else: # 'pickle'
        write = functools.partial(write_pickle, args.output)
    with args.output:
        for filename in args.filenames:
            with open_compressed_file(filename) as f:
                logging.info("Extracting from %s" % (filename,))
                main_table = get_main_table_from_file(f, args.year)
                for i in parser.get_elev(main_table):
                    write(i)

if __name__ == '__main__':
    main()
