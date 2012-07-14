r"""Emulates the ``ged`` JavaScript function from some HTML pages

  "{yo,sup} dawg, I herd you like X, so I put an X in your Y so you can VERB
  while you VERB"

  -- Xzibit

Siveco must really like the `Xzibit Yo Dawg meme`_ because they have a
JavaScript function named ``ged`` that returns an HTML page which contains the
results. This module emulates that functionmooooooooooosome.

.. _Xzibit Yo Dawg meme: http://knowyourmeme.com/memes/xzibit-yo-dawg
"""

__docformat__ = "restructuredtext en"

import re
import sys

from . import maintimeline

js_ged_regex = re.compile(r'''function\s+ged\(\)\s*{\s*return\s+"([^"]*)"\s*;\s*}''')

def get_inner_html(line):
    """Return the value of the ``ged`` JavaScript function"""
    global js_ged_regex
    ged = js_ged_regex.search(line)
    if not ged:
        return None
    return maintimeline.s3(ged.group(1)).decode('base64')

def main():
    for line in sys.stdin:
        html = get_inner_html(line)
        if html:
            sys.stdout.write(html)

if __name__ == '__main__':
    main()
