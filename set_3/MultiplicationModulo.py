def multiply_modulo(a, b, modulus):
    result = 0

    while b > 0:

        if b & 1:
            result ^= a

        a <<= 1
        b >>= 1

    while result.bit_length() >= modulus.bit_length():

        shift = result.bit_length() - modulus.bit_length()

        result ^= modulus << shift

    return result


a = input("Enter first polynomial in binary: ")
b = input("Enter second polynomial in binary: ")
modulus = input("Enter irreducible polynomial in binary: ")

a = int(a, 2)
b = int(b, 2)
modulus = int(modulus, 2)

result = multiply_modulo(a, b, modulus)

print("Result:", bin(result)[2:])