# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color('green')

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)


# screen = Screen()
# screen.exitonclick()

# from turtle import Turtle, Screen
# turtle is the module and Turtle is the 
# thing in the module we want to import or use

# draw a dashed line

# tim = Turtle()

# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
    
    # draw a triangle, square, pentagon, hexagon, 
    # heptagon, octagon, nonagon, and decagon

# def shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(50)
#         tim.right(angle)

# for sides in range(3, 11):
#     shape(sides)


# draw a random walk

# import turtle as t
# import random


# color = ['blue', 'dark green','orange red', 'purple', 'lime', 'sky blue', 'khaki']
# directions = [0, 90, 180, 270]

# t.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b


    
# t.pensize(10)
# t.speed('fast')


# for _ in range(50):  
#     t.pencolor(random_color())
#     t.forward(20)
#     t.setheading(random.choice(directions))


# screen = Screen()
# screen.exitonclick()

# drawing a spirograph

#using random colors

import turtle as t
import random

t.colormode(255)
t.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# drawing a circle

# def draw():
#     for angle in range(0, 360, 5):
#         t.pencolor(random_color())
#         t.right(angle)
#         t.circle(100)
        
        
# draw()

def draw_spirograph(size):
    for _ in range(int(360/ size)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size)


draw_spirograph(5)      
t.exitonclick()