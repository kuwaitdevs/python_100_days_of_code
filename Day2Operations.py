print("My age:" + str(33))

print("addition")
print(123 + 456)

print("subtraction")
print(7 - 3)

print("division with implicit type casting")
# you always end with floating point even if the division result got no remainder
print(6 / 3)
print(type(6 / 3))

print("division to int")
print(6 // 3)
print(type(6 // 3))
# be careful with fractions
print(5 / 3)
print(5 // 3)

print("multiplication")
print(3 * 2)

print("exponents")
print(2 ** 2)
print(2 ** 3)

# order of operation
print("PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction")
# ()
# **
# * OR / (the one to the left will happen first)
# + OR - (the one to the left will happen first)
# the following line will print 7
print(3 * 3 + 3 / 3 - 3)

# to make it print 3:
print(3 * ((3 + 3) / 3) - 3)
