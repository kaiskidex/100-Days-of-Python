import colorgram
import turtle as t
import random

colors = colorgram.extract("d:/VSCODE/100 Days of Python/Day18/image.jpg", 30)
t.colormode(255)
t.speed('fastest')
t.pensize(20)

color_list = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colors]

# 10 by 10 
# dots size 20 spaced by 50 

start_x = -200
start_y = -200
# set pen to the bottom left corner
t.hideturtle()
t.penup()
t.goto(start_x,start_y)
t.pendown()

for row in range(10):
    t.penup()
    t.goto(start_x, start_y + row * 50)
    for col in range(10):
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)


t.exitonclick()
