from myturtle_start import *

from mymaze import *

move_forward(50)
rotate(120)
move_forward(50)

goto(0,0)
goto(100,100)

pos = position()
print(pos)

angle = heading()
print(angle)

#move_backward(200)


#slower(50)
speed = get_speed()
print("Speed: ", speed)

set_speed(5)

circle(50)

fillcolor('yellow')
begin_fill()
move_forward(100)
rotate(90)
move_forward(100)
rotate(90)
move_forward(100)
rotate(90)
move_forward(100)
end_fill()

get_invisible()
goto(150,150)
get_visible()

angle = heading()
direction = towards(0,0)
print(direction, angle )

msg = "At position" + str(position())
write(msg,  font=('Arial', 8, 'normal'))

move_forward_if_clear(200)

place_dot(50, 50, 'red')
place_dot(50, 300, 'red')

move_backward(200)

goto(50,50)
x,y = position()
if check_if_dot(x,y):
    print("Found a dot at: ", x,y)
    #eat_dot(x,y)
else:
    print("No dots! :-(")

goto(10,200)

nearest_dot = get_nearest_dot(10,300)
print("Nearest dot: ", nearest_dot)

goto(nearest_dot[0], nearest_dot[1])


exitonclick()      

