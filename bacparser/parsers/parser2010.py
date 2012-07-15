import logging

from .ged import get_inner_html
from .parser2009 import Parser2009
from ..models import elev2010

class Parser2010(Parser2009):
    """Parser for the year 2010 onwards"""

    _logger = logging.getLogger(__name__ + '.' + 'Parser2010')

    Elev = elev2010.Elev

    tr1_cols = (
        None, # Nr. crt.
        None, # Nume... <script>
        None, # Pozitia in ierarhie...
        None, # Pozitia in ierarhie...
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
        None, # LuatDePe_Bac...
        None, # Luat_DePe_Bac...
        )

    tr2_cols = (
        'd_limba_materna_competente', 'd_limba_materna_scris_nota', 'd_limba_materna_scris_nota_contestatie', 'd_limba_materna_scris_nota_finala',
        'd_profil_scris_nota', 'd_profil_scris_nota_contestatie', 'd_profil_scris_nota_finala',
        'd_alegere_scris_nota', 'd_alegere_scris_nota_contestatie', 'd_alegere_scris_nota_finala'
        )

    @classmethod
    def data_from_tr_filter(cls, s):
        return s.replace('&nbsp', '').strip()

    @classmethod
    def get_extra_data_from_tr(cls, tr):
        items = cls.get_luat_de_pe_bacalaureat(tr)
        return {
            'nume': items[0][0].replace('<br>', ''),
            'rezultat_final': items[2][1]}


    @classmethod
    def get_main_table_from_file(cls, f):
        """Return the mainTable table from file f while taking care of all the
        obfuscation and garbage.
        """

        for line in f:
            html = get_inner_html(line)
            if html:
                break
        else:
            return None
        html = html[html.index('<HTML>'):] # remove leading garbage
        return cls.get_main_table_from_html(html)
