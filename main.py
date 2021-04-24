from turtle import Screen,Turtle 
from food import Food
from snake import Snake
from score_board import Score
import time
screen = Screen()
#For the dimensions of the displayed screen 
screen.setup(width=600, height=600) 

#For setting the background color of the screen
screen.bgcolor("black")

screen.title("My snake game")

# To stop the automatic animation of the screen (and basically start 
# the animation only when update() ) we use
screen.tracer(0)

# Initialising the snake object using the Snake class
snake = Snake() 

# listen() is used to set focus in the turtle screen for collecting
# out key events
screen.listen()

#onkey() is used to take set the keyword which will move the object
# with the action of the object intialised inside a fuction
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down",)
screen.onkey(snake.move_right,"Right",)
screen.onkey(snake.move_left,"Left")

food = Food()

score = Score()


game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segment[0].distance(food) <15 :
        food.refresh()
        snake.extend()
        score.score_inc()
    if snake.segment[0].xcor() > 290 or snake.segment[0].xcor() < -290 or snake.segment[0].ycor() > 290 or snake.segment[0].ycor() < -290 :
        game_is_on = False
        score.game_over()
    for seg in snake.segment :
        if seg == snake.segment[0] :
            pass
        elif snake.segment[0].distance(seg) < 10 :
            game_is_on = False
            score.game_over()

screen.exitonclick()