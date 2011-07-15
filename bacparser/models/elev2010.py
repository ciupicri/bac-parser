'''Model from the year 2010 onwards'''
import collections

Elev = collections.namedtuple('Elev',
        ('nume',
         'scoala',
         'judet',
         'promotie_anterioara',
         'forma_invatamant',
         'specializare',
         'd_romana_competente',
         'd_romana_scris_nota', 'd_romana_scris_nota_contestatie', 'd_romana_scris_nota_finala',
         'd_limba_materna_nume',
         'd_limba_materna_competente',
         'd_limba_materna_scris_nota', 'd_limba_materna_scris_nota_contestatie', 'd_limba_materna_scris_nota_finala',
         'd_limba_moderna_nume', 'd_limba_moderna_nota',
         'd_profil_scris_nume', 'd_profil_scris_nota', 'd_profil_scris_nota_contestatie', 'd_profil_scris_nota_finala',
         'd_alegere_scris_nume', 'd_alegere_scris_nota', 'd_alegere_scris_nota_contestatie', 'd_alegere_scris_nota_finala',
         'd_competente_digitale',
         'rezultat_final',
        )
    )
