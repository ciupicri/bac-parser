import logging

import lxml.etree

from .baseparser import BaseParser
from ..models import elev2010

class Parser2012(BaseParser):
    """Parser for the year 2012 onwards"""

    _logger = logging.getLogger(__name__ + '.' + 'Parser2012')

    Elev = elev2010.Elev

    xpath_get_trs = \
        lxml.etree.XPath('tr[@onclick]', regexp=False, smart_strings=False)

    xpath_get_nume = \
        lxml.etree.XPath('td[2]/text()', regexp=False, smart_strings=False)

    tr1_cols = (
        None, # Nr. crt.
        None, # Nume... <script>
        'scoala',
        'judet',
        'promotie_anterioara',
        'forma_invatamant',
        'specializare',
        'd_romana_competente', 'd_romana_scris_nota', 'd_romana_scris_nota_contestatie', 'd_romana_scris_nota_finala',
        'd_limba_materna_nume',
        'd_limba_moderna_nume', 'd_limba_moderna_nota',
        'd_profil_scris_nume',
        'd_alegere_scris_nume',
        'd_competente_digitale',
        None, # media
        'rezultat_final',
        )

    tr2_cols = (
        'd_limba_materna_competente', 'd_limba_materna_scris_nota', 'd_limba_materna_scris_nota_contestatie', 'd_limba_materna_scris_nota_finala',
        'd_profil_scris_nota', 'd_profil_scris_nota_contestatie', 'd_profil_scris_nota_finala',
        'd_alegere_scris_nota', 'd_alegere_scris_nota_contestatie', 'd_alegere_scris_nota_finala'
        )

    @classmethod
    def get_extra_data_from_tr(cls, tr):
        return {'nume': ''.join(cls.xpath_get_nume(tr))}
