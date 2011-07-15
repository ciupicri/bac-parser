from .. import BacParserUnsupportedYear
from . import elev2006
from . import elev2010

SUPPORTED_YEARS = range(2006, 2011+1)

def get_model(year):
    if year < 2006:
        raise BacParserValueError('Unsupported year')
    if year <= 2009:
        return elev2006.Elev
    if year <= 2011:
        return elev2010.Elev
    # year > 2011
    raise BacParserUnsupportedYear('Unsupported year')
