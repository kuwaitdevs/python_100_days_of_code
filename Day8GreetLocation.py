def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What is it like in your {location}?")

name = input("What is your name? \n>")
location = input("Where do you live? \n>")

greet_with_name(name, location)

greet_with_name(location=location, name=name)
