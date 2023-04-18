import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor('white')
drawing_board.title('Drawing Board')

turtle_instance = turtle.Turtle()
turtle_instance2 = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def turtle_angle_right():
    turtle_instance.right(10)

def turtle_angle_left():
    turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_origin():
    turtle_instance.home()

def turtle_pen_down():
    turtle_instance.pendown()

def turtle_pen_up():
    turtle_instance.penup()



drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=turtle_angle_right,key="Down")
drawing_board.onkey(fun=turtle_angle_left,key="Up")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=turtle_return_origin,key="o")
drawing_board.onkey(fun=turtle_pen_down,key="w")
drawing_board.onkey(fun=turtle_pen_up,key="q")



"""
turtle_colors = ['red','brown','purple','yellow','blue','green','orange']

num_sides = 4
angle = 360.0 / num_sides
side_length = 100

turtle_instance.speed(0)


for i in range(len(turtle_colors)):
    turtle_instance.color(turtle_colors[i % 7])
    turtle_instance.circle(30 * i)
    turtle_instance.circle(-30 * i)
    turtle_instance.left(i)
"""
"""
def shrinkingSquare(size):
    for i in range(num_sides):
        turtle_instance.forward(size)
        turtle_instance.left(angle)
        size = size - 5

shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(70)
shrinkingSquare(50)
shrinkingSquare(30)
"""
"""
for i in range(num_sides):
    turtle_instance2.forward(side_length)
    turtle_instance2.right(angle)
"""
#for i in range(5):
#    turtle_instance.forward(angle)
#    turtle_instance.left(side_length)



turtle.done()