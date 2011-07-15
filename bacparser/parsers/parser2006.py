import logging

import lxml.etree

from .baseparser import BaseParser
from ..models import elev2006

class Parser2006(BaseParser):
    """Parser for the year 2006 onwards"""

    _logger = logging.getLogger(__name__ + '.' + 'Parser2006')

    Elev = elev2006.Elev

    xpath_get_d_alegere_alte_arii_curiculare_nume = \
        lxml.etree.XPath('td[19]/text()', regexp=False, smart_strings=False)

    tr1_cols = (
        None, # Nr. crt.
        'nume',
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
        'rezultat_final',
        )

    tr2_cols = (
        'd_limba_materna_oral_nota',
        'd_limba_materna_scris_nota', 'd_limba_materna_scris_nota_contestatie', 'd_limba_materna_scris_nota_finala',
        'd_profil_scris_nota', 'd_profil_scris_nota_contestatie', 'd_profil_scris_nota_finala',
        'd_alegere_aria_curiculara_nota', 'd_alegere_aria_curiculara_nota_contestatie', 'd_alegere_aria_curiculara_nota_finala',
        'd_alegere_alte_arii_curiculare_nota', 'd_alegere_alte_arii_curiculare_nota_contestatie', 'd_alegere_alte_arii_curiculare_nota_finala',
        )

    @classmethod
    def get_extra_data_from_tr(cls, tr):
        return {
            'd_alegere_alte_arii_curiculare_nume':
                ' - '.join(cls.data_from_tr_filter(t) for t in
                    cls.xpath_get_d_alegere_alte_arii_curiculare_nume(tr))}
