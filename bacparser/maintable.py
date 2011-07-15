import lxml.etree
import lxml.html
import sys

from .ged import get_inner_html

def get_main_table(html):
    """ -> the mainTable table"""
    html = html[html.index('<HTML>'):]
    html = unicode(html, 'utf-8')
    doc = lxml.html.fromstring(html)
    main_table = doc.xpath(r'//table[@id="mainTable"]')[0]
    return main_table

def get_main_table_from_file(f, year):
    """ -> the mainTable table from a file"""
    if year <= 2009:
        html = f.read()
    else:
        for line in f:
            html = get_inner_html(line)
            if html:
                break
        else:
            return None
    return get_main_table(html)

def main(f):
    with f:
        html = f.read()
        main_table = get_main_table(html)
        sys.stdout.write(lxml.etree.tostring(main_table, pretty_print=True))

if __name__ == '__main__':
    main(sys.stdin)
