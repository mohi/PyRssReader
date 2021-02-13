PyRssReader
===========

.. image:: https://img.shields.io/pypi/v/PyRssReader.svg
    :target: https://pypi.python.org/pypi/PyRssReader
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/kragniz/cookiecutter-pypackage-minimal.png
   :target: https://travis-ci.org/kragniz/cookiecutter-pypackage-minimal
   :alt: Latest Travis CI build status

Sample RSS Reader to perform multiple text processing on text. Input Read and Output Write supports multiple sources & destinations.

Usage
-----

Sample command

.. code-block::

  python PyRssReader --input http://tech.uzabase.com/ --convert="cut,replace(/base/acid/)" -o tmp.txt

Assumptions
----------
1. Input file articles.txt is a xml file which meets the rss specification
2. URL points to the base url of the RSS feed. RSS feed url can be found out by appending ‘feed/‘
3. CUT function will be applied on the tag ``<title>`` and ``<summary>`` of the rss xml file 
4. REPLACE function will be applied on the text inside the tags ``<title>``, ``<subtitle>``, ``<author>``, ``<content>``, etc  inside of xml file 
   
Installation
------------

Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`PyRssReader` was written by `Mohit Agrawal <mohitleoagrawal@gmail.com>`_.
