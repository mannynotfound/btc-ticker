#!/usr/bin/python3
# -*- coding: utf-8 -*-
import curses
from math import floor
from datetime import datetime as date
import sys
import time
import argparse
import signal
import random
from .__version__ import __version__


def get_args():
    """get all args"""
    parser = argparse.ArgumentParser(
        description='Simple curses clock written in Python.\n\
                Press q to exit.',
        epilog="Made with help from #linuxmasterrace on Snoonet thanks to n473,\
                thimoteus, AWindowsKrill, timawesomeness, calexil, tirkaz \
                and somehow R0flcopt3r, with additional help from bdalenoord \
                and Noremac201.")
    parser.add_argument('-V', '-v', '--version', action='version',
                        version='%(prog)s ' + __version__)
    parser.add_argument(
        '-c', '--color', type=str, help='changes color of the clock.',
        required=False)
    parser.add_argument(
        '-d', '--dateformat', type=str, help='changes the format in which the \
                date is printed, see \'man date\' for support on formats. \
                Not to be combined with the \'--nodate\'-argument.',
        required=False, default=None)
    parser.add_argument(
        '-n', '--nodate', action='store_true', help='does not print the date \
                in the clock', required=False)
    parser.add_argument(
        '-t', '--twentyfourhours', action='store_true', help='prints the time \
                in 24-hour format', required=False, default=None)
    args = parser.parse_args()
    color = args.color
    dateformat = args.dateformat
    nodate = args.nodate
    twentyfourhourarg = args.twentyfourhours
    conflictdate = args.dateformat, args.nodate
    if all(conflictdate):
        sys.exit('Conflict in options: can not use \
                nodate option with dateformat.')
    return color, dateformat, nodate, twentyfourhourarg

color, dateformat, nodate, twentyfourhourarg = get_args()


screen = curses.initscr()
width = 0
height = 0
origin_x = 0
origin_y = 0
glyph = {
    '0': ["  #####   ", " ##   ##  ", "##     ## ", "##     ## ", "##     ## ",
          " ##   ##  ", "  #####   "],
    '1': ["    ##    ", "  ####    ", "    ##    ", "    ##    ", "    ##    ",
          "    ##    ", "  ######  "],
    '2': [" #######  ", "##     ## ", "       ## ", " #######  ", "##        ",
          "##        ", "######### "],
    '3': [" #######  ", "##     ## ", "       ## ", " #######  ", "       ## ",
          "##     ## ", " #######  "],
    '4': ["##        ", "##    ##  ", "##    ##  ", "##    ##  ", "######### ",
          "      ##  ", "      ##  "],
    '5': [" ######## ", " ##       ", " ##       ", " #######  ", "       ## ",
          " ##    ## ", "  ######  "],
    '6': [" #######  ", "##     ## ", "##        ", "########  ", "##     ## ",
          "##     ## ", " #######  "],
    '7': [" ######## ", " ##    ## ", "     ##   ", "    ##    ", "   ##     ",
          "   ##     ", "   ##     "],
    '8': [" #######  ", "##     ## ", "##     ## ", " #######  ", "##     ## ",
          "##     ## ", " #######  "],
    '9': [" #######  ", "##     ## ", "##     ## ", " ######## ", "       ## ",
          "##     ## ", " #######  "],
    ':': ["   ", "   ", " # ", "   ", " # ", "   ", "   "]
}


def getcolor():
    """color selection"""
    colors = {
        "red": 1,
        "green": 2,
        "yellow": 3,
        "blue": 4,
        "magenta": 5,
        "cyan": 6,
        "white": 7,
        "orange": 9,
        "random": random.randint(1, 255)
    }

    if color is not None and color.lower() in colors.keys():
        curses.init_pair(1, 0, -1)
        curses.init_pair(2, colors[color], -1)
        curses.init_pair(3, 0, colors[color])
    else:
        pass


def addstr(y, x, string, color):
    try:
        screen.addstr(origin_y + y, origin_x + x, string, color)
        screen.refresh()
    except:
        return


def print_time(now):
    """main time function"""
    twentyfourhours = twentyfourhourarg
    time_line = now.strftime("%H:%M:%S" if twentyfourhours else "%I:%M:%S")
    time_array = ["" for i in range(0, 7)]

    for char in time_line:
        char_array = glyph[char]
        for row in range(0, len(char_array)):
            time_array[row] += char_array[row]

    for y in range(0, len(time_array)):
        for x in range(0, len(time_array[y])):
            char = time_array[y][x]
            color = 1 if char == " " else 3

            # If we run in 24-hour mode, the AM/PM will be omitted.
            # This then leads to a misaligned clock, thus
            # we need to move the clock to the right 2 columns
            addstr(y, x if not twentyfourhours else x + 2, " ",
                   curses.color_pair(color))

    if not twentyfourhours:
        addstr(6, len(time_array[0]), now.strftime("%p"),
               curses.color_pair(2) | curses.A_BOLD)


def print_date(now):
    """main date function"""
    day_line = now.strftime("%A").center(11, " ")
    date_line = now.strftime("%B %d, %Y") if not dateformat \
        else now.strftime(dateformat)
    if nodate:
        pass
    else:
        addstr(8, 0, day_line, curses.color_pair(2))
        addstr(8, len(day_line) + 40, date_line,
               curses.color_pair(2) | curses.A_BOLD)


def gracefull_exit(signal=None):
    """exit with grace, prevents a messed up terminal"""
    curses.endwin()
    sys.exit()


def win_resize():
    """window resize function"""
    global width, height, origin_x, origin_y, last_t
    screen.clear()
    height, width = screen.getmaxyx()
    origin_x = floor(width / 2) - 34
    origin_y = floor(height / 2) - 4
    last_t = None

screen.keypad(1)
curses.curs_set(0)
curses.start_color()
curses.use_default_colors()
# if no arguments use these values
curses.init_pair(1, 0, -1)
curses.init_pair(2, 5, -1)
curses.init_pair(3, 0, 5)
curses.noecho()
curses.cbreak()
screen.timeout(0)

# Register signal handlers for graceful exit on for instance CTRL-C
signal.signal(signal.SIGINT, gracefull_exit)
signal.signal(signal.SIGTERM, gracefull_exit)


def main():
    """lets run this thing"""
a = 0
getcolor()
win_resize()
while True:
    char = screen.getch()
    if char == curses.KEY_RESIZE:
        win_resize()
    elif char in (ord('q'), ord('Q')):
        break

    now = date.now()
    if last_t and now.timetuple()[:6] != last_t.timetuple()[:6]:
        print_time(now)
        print_date(now)

    time.sleep(0.01)
    last_t = now

gracefull_exit()


if __name__ == '__main__':
    main()
