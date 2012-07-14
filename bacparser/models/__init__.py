from .. import BacParserUnsupportedYear
from . import elev2006
from . import elev2010

SUPPORTED_YEARS = range(2006, 2012+1)

def get_model(year):
    if year < 2006:
        raise BacParserValueError('Unsupported year')
    if year <= 2009:
        return elev2006.Elev
    if year <= 2012:
        return elev2010.Elev
    raise BacParserUnsupportedYear('Unsupported year')
