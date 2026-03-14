# https://reeborg.ca/reeborg.html
# wall_in_front()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    height = 1

    turn_left()
    move()
    turn_right()

    while wall_in_front():
        height += 1
        turn_left()
        move()
        turn_right()

    move()
    turn_right()

    while height > 1:
        move()
        height -= 1
    
    turn_left()    

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()