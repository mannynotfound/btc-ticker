#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import curses
from math import floor
from datetime import datetime as date
import sys
import time
import signal
from exchanges.bitfinex import Bitfinex

last_price = 0

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


def addstr(y, x, string, color):
    try:
        screen.addstr(origin_y + y, origin_x + x, string, color)
        screen.refresh()
    except:
        return


def print_price(now):
    global last_price
    """main price function"""
    try:
        price = Bitfinex().get_current_price()
    except Exception as e:
        return

    price = int(round(price))
    tick_color = 4 if price >= last_price else 2
    usd_color = 5 if price >= last_price else 3
    last_price = price

    time_line = str(price)
    time_array = ["" for i in range(0, 7)]

    for char in time_line:
        char_array = glyph[char]
        for row in range(0, len(char_array)):
            time_array[row] += char_array[row]

    total_x = 65
    offset_x = int(round((total_x - len(time_array[0])) / 2))

    for y in range(0, len(time_array)):
        for x in range(0, len(time_array[y])):
            char = time_array[y][x]
            color = 1 if char == " " else tick_color

            addstr(y, x + offset_x, " ", curses.color_pair(color))

    addstr(6, offset_x + len(time_array[0]), 'USD', curses.color_pair(usd_color))


def print_date(now):
    """main date function"""
    day_line = now.strftime("%A").center(11, " ")
    date_line = now.strftime("%B %d, %Y")

    addstr(8, 0, day_line, curses.color_pair(0))
    addstr(8, len(day_line) + 40, date_line, curses.color_pair(0))


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
# init curses color pairs
curses.init_pair(1, 0, -1)
# black on red
curses.init_pair(2, 0, 1)
# red on black
curses.init_pair(3, 1, 0)
# black on green
curses.init_pair(4, 0, 2)
# green on black
curses.init_pair(5, 2, 0)

curses.noecho()
curses.cbreak()
screen.timeout(0)

# Register signal handlers for graceful exit on for instance CTRL-C
signal.signal(signal.SIGINT, gracefull_exit)
signal.signal(signal.SIGTERM, gracefull_exit)


def main():
    """lets run this thing"""

a = 0
win_resize()
now = date.now()
print_price(now)
print_date(now)

while True:
    char = screen.getch()
    if char == curses.KEY_RESIZE:
        win_resize()
    elif char in (ord('q'), ord('Q')):
        break

    now = date.now()
    if last_t and now.timetuple()[:6] != last_t.timetuple()[:6]:
        print_price(now)
        print_date(now)

    time.sleep(15)
    last_t = now

gracefull_exit()


if __name__ == '__main__':
    main()
