import os
import sys

from gzip import GzipFile
from bz2 import BZ2File
from lzma import LZMAFile


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
