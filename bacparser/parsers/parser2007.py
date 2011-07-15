import logging

from .parser2006 import Parser2006

class Parser2007(Parser2006):
    """Parser for the year 2007 onwards"""

    _logger = logging.getLogger(__name__ + '.' + 'Parser2007')

    @classmethod
    def get_extra_data_from_tr(cls, tr):
        return {
            'd_alegere_alte_arii_curiculare_nume':
                ' - '.join(cls.data_from_tr_filter(t) for t in
                    cls.xpath_get_d_alegere_alte_arii_curiculare_nume(tr)[:2])}
