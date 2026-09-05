def add_modulo(a, b):
    return a ^ b


a = input("Enter first polynomial in binary: ")
b = input("Enter second polynomial in binary: ")

a = int(a, 2)
b = int(b, 2)

result = add_modulo(a, b)

print("Result:", bin(result)[2:])