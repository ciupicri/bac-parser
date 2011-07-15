import logging

import lxml.etree

from ..utils import grouper

class BaseParser(object):
    """A basic parser"""

    _logger = logging.getLogger(__name__ + '.' + 'BaseParser')

    xpath_get_trs = \
        lxml.etree.XPath('tr[@hint]', regexp=False, smart_strings=False)

    xpath_get_tds = \
        lxml.etree.XPath('td', regexp=False, smart_strings=False)

    @classmethod
    def data_from_tr_filter(cls, s):
        return s.strip()

    @classmethod
    def get_elev(cls, main_table):
        for trs in grouper(2, cls.xpath_get_trs(main_table)):
            d = cls.get_extra_data_from_tr(trs[0])
            d.update(cls.get_data_from_tr(trs[0], cls.tr1_cols))
            d.update(cls.get_data_from_tr(trs[1], cls.tr2_cols))
            elev = cls.Elev(**d)
            if cls._logger.isEnabledFor(logging.INFO):
                cls._logger.info("extracted %s" % (elev,))
            yield elev

    @classmethod
    def get_data_from_tr(cls, tr, cols):
        return {c: cls.data_from_tr_filter(td.text_content())
                    for c, td in zip(cols, cls.xpath_get_tds(tr)) if c}
