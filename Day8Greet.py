def greet():
    print("Hello")
    print("My name is Anas")
    print("Nice to meet you!")

greet()

# parameter = is the name itself
# argument = the value of the name

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name(input("what is your name? \n>"))
