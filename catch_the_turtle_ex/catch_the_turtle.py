import turtle
import random
import time

game_board = turtle.Screen()
game_board.title('Catch The Turtle')
game_board.bgcolor('white')

score_text = 0
score_message = "Score: " + str(score_text)
FONT = ('Arial', 20, 'normal')

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0,game_board.window_height() / 2.3)
score_turtle.write(score_message,align='center',font=FONT)


time_message = 'Time: '

time_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0,game_board.window_height() / 2.6)
score_turtle.write(time_message,align='center',font=FONT)

escape_turtle = turtle.Turtle()
def make_turtle():
    escape_turtle.penup()
    escape_turtle.color('green')
    escape_turtle.shape('turtle')
    escape_turtle.shapesize(2,2)
    escape_turtle.speed(6)
    turtle_move()

def turtle_move():
    escape_turtle.forward(200)
    escape_turtle.right(30)
    escape_turtle.forward(200)

def game_start():
    make_turtle()

game_board.listen()
game_board.onkey(game_start,"space")

turtle.done()