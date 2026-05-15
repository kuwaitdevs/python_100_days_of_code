valid_age = False
age = 0

while not valid_age:
    try:
        age = int(input("How old are you?"))
        valid_age = True
    except ValueError:
        print('You have types in an invalid number, please try again with a numerical response such as 15')

if age > 18:
    print(f"You can drive at age {age}.")