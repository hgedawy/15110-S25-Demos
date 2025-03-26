#https://www.101computing.net/turtle-maze/
import turtle

screen = turtle.Screen()
screen.tracer(0)

mazeWidth = 150

myMaze = turtle.Turtle()

mazeWalls = dict()

myMaze.width(5)
myMaze.hideturtle()

myMaze.speed(0)

myMaze.penup()

myMaze.goto(200, 400)


def stepwise_forward(d):
    if myMaze.isdown():
        for i in range(1,d):
            myMaze.forward(1)
            x,y = myMaze.pos()
            mazeWalls[(round(x), round(y))] = 1
    else:
        myMaze.forward(d)
        
def move_forward_if_clear(d):
    for i in range(1,d):
        turtle.forward(1)
        x,y = turtle.pos()
        #print x,y
        if (round(x), round(y)) in mazeWalls:
            #print "Wall at: ", x, "[", round(x), "]", y, "[", round(y), "]"
            turtle.backward(1)
            return False
    return True

# only works for headings parallel to coordinate axes
def is_wall_left(x, y, heading):
    if heading == 0:
        wx = round(x)
        wy = round(y)+1
    elif heading == 180:
        wx = round(x)
        wy = round(y)-1
    elif heading == 90:
        wx = round(x)-1
        wy = round(y)
    elif heading == -90 or heading == 270:
        wx = round(x)+1
        wy = round(y)
    else:
        wx = round(x)
        wy = round(y)

    if (wx, wy) in mazeWalls:
        #print "Wall at the Left"
        return True
    else:
        #print "No Wall at the Left", wx, wy, heading
        return False


# only works for headings parallel to coordinate axes
def is_wall_right(x, y, heading):
    if heading == 0:
        wx = round(x)
        wy = round(y)-1
    elif heading == 180:
        wx = round(x)
        wy = round(y)+1
    elif heading == 90:
        wx = round(x)+1
        wy = round(y)
    elif heading == -90 or heading == 270:
        wx = round(x)-1
        wy = round(y)
    else:
        wx = round(x)
        wy = round(y)

    if (wx, wy) in mazeWalls:
        #print "Wall at the Right"
        return True
    else:
        #print "No Wall at the Right", wx, wy, heading
        return False
    
    
def drawMazeSection(color):
  myMaze.color(color)
  myMaze.pendown()
  stepwise_forward(mazeWidth)
  myMaze.penup()
  stepwise_forward(40)
  myMaze.pendown()
  stepwise_forward(mazeWidth)
  myMaze.right(90)
  stepwise_forward(100)
  myMaze.right(90)
  stepwise_forward(mazeWidth)
  myMaze.penup()
  stepwise_forward(40)
  myMaze.pendown()
  stepwise_forward(mazeWidth)
  myMaze.right(90)
  stepwise_forward(100)
  myMaze.right(90)
  x,y = myMaze.pos()
  myMaze.penup()  
  myMaze.goto(x, y-50)
  myMaze.pendown()
  stepwise_forward(30)
  myMaze.penup()
  stepwise_forward(40)
  myMaze.pendown()
  stepwise_forward(200)
  myMaze.penup()
  stepwise_forward(40)
  myMaze.pendown()
  stepwise_forward(30)
  myMaze.penup()
  myMaze.goto(x,y-110)

for color in ["#FF0000","#0000FF","#00FF00"]:
  drawMazeSection(color)


screen.tracer(1)

