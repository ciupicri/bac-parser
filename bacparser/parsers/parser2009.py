import logging
import re

import lxml.etree

from .. import BacParserException
from .parser2006 import Parser2006

class Parser2009(Parser2006):
    """Parser for the year 2009 onwards"""

    _logger = logging.getLogger(__name__ + '.' + 'Parser2009')

    xpath_get_script = \
        lxml.etree.XPath('script[1]/text()', regexp=False, smart_strings=False)

    js_luat_regex = re.compile(
        r'''Luat_?De_?Pe_?BacalaureatEduRo\["([^"]*)"]="([^"]*)";''')

    tr1_cols = (
        None, # Nr. crt.
        None, # nume; use another method to get it
        None, # Pozitia in ierarhie...
        None, # Pozitia in ierarhie...
        'scoala',
        'judet',
        'promotie_anterioara',
        'forma_invatamant',
        'specializare',
        'd_romana_oral_nota',
        'd_romana_scris_nota', 'd_romana_scris_nota_contestatie', 'd_romana_scris_nota_finala',
        'd_limba_materna_nume',
        'd_limba_moderna_nume', 'd_limba_moderna_nota',
        'd_profil_scris_nume',
        'd_alegere_aria_curiculara_nume',
        None, # d_alegere_alte_arii_curiculare_nume; use another method to get it
        None, # media
        None # rezultat_final; use another method to get it
        )

    @classmethod
    def get_luat_de_pe_bacalaureat(cls, tr):
        script = cls.xpath_get_script(tr)[0]
        items = cls.js_luat_regex.findall(script)
        if len(items) != 3:
            raise BacParserException("script paranormal: n-am gasit 3 chei")
        if not (items[0][0] == items[1][0] == items[2][0]):
            raise BacParserException("script paranormal: cheie inegale")
        return items

    @classmethod
    def get_extra_data_from_tr(cls, tr):
        items = cls.get_luat_de_pe_bacalaureat(tr)
        return {
            'nume': items[0][0].replace('<br>', ''),
            'd_alegere_alte_arii_curiculare_nume':
                ' - '.join(cls.data_from_tr_filter(t) for t in
                    cls.xpath_get_d_alegere_alte_arii_curiculare_nume(tr)[:2]),
            'rezultat_final': items[2][1]}
