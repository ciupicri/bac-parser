import lxml.etree
import lxml.html
import sys

def get_main_table(html):
    """ -> the mainTable table"""
    html = html[html.index('<HTML>'):]
    html = unicode(html, 'utf-8')
    doc = lxml.html.fromstring(html)
    main_table = doc.xpath(r'//table[@id="mainTable"]')[0]
    return main_table

def main(f):
    with f:
        html = f.read()
        main_table = get_main_table(html)
        sys.stdout.write(lxml.etree.tostring(main_table, pretty_print=True))

if __name__ == '__main__':
    main(sys.stdin)
