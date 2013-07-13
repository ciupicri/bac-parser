#!/usr/bin/env python
from __future__ import print_function
import argparse
from contextlib import closing
try:
    import cPickle as pickle
except ImportError:
    import pickle
import functools
import logging
import logging.config
import math
from multiprocessing import Pool
import sys
import time

from utils import open_compressed_file

import bacparser.parsers

def write_python(f, record):
    f.write(repr(record))
    f.write('\n#######################################################################\n')

def write_pickle(f, record):
    pickle.dump(record, f, pickle.HIGHEST_PROTOCOL)

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
    parser.add_argument('--processes', metavar='PROCESSES',
                        type=int)
    parser.add_argument('filenames', metavar='FILE', type=str, nargs='+',
            help='Files to parse')
    return parser.parse_args()


# === parallel processing ===

parser_cls = None

def initialize(year):
    global parser_cls
    parser_cls = bacparser.parsers.get_parser_cls(year)

def parse(filename):
    with open_compressed_file(filename) as f:
        logging.info("Extracting from %s" % (filename,))
        return list(parser_cls(f))

# === end of parallel processing ===


def main():
    logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
    args = parse_args()
    if args.format == 'python':
        write = functools.partial(write_python, args.output)
    else: # 'pickle'
        write = functools.partial(write_pickle, args.output)
    with args.output:
        with closing(Pool(args.processes, initialize, (args.year,))) as pool:
            # split the workload in equal large chunks
            chunksize = len(args.filenames) / pool._processes + \
                        1 if len(args.filenames) % pool._processes else 0
            for L in pool.imap_unordered(parse, args.filenames, chunksize=chunksize):
                for i in L:
                    write(i)


if __name__ == '__main__':
    main()
