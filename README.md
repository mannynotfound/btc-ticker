# clockr
[![Build Status](https://travis-ci.org/shaggytwodope/clockr.svg)](https://travis-ci.org/shaggytwodope/clockr)

clockr is a collaborative effort at a simple curses clock written in Python 3.

# Screenshot
![clockr](http://i.imgur.com/gNyIXlX.png)


# Installation
* Arch Linux: clockr in the AUR
* pip: clockr

For manual installation, clone the repository, cd into it and run
```
# python setup.py install
```


# Options

usage: clockr [−h] [−V] [−c COLOR] [−d DATEFORMAT] [−n] [−t]

**optional arguments: 
−h**, **−−help**

show this help message and exit

**−V**, **−v**, **−−version**

show program’s version number and exit

**−c** COLOR, **−−color** COLOR

changes color of the clock.

**−d** DATEFORMAT, **−−dateformat** DATEFORMAT

changes the format in which the date is printed, see ’man date’ for support on formats. Not to be combined with the ’−−nodate’−argument.

**−n**, **−−nodate**

does not print the date in the clock

**−t**, **−−twentyfourhours**

prints the time in 24−hour format


# Examples

**clockr −−nodate −−twentyfourhours −−color** _white_

Will display a white-colored 24-hour clock while omitting the date.

The different colors avaialable are,

_white red green yellow blue magenta cyan orange_

And you can also use _random_ to chose a random color.



# FAQ
Q: Can you add [feature]? When will [bug] be fixed?

A: This project is completely run by volunteers and will most likely never be 100% bug-free as developers are humans too. You can help out yourself, though, by submitting a bug report!

# Thanks and Authors
Made with help from #linuxmasterrace on Snoonet thanks to n473, thimoteus, AWindowsKrill, timawesomeness, calexil, tirkaz and somehow R0flcopt3r, with additional help from bdalenoord and Noremac201.
