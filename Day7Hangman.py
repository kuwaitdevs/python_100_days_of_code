import random
# Hangman

words_list = ['hallucination', 'lucid dream', 'procrastination', 'banana', 'apple', 'orange']

word_to_guess = random.choice(words_list)

word_length = len(word_to_guess)

# Game loop
trials = 6
game_won = False

shadow_word = []
unique_letters = []
letters_guessed = []

# create shadow word
for char in word_to_guess:

    if char == " ":
        shadow_word.append(" ")
    else:
        shadow_word.append("_")

        if unique_letters.count(char) == 0 and char != " ":
            unique_letters.append(char)
        

def print_hang_man(number_of_trials):
    if number_of_trials == 6:
        print('''
   ______
        |
        |
        |
        |      
---------''')
    elif number_of_trials == 5:
        print('''
   ______
  |     |
  o     |
        |
        |      
---------''')
    elif number_of_trials == 4:
        print('''
   ______
  |     |
  o     |
  |     |
        |      
---------''')
    elif number_of_trials == 3:
        print('''
   ______
  |     |
  o     |
/ |     |
        |      
---------''')
    elif number_of_trials == 2:
        print('''
   ______
  |     |
  o     |
/ | \\  |
        |      
---------''')
    elif number_of_trials == 1:
        print('''
   ______
  |     |
  o     |
/ | \\  |
  /     |      
---------''')
    elif number_of_trials == 0:
        print('''
   ______
  |     |
  o     |
/ | \\   |
  /\     |      
---------''')


while not game_won and trials > 0:

    print_hang_man(trials)
    print("Trials: ", trials)

    print("Word to Guess: ", "".join(shadow_word))
    user_letter = str.lower(input("Guess a letter: "))

    if letters_guessed.count(user_letter) > 0:
        print("Letter already guessed, use another letter")
        continue;

    letter_found = False

    for index, char in enumerate(word_to_guess):
        if user_letter != ' ' and user_letter == char:
            letter_found = True

            # reveal the character
            shadow_word[index] = char

            # updated guessed characters
            if letters_guessed.count(user_letter) == 0:
                letters_guessed.append(user_letter)
        
    if not letter_found:
        trials -= 1 
    
    if len(letters_guessed) == len(unique_letters):
        game_won = True
    

if game_won:
    print("You Won! The word is: ", "".join(shadow_word))
else:
    print_hang_man(trials)
    print("You lost! try again.")

