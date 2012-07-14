__docformat__ = "restructuredtext en"

import lxml.etree
import lxml.html
import sys

from .ged import get_inner_html

def get_main_table(html, year):
    """Return the mainTable table, the one containing the results"""
    html = unicode(html, 'utf-8')
    doc = lxml.html.fromstring(html)
    if year <= 2011:
        return doc.xpath(r'//table[@id="mainTable"]')[0]
    else:
        return doc.xpath(r'//table[@class="mainTable"]')[0]

def get_main_table_from_file(f, year):
    """Return the ``mainTable`` table from file ``f`` for year ``year`` while
        taking care of all the obfuscation and garbage.
    """

    if year <= 2011:
        if year <= 2009:
            html = f.read()
        else: # Siveco's HTML inside HTML
            for line in f:
                html = get_inner_html(line)
                if html:
                    break
            else:
                return None
        html = html[html.index('<HTML>'):] # remove leading garbage
    else: # finally a plain HTML
        html = f.read()
    return get_main_table(html, year)

def main(f, year):
    with f:
        html = f.read()
        main_table = get_main_table(html)
        sys.stdout.write(lxml.etree.tostring(main_table, pretty_print=True))

if __name__ == '__main__':
    main(sys.stdin, int(sys.argv[1]))
