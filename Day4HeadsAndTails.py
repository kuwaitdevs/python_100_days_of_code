import random
print("Welcome to heads and tails game!")

def prompt():    
    print("Ready to flip the coin?")
    return input("y / n ").lower()

user_answer = prompt()

while user_answer == "y":
    random_number = random.randint(0, 1)
    
    print("Coin tossed!\n")
    
    if(random_number == 1):
        print("Heads\n")
    else:
        print("Tails\n")

    user_answer = prompt()