from myturtle_setup import *

#from mymaze import *

'''
set_start_position(100,100)
set_heading(90)
move_forward(50)

move_forward(30)
rotate_right(90)
move_forward(30)
rotate_left(90)
move_forward(30)
rotate_right(90)
move_forward(30)
rotate_left(90)
move_forward(30)

length = 55
angle = 80
distance = 0

move_forward(length)
distance = distance + length

rotate_right(angle)
move_forward(length)
distance = distance + length

rotate_left(angle)
move_forward(length)
distance = distance + length

rotate_right(angle)
move_forward(length)
distance = distance + length

rotate_left(angle)
move_forward(length)
distance = distance + length

print("Distance: ", distance)
write(distance, align='right')

move_forward(length)

position = get_position()
print(position)
if position == (100, 100):
    write("(100,100)")
    goto(0,0)
else:
    move_forward(10)

get_invisible()    
goto(300,300)
get_visible()

move_forward(100)
rotate_right(90)
move_forward(100)
rotate_right(90)
move_forward(100)
rotate_right(90)
'''

get_invisible()    
goto(100,100)
set_heading(90)
get_visible()

place_dot(100, 100, 'red')
place_dot(100, 300, 'red')
place_dot(300, 100, 'red')
place_dot(300, 300, 'red')

turns = 0

while turns < 4:
    move_forward(1)
    x,y = get_position()
    if check_if_dot(x,y):
        rotate_right(90)
        turns = turns + 1


'''
goto(370,0)
set_heading(90)

crossed_rooms = 0
while crossed_rooms < 3:
    while True:
        if not move_forward_if_clear(200):
            break
        
    rotate_right(90)
            
    while True:
        x,y = get_position()
        h = get_heading()
        if is_wall_left(x,y,h):
            move_forward(1)
        else:
            break
                
    move_forward(20)
    rotate_left(90)
                    
    while True:
        if not move_forward_if_clear(200):
            break
                        
    rotate_left(90)


    while True:
        x,y = get_position()
        h = get_heading()
        if is_wall_right(x,y,h):
            move_forward(1)
        else:
            break

    move_forward(20)
    rotate_right(90)

    crossed_rooms = crossed_rooms + 1

stop()
'''    
    
exitonclick()
