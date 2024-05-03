import curses

def draw_labyrinth(stdscr):
    # Set up initial position and screen
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()
    stdscr.refresh()

    # Define the size of the labyrinth
    height, width = 10, 10
    start_y, start_x = 1, 1  # Start position of the cursor
    end_y, end_x = height - 2, width - 2  # End position (goal)

    # Draw the labyrinth (using '#' for walls)
    labyrinth = [
        "##########",
        "#        #",
        "###      #",
        "#   ######",
        "#   #  # #",
        "### #    #",
        "#   #  # #",
        "# ###  # #",
        "#      # #",
        "##########"
    ]

    # Function to draw the labyrinth on the screen
    def draw():
        for y, line in enumerate(labyrinth):
            for x, char in enumerate(line):
                if (y, x) == (end_y, end_x):
                    stdscr.addstr(y, x, 'E', curses.color_pair(1))  # Draw endpoint with color
                else:
                    stdscr.addch(y, x, char)

    # Function to move the cursor within the boundaries of the labyrinth
    def move_cursor(dy, dx):
        nonlocal start_y, start_x
        new_y, new_x = start_y + dy, start_x + dx

        # Check if the new position is within bounds and not a wall
        if 0 < new_y < height - 1 and 0 < new_x < width - 1 and labyrinth[new_y][new_x] == ' ':
            start_y, start_x = new_y, new_x
    
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Color pair for the endpoint


    # Main game loop
    while True:
        stdscr.clear()
        draw()

        # Draw the cursor
        stdscr.addch(start_y, start_x, '@')

        # Refresh the screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Handle input to move the cursor
        if key == curses.KEY_UP:
            move_cursor(-1, 0)
        elif key == curses.KEY_DOWN:
            move_cursor(1, 0)
        elif key == curses.KEY_LEFT:
            move_cursor(0, -1)
        elif key == curses.KEY_RIGHT:
            move_cursor(0, 1)

        # Check if the player has reached the end
        if start_y == end_y and start_x == end_x:
            # Clear the screen
            stdscr.clear()

            # Display the congratulatory message if screen is large enough
            if height >= 3 and width >= 21:
                stdscr.addstr(height // 2, width // 2 - 10, "Congratulations!")
                stdscr.addstr(height // 2 + 1, width // 2 - 10, "You reached the end of the labyrinth!")
            else:
                stdscr.addstr(0, 0, "Congratulations! You reached the end of the labyrinth!")
            
            stdscr.refresh()
            stdscr.getch()  # Wait for user to press a key before exiting
            break

# Initialize curses and run the game
curses.wrapper(draw_labyrinth)
