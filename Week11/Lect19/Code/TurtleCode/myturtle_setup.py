# https://trinket.io/docs/python

from turtle import *

def move_forward(d):
    forward(d)

def make_forward_step(d=10):
    forward(d)    

def move_backward(d):
    backward(d)

def make_backward_step(d=10):
    backward(d)    

def rotate(a):
    if a > 0:
        right(a)
    else:
        left(-a)

def rotate_left(a):
    left(a)

def rotate_right(a):
    right(a)
        
        
def get_invisible():        
    hideturtle()
    penup()

def get_visible():        
    showturtle()
    pendown()

def get_speed():
    return speed()

def set_speed(s):
    # from 0 to 10, increasingly faster
    speed(s)
    
def slower(f):
    tracer(1,f)

def faster(f):
    tracer(f)

def stop():
    {}

def get_heading():
    return heading()

def set_heading(angle):
    setheading(angle)

def get_position():
    return position()

def set_position(x,y):
    setpos(x,y)

def set_start_position(x,y):
    tracer(0)
    get_invisible()
    setpos(x,y)
    get_visible()
    tracer(1)

# place a "dot" at the nearest integer coordinate, in order to not be too
# difficult to catch a dot
def place_dot(x,y, color):
    current_x, current_y = position()
    tracer(0)
    get_invisible()
    goto(x,y)
    dot(dot_size, color)
    goto(current_x, current_y)
    get_visible()
    tracer(1,1)
    dotsPos[(round(x), round(y))] = 1
    
def check_if_dot(x,y):
    if (round(x), round(y)) in dotsPos:
        return True
    else:
        return False
    
def eat_dot(x,y):
    dot(dot_size+1, background)
    del dotsPos[(round(x), round(y))]


def get_nearest_dot(x,y):
    min_d = width + height
    min_pos = (-1.0, -1.0)
    for pos in dotsPos:
        d = sqrt((x - pos[0])*(x - pos[0]) + (y - pos[1])*(y - pos[1]))
        if d < min_d:
            min_pos = pos
            min_d = d
    return min_pos

    
####################################


width  = 800
height = 800
startx = 0
starty = 0
background = "white"

turtle_color = "blue"

size_pen = 1

dot_size = 10

dotsPos = dict()

wn = Screen()
mc = Turtle()

# window setup: color, size, position
bgcolor(background)       
setup(width, height, startx, starty)

setworldcoordinates(0,0, width, height)

#print("W: ", window_width(), "H: ", window_height())

color(turtle_color)              # make turtle blue
pensize(size_pen)                 # set the width of pen

shape('turtle')

title("MindCraft's Turtle")

#import mymaze
