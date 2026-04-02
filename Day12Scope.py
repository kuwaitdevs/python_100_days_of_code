# Example 1
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside the function: {enemies}")

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()

# can't be used, outside of the scope
# print(potion_strength)


# Example 2
# Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)


## Example 3
game_level = 3
enemies_list = ['Skeleton', 'Zombie', 'Alien']

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

print(new_enemy)