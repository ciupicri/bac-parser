r"""Parsers for the main_table"""

from .. import BacParserUnsupportedYear
from .parser2006 import Parser2006
from .parser2007 import Parser2007
from .parser2009 import Parser2009
from .parser2010 import Parser2010
from .parser2012 import Parser2012

SUPPORTED_YEARS = range(2006, 2012+1)

def get_parser_cls(year):
    """-> Parser class for the specified year"""
    if year < 2006:
        raise BacParserUnsupportedYear('Unsupported year')
    if year <= 2006:
        return Parser2006
    if year <= 2008:
        return Parser2007
    if year <= 2009:
        return Parser2009
    if year <= 2011:
        return Parser2010
    if year <= 2012:
        return Parser2012
    raise BacParserUnsupportedYear('Unsupported year')
