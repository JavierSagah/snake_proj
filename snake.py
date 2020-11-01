# curses is Mac only
import curses
from random import randint

# setup window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)  # rows, cols, starting coords x,y although here is y,x in curses
# use arrow keys
win.keypad(True)
# do not want to listen to other keys
curses.noecho()
# hide the cursor
curses.curs_set(0)
# draw a border
win.border(0)
# we do not want to wait for the next user input, so if not event we use -1, if event then 1
win.nodelay(True)

# snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)

# game logic
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)  # increase speed

    prev_key = key
    # event gets the next character
    event = win.getch()
    key = event if event != -1 else prev_key

    # moving the snake by calculate the next coordinates for the head
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_RIGHT:
        x += 1
    if key == curses.KEY_LEFT:
        x -= 1

    # actually moving the snake by adding the new coordinates for the head based on the last pressed key
    # and shifting right the other coordinates
    snake.insert(0, (y, x))  # this is sadly O(n) can probably be improved
    # remove the tail to keep the proper length of the snake
    tail = snake.pop()
    win.addch(tail[0], tail[1], ' ')

    # check if snake hits the border
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    # check if snake hit itself
    if snake[0] in snake[4:]: break     # the head of the snake can only hit from the fifth * down
    # a minimum of 5 stars are needed in the snake including its head for this to be possible to happen

    # check if snake reached the food
    if snake[0] == food:
        # eat it, meaning: increase the score, delete the food and put a new one somewhere else, grow snake
        # increase score
        score += 1
        # grow the snake
        snake.append(food)
        # set a new food
        food = (randint(1,18), randint(1,58))
        # win.addch(food[0], food[1], '#')

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # visually moving the snakes body
    for c in snake:
        win.addch(c[0], c[1], '*')

    # visually setting the food into the grid
    win.addch(food[0], food[1], '#')

# destroy the window
curses.endwin()
print("Final score: ", score)
