
import sys
import curses
import time

from hfilter import translate


def run(stdscr):
    """Curses entry point"""

    max_height, max_width = stdscr.getmaxyx()

    win_status = stdscr.subwin(1, max_width, 0, 0)
    win_status.bkgdset(" ", curses.A_REVERSE)
    win_status.addstr(" " * (max_width - 1))
    win_status.addstr(0, 0, "Status bar goes here")
    win_status.refresh()

    win_input = stdscr.subwin(3, max_width - 1, 1, 0)
    win_input.border()
    win_input.addstr(1, 1, "Input: ")
    win_input.refresh()

    # Use a scrollable 'pad' for output window?
    win_output = stdscr.subwin(max_height - 4, max_width, 4, 0)
    win_output.scrollok(True)
    win_output.idlok(True)
    add_msgs(win_output)

    stdscr.getch()


def add_msgs(win):
    """Add IRC messages to win"""

    for line in open('/home/graham/.hatcog/client_raw.log', 'rt'):
        line = ' '.join(line.split(' ')[3:])
        display = translate(line)
        if not display:
            continue

        win.addstr(display + "\n")
        win.refresh()
        time.sleep(0.1)


def main():
    """Main"""
    curses.wrapper(run)

if __name__ == '__main__':
    sys.exit(main())
