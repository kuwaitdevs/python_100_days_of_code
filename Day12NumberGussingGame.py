import random

trials = 3
user_guess = -1
game_over = False
user_choice_for_difficulty = 'hard'
random_number = random.randrange(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_choice_for_difficulty = input("Chose a difficulty. Type 'easy' or 'hard':")

if user_choice_for_difficulty == 'hard':
    trials = 5
elif user_choice_for_difficulty == 'easy':
    trials = 10

while not game_over:
    print(f"You have {trials} attempts left")
    user_guess = int(input("Make a guess:\n>"))

    if user_guess == random_number:
        print(f"You won! The number was: {random_number}")
        game_over = True
        continue
    elif user_guess > random_number:
        print("Too high.\nGuess again.")
        trials -= 1
    elif user_guess < random_number:
        print("Too low.\nGuess again.")
        trials -= 1

    if trials == 0:
        game_over = True
        print(f"You ran out of attempts. Game over! The number was: {random_number}")
