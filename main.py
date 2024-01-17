from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen=Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
board=Scoreboard()

screen.listen()
screen.onkey(snake.down,"s")
screen.onkey(snake.up,"w")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_is_on=True
count=0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        board.increaseScore()
        snake.extend()
    if snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280:
        game_is_on=False
        board.gameover()
    for segment in snake.segment:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<15:
            game_is_on=False
            board.gameover()
screen.exitonclick()