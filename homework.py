# Homework not assigned yet

# Since we use a new module called turtle, regular python compiler websites (like online-python.com) will not work.
# Please test your script in turtle supported online python environments, like
# "https://pythonsandbox.com/turtle"
# or "https://trinket.io/turtle"
# or "https://stepindev.com/en/py-playground"


impo
import turtle
import random

#
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0)
t.pensize(1)
t.pencolor("black")
t.fillcolor("orange")
screen.bgcolor("skyblue")
screen.setup(1000, 500)

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def five():
    t.begin_fill()
    for i in range(5):
        t.forward(100)
        t.left(215)
    t.end_fill()

for i in range(30):
    go(random.randint(-500,500),random.randint(-250,250))
    five()













