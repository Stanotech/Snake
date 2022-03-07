from turtle import Screen
from snake import Snake
from food import Food
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

def up():
    snake.direction = "up"

def down():
    snake.direction = "down"

def right():
    snake.direction = "right"

def left():
    snake.direction = "left"

snake = Snake()
food = Food()
score = 0
grow = False

game_on = True
screen.listen()
while game_on:
    screen.update()
    time.sleep(0.2)
    screen.onkey(up, "w")
    screen.onkey(down, "s")
    screen.onkey(right, "d")
    screen.onkey(left, "a")
    screen.update()

    snake.move(grow)
    grow = False

    if snake.segments[len(snake.segments) - 1].pos() == food.pos():
        print("jam jam")
        food.setpos(21 * random.randint(-10, 10), 21 * random.randint(-10, 10))
        score += 1
        print(score)
        grow = True
