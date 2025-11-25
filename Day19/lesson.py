from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(18)
    
def move_backwards():
    t.backward(30)


def move_counter():
    t.left(90)
    

def move_clock():
    t.right(90)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
    
# screen.onkey(key="space", fun=move_forwards)
 
# etch a sketch
# w = forwards

screen.onkey(key="w", fun=move_forwards)
# s = backwards
screen.onkey(key="s", fun=move_backwards)
# a = counter-clockwise
screen.onkey(key="a", fun=move_counter)
# d = clockwise
screen.onkey(key="d", fun=move_clock)
# c = clear drawing
screen.onkey(key='c', fun=clear)







screen.exitonclick()