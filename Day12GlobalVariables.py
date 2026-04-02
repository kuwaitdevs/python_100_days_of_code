enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside of the function {enemies}")

def increase_enemies_by_reference(enemies):
    return enemies + 1

increase_enemies()
print(f"enemies outside of the function {enemies}")

enemies = increase_enemies_by_reference(enemies)

print(f"enemies outside of the function {enemies}")
