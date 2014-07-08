This is a scraping script for extracting the results of the
[Romanian Baccalaureate][bac] from http://bacalaureat.edu.ro for the years
2006 - 2014.

[bac]: http://en.wikipedia.org/wiki/Romanian_Baccalaureate

Installation and Requirements
=============================

 - python 2.7
 - [python-lxml](http://lxml.de/)
 - [PylibLZMA](https://launchpad.net/pyliblzma) (for LZMA/XZ compressed files)
 - python-argparse (on Python 2.6)

Fedora 15
---------

    yum install python-lxml pyliblzma

Enterprise Linux 6
------------------

    yum install python-lxml pyliblzma python-argparse


Usage
=====

First you need to get the HTML pages that will be parsed. You can download them
with a browser or you can use a spider, whatever fits you. Then you can parse
them.


Basic usage
-----------

    ./main.py data/alfabetic_page_4.html

outputs:

    Elev(nume=u'John Doe', scoala=u'Summer school', judet=u'B', promotie_anterioara=u'NU', forma_invatamant=u'Zi', specializare=u'Tehnician in activitati economice', d_romana_competente=u'Utilizator avansat', d_romana_scris_nota=u'5.45', d_romana_scris_nota_contestatie=u'', d_romana_scris_nota_finala=u'5.45', d_limba_materna_nume=u'', d_limba_materna_competente=u'', d_limba_materna_scris_nota=u'', d_limba_materna_scris_nota_contestatie=u'', d_limba_materna_scris_nota_finala=u'', d_limba_moderna_nume=u'Limba engleza', d_limba_moderna_nota=u'B2-A2-B2-B1-B1', d_profil_scris_nume=u'Matematica T2', d_profil_scris_nota=u'5', d_profil_scris_nota_contestatie=u'', d_profil_scris_nota_finala=u'5', d_alegere_scris_nume=u'Economie', d_alegere_scris_nota=u'8.05', d_alegere_scris_nota_contestatie=u'', d_alegere_scris_nota_finala=u'8.05', d_competente_digitale=u'Utilizator experimentat', rezultat_final=u'Reu\u015fit')
    #######################################################################
    ...
    #######################################################################
    Elev(nume=u'Joahna Doe', scoala=u'Winter school', judet=u'B', promotie_anterioara=u'NU', forma_invatamant=u'Zi', specializare=u'Tehnician in activitati economice', d_romana_competente=u'Utilizator avansat', d_romana_scris_nota=u'5.45', d_romana_scris_nota_contestatie=u'', d_romana_scris_nota_finala=u'5.45', d_limba_materna_nume=u'', d_limba_materna_competente=u'', d_limba_materna_scris_nota=u'', d_limba_materna_scris_nota_contestatie=u'', d_limba_materna_scris_nota_finala=u'', d_limba_moderna_nume=u'Limba engleza', d_limba_moderna_nota=u'B2-A2-B2-B1-B1', d_profil_scris_nume=u'Matematica T2', d_profil_scris_nota=u'5', d_profil_scris_nota_contestatie=u'', d_profil_scris_nota_finala=u'5', d_alegere_scris_nume=u'Economie', d_alegere_scris_nota=u'8.05', d_alegere_scris_nota_contestatie=u'', d_alegere_scris_nota_finala=u'8.05', d_competente_digitale=u'Utilizator experimentat', rezultat_final=u'Reu\u015fit')

You can parse multiple files in one run. In order to save disk space, reading
from compressed files is supported (formats: gzip, bzip2, lzma/xz).

You can specify the year of the exam with the `--year` parameter. By the
default it's the last year supported.

Other output formats
--------------------

If you're planning to analyze the results, you can dump them in the
**[pickle]** format. Then either read the pickle file from Python or convert it
to a **CSV** file using `pickle2csv.py`. From there on, the sky's the limit.
Here's an example:

    ./main.py --format pickle data/alfabetic_page_4.html.xz | xz --best > results.pickle.xz
    ./pickle2csv.py results.pickle.xz > results.csv

The pickle file is actually composed of multiple pickle dumps in order to
minimize the memory usage, so you'll need to load pickles from it until `EOF`.

As you can see, `pickle2csv` supports compressed files, too.

The `--year` parameter works in the same way as for `main`.

If you don't need the pickle files, you can do it in a single step:

    ./main.py --format pickle data/alfabetic_page_4.html.xz | ./pickle2csv.py - > results.csv

[pickle]: http://docs.python.org/library/pickle.html

Spiders
-------

Here's a list of software you might find useful for downloading the pages:

 * [bac-spider](https://github.com/ciupicri/bac-spider) - the spider I used to
   get the results for years 2006 - 2011
 * [bac-spider-2012](https://github.com/diana-coman/bac-spider-2012) - a
   spider for getting the results for year 2012


Why?
====

When talking about this national exam, most Romanian TV shows and newspaper
articles mention only stuff like only p% have passed it, N pupils managed to
get a maxim score or they point to high-schools where everyone failed. But
things were about to change in the summer of 2011. A friend of mine, [Diana
Coman] wanted more than just press reports, she wanted to do a statistical
analysis of the data.

Unfortunately the data is available only in the form of HTML pages which might
look nice, but they're useless when it comes to statistics (she mentioned this
in the article ["Bac Data"][DC-bac-data]). So she started writing a scraping
script. After noticing that it was harder than she though because the pages
were a bit obfuscated, she asked for my help so she could analyze the data
while it was still hot. I managed to write something that did the job, but it
was ugly just like the HTML pages. After she asked for the data from previous
years as well, I decided to start *almost* from scratch and you can see the
result here. The old code is in the [bac-parser.old] repository and it's not
for the faint of the heart. As for the analysis, Diana's first article was a
top of the cheaters that were caught - ["Topul hoților (prinși) la Bacalaureat
2011"][DC-top].

[Diana Coman]: http://www.dianacoman.com
[DC-bac-data]: http://www.dianacoman.com/bac-data/
[bac-parser.old]: https://github.com/ciupicri/bac-parser.old
[DC-top]: http://www.dianacoman.com/blog/2011/07/09/topul-hotiei-dovedite-la-bacalaureat-2011/


Copyright and License
=====================

The code is too simple and too ugly to require legal paperwork, so I declare
it public domain.


Credits
=======

This wouldn't have been possible without the [Sothink SWF Decompiler]. Shame on
Siveco for using Flash even if it wasn't really needed.

[Sothink SWF Decompiler]: http://www.sothink.com/product/flashdecompiler/
