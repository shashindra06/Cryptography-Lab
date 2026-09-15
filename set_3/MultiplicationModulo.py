def multiply_modulo(a, b, modulus):

    result = 0

    # Polynomial multiplication
    while b > 0:

        if b & 1:
            result = result ^ a

        a = a << 1
        b = b >> 1

    # Polynomial modulo reduction
    while result.bit_length() >= modulus.bit_length():

        shift = result.bit_length() - modulus.bit_length()

        result = result ^ (modulus << shift)

    return result


a = int(input("Enter first polynomial in binary: "), 2)
b = int(input("Enter second polynomial in binary: "), 2)
modulus = int(input("Enter irreducible polynomial in binary: "), 2)

result = multiply_modulo(a, b, modulus)

print("Result:", bin(result)[2:])