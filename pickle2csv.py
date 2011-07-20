#!/usr/bin/env python
from __future__ import print_function
import argparse
import cPickle
import logging
import logging.config
import os
import sys

from utils import open_compressed_file, UnicodeWriter
import bacparser.models

def parse_args():
    parser = argparse.ArgumentParser(
            description='Extract results from bacalaureat')
    parser.add_argument('--year', metavar='YEAR', type=int,
            required=True, choices=bacparser.models.SUPPORTED_YEARS,
            help='Year of the exam')
    parser.add_argument('-o', '--output', metavar='OUTPUT',
                        type=lambda f: open(f, 'wb'), default=sys.stdout)
    parser.add_argument('filenames', metavar='FILE', type=str, nargs='+',
            help='Files to parse')
    return parser.parse_args()

def main():
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    args = parse_args()
    with args.output:
        csv_writer = UnicodeWriter(args.output)
        csv_writer.writerow(bacparser.models.get_model(args.year)._fields)
        for filename in args.filenames:
                logging.info('Converting %s' % (filename,))
                with open_compressed_file(filename) as f:
                    unpickler = cPickle.Unpickler(f)
                    try:
                        while True:
                            o = unpickler.load()
                            csv_writer.writerow(o)
                    except EOFError:
                        pass

if __name__ == '__main__':
    main()
