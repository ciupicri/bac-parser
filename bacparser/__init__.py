class BacParserException(Exception):
    pass

class BacParserUnsupportedYear(BacParserException, ValueError):
    pass
