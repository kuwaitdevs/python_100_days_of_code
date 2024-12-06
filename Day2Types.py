# type checking
print(type("hello"))

print(type(123))

print(type(123.456))

print(type(True))

# type casting / conversion
print(123)
print("123")
print("123" + "456")
print(int("123") + int("456"))

# conversion does not work on all data types
# print(int("abc"))
# int()
# str()
# float()
# bool()

name = input("enter your name: ")
# you can't concatenate string to number
# print("number of letters in your name: " + len(name))
# correct way
name_length = len(name)
print(type(name_length))
print("number of letters in your name: " + str(name_length))
