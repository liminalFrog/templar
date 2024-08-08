import os
import sys
import time
import curses
import argparse
import pytesseract
import cv2

#splash = ' _____             _     _           \n| __  |___ ___ ___|_|___| |_ ___ ___ \n|    -| -_|  _| -_| | . |  _| . |  _|\n|__|__|___|___|___|_|  _|_| |___|_|  \n                    |_|              \n'
splash = '╔──────────────────────────────────────╗\n│  ___ ____ _  _ ___  _    ____ ____   │\n│   |  |___ |\/| |__] |    |__| |__/   │\n│   |  |___ |  | |    |___ |  | |  \   │\n│                                      │\n╚─────────╔─────────────────╗──────────╝\n          │ RECEIPT SCANNER │           \n          ╚─────────────────╝           \n                                        \n'

parser = argparse.ArgumentParser()
parser.add_argument('--image', '-i', required=True, help="Image to read")
args = vars(parser.parse_args())

def main(stdscr):

  curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  BLACK_ON_WHITE = curses.color_pair(1)
  curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
  GREEN = curses.color_pair(2)
  curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
  MAGENTA = curses.color_pair(3)
  curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
  BLUE = curses.color_pair(4)
  curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
  RED = curses.color_pair(5)

  stdscr.clear()
  
  stdscr.addstr(splash, GREEN)
  stdscr.addstr(6,12,"RECEIPT SCANNER", MAGENTA)
  stdscr.addstr(6, 30, 'v 1.0.0', BLUE)
  stdscr.addstr("\n")
  
  image = cv2.imread(args["image"])
  rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  try:
    text = pytesseract.image_to_string(rgb)
  except:
    text = 'Error'

  stdscr.addstr(8, 0, "Image received\n=======\n")
  for line in text.splitlines():
    stdscr.addstr(line)
    stdscr.addstr('\n')
  stdscr.addstr("\n=======")

  quitApp = False
  while quitApp == False:
    k = stdscr.getkey()
    if k != "q":
      msg = "You pressed the " + k + " key."
      stdscr.addstr(8, 0, msg)
      stdscr.refresh()
    else:
      quitApp = True

curses.wrapper(main)