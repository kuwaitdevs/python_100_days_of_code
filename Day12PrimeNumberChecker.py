def is_prime(num):
    is_devisable = False
    
    for n in range(1, num, 1):
        if num % (n + 1) == 0 and num != (n + 1):
            is_devisable = True
            break
    
    return not is_devisable

print(is_prime(1))
print(is_prime(4))
print(is_prime(7))
print(is_prime(73))
print(is_prime(75))