# https://reeborg.ca/reeborg.html
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def routine():
    move()
    jump()

while not at_goal():
    routine()