This is a scraping script for extracting the results of the
[Romanian Baccalaureate][bac] from http://bacalaureat.edu.ro for the years
2006 - 2011.

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


Copyright and License
=====================

The code is too simple and too ugly to require legal paperwork, so I declare
it public domain.


Credits
=======

This wouldn't have been possible without the [Sothink SWF Decompiler]. Shame on
Siveco for using Flash even if it wasn't really needed.

[Sothink SWF Decompiler]: http://www.sothink.com/product/flashdecompiler/
