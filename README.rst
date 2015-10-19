clockr
======

|Build Status| |pypi| |python| |downloads|

clockr is a collaborative effort at a simple curses clock written in
Python 3.

Reviews
=======

`Video by Yu-Jie Lin`_

-  A harsh critique, but the video nicely shows clockr.

Screenshot
==========

.. figure:: http://i.imgur.com/gNyIXlX.png
   :alt: clockr

   clockr

Installation
============

-  Arch Linux: clockr in the AUR
-  pip: clockr

For manual installation, clone the repository, cd into it and run

::

    # python setup.py install

Options
=======

usage: clockr [−h] [−V] [−c COLOR] [−d DATEFORMAT] [−n] [−t]

**optional arguments: −h**, **−−help**

show this help message and exit

**−V**, **−v**, **−−version**

show program’s version number and exit

**−c** COLOR, **−−color** COLOR

changes color of the clock.

**−d** DATEFORMAT, **−−dateformat** DATEFORMAT

changes the format in which the date is printed, see ’man date’ for
support on formats. Not to be combined with the ’−−nodate’−argument.

**−n**, **−−nodate**

does not print the date in the clock

**−t**, **−−twentyfourhours**

prints the time in 24−hour format

Examples
========

**clockr −−nodate −−twentyfourhours −−color** *white*

Will display a white-colored 24-hour clock while omitting the date.

The different colors avaialable are,

*white red green yellow blue magenta cyan orange*

And you can also use *random* to chose a random color.

FAQ
===

Q: Can you add [feature]? When will [bug] be fixed?

A: This project is completely run by volunteers and will most likely
never be 100% bug-free as developers are humans too. You can help out
yourself, though, by submitting a bug report!

Thanks and Authors
==================

Made with help from #linuxmasterrace on Snoonet thanks to n473,
thimoteus, AWindowsKrill, timawesomeness, calexil, tirkaz and somehow
R0flcopt3r, with additional help from bdalenoord and Noremac201.

.. _Video by Yu-Jie Lin: https://www.youtube.com/watch?v=P3rv3rS40Ls

.. |Build Status| image:: https://travis-ci.org/shaggytwodope/clockr.svg
   :target: https://travis-ci.org/shaggytwodope/clockr
   :alt: Build status

.. |python| image:: https://img.shields.io/badge/python-3.5-blue.svg?style=flat
    :target: https://pypi.python.org/pypi/clockr/
    :alt: Supported Python versions

.. |pypi| image:: https://img.shields.io/pypi/v/clockr.svg?label=version&style=flat
    :target: https://pypi.python.org/pypi/clockr/
    :alt: Latest Version

.. |downloads| image:: https://img.shields.io/pypi/dm/clockr.svg?period=month&style=flat
    :target: https://pypi.python.org/pypi/clockr/
    :alt: Downloads
