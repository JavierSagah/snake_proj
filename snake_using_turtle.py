import os
import turtle
import time
from random import randrange

score = 0

# set up the window screen
win = turtle.Screen()
win.title("My Snake Game")
# rows was 20, so here will be 400; cols was 60 so here will be 1200; from 1x1 pixels to 20x20 pixels
win.setup(width=600, height=600)
# supposedly this allows our game to go faster by preventing the window to update itself, it only updates when we say so
win.tracer(0)

# the snake: the snake will be an array of turtles; the snake will start with 3 turtles as its body
snake = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
for i in range(len(snake)):
    snake[i].speed(0)  # sets the speed of animation to maximum possible speed
    snake[i].shape("square")  # give a shape to the turtle, by default it is an arrow and has dimensions 20x20 pixels
    snake[i].color("green")
    snake[i].penup()  # prevent the turtle from drawing while moving
    snake[i].goto(x=-250 - i * 20, y=100)  # setting starting position of our snake, i=0 is the head
head = snake[0]
head.color("brown")

# the food
food = turtle.Turtle()
food.speed(0)  # sets the speed of animation to maximum possible speed
food.shape("circle")  # give a shape to the turtle, by default it is an arrow and has dimensions 20x20 pixels
food.color("red")
food.penup()  # prevent the turtle from drawing while moving
# food.shapesize(0.5, 0.5)

# A pen turtle to draw a score message
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 280)
pen.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))


# functions

def up():
    # The snake cannot go right from left, left from right, top from down and down from the top.
    if snake[0].heading() != 270:
        # Now changing the direction of the head accordingly
        snake[0].setheading(90)


def down():
    # The snake cannot go right from left, left from right, top from down and down from the top.
    if head.heading() != 90:
        # Now changing the direction of the head accordingly
        head.setheading(270)


def right():
    # The snake cannot go right from left, left from right, top from down and down from the top.
    if head.heading() != 180:
        # Now changing the direction of the head accordingly
        head.setheading(0)


def left():
    # The snake cannot go right from left, left from right, top from down and down from the top.
    if head.heading() != 0:
        # Now changing the direction of the head accordingly
        head.setheading(180)


def move():
    # move the head 20 pixels in the direction it is pointing
    head.forward(20)


# game logic
# allow the window listen for input keyboard or mouse
win.listen()
# binding the movement functions to the key from the keyboard
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(right, "Right")
win.onkeypress(left, "Left")

while True:
    win.update()

    # move the body first segment by segment from tail to neck
    for seg in range(len(snake) - 1, 0, -1):
        x = snake[seg - 1].xcor()
        y = snake[seg - 1].ycor()
        snake[seg].goto(x, y)
    # now move the head
    move()

    # check if snake hist the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        break

    # check if snake hits itself
    body_collision = False
    for segment in snake[4:]:
        if segment.distance(head) < 20:
            body_collision = True
    if body_collision:
        break

    # check if snake reached the food
    if head.distance(food) < 20:
        # play sound when it eats the food:
        # on MAC we use os.system and the afplay, on linux is aplay,
        # on windows use winsound.playSound("bounce.wav", winsound.SND_ASYNC)
        # the game pauses for the sound to be reproduced, to avoid this, add & at the end of the wav file name
        os.system("afplay bounce.wav")
        score += 1
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 18, "normal"))
        new_segment = turtle.Turtle()
        new_segment.penup()  # prevent the turtle from drawing while moving
        new_segment.goto(0,1000)
        new_segment.speed(0)  # sets the speed of animation to maximum possible speed
        new_segment.shape("square")
        new_segment.color("green")
        snake.append(new_segment)
        # move the food somewhere else considering the alignment with the snake paths, 20x20 and not just any x and y
        # food.goto(randint(-290, 290), randint(-290, 290))
        food.goto(randrange(-280, 280, 20), randrange(-280, 280, 20))

    # creating a sleep time between each update (for each loop) to slow down the speed of the game
    time.sleep(0.2)

print("Final score: ", score)
