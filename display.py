import curses

screen = curses.initscr()

num_lines = curses.LINES
num_cols = curses.COLS

# Update the buffer, adding text at different locations
for line in range(1,6):
    screen.addstr(num_lines - 6 + line, 1, "Sensor " + str(line) + ": ", curses.A_BOLD)
    


# Changes go in to the screen buffer and only get
# displayed after calling `refresh()` to update
screen.refresh()

curses.napms(3000)
curses.endwin()