#!/usr/bin/env python
from __future__ import print_function
import argparse
import logging
import logging.config
import sys

from bacparser.maintable import get_main_table_from_file
import bacparser.parsers

def get_data_from_file(f, year):
    parser = bacparser.parsers.get_parser(year)
    main_table = get_main_table_from_file(f, year)
    for i in parser.get_elev(main_table):
        yield i

def parse_args():
    parser = argparse.ArgumentParser(
            description='Extract results from bacalaureat')
    parser.add_argument('--year', metavar='YEAR', type=int,
            required=True, choices=bacparser.parsers.SUPPORTED_YEARS,
            help='Year of the exam')
    parser.add_argument('filenames', metavar='FILE', type=str, nargs='+',
            help='Files to parse')
    return parser.parse_args()

def main():
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    args = parse_args()
    for filename in args.filenames:
        with open(filename, 'rb') as f:
            logging.info("Extracting from %s" % (filename,))
            for i in get_data_from_file(f, args.year):
                print(i)

if __name__ == '__main__':
    main()
