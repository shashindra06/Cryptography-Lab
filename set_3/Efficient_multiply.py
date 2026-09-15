def efficient_multiply(a, b, modulus):

    result = 0

    # First reduce a
    while a.bit_length() >= modulus.bit_length():
        shift = a.bit_length() - modulus.bit_length()
        a = a ^ (modulus << shift)

    degree = modulus.bit_length() - 1

    while b > 0:

        if b & 1:
            result = result ^ a

        b = b >> 1

        # Check if multiplying a by x will exceed the degree
        if a & (1 << (degree - 1)):
            a = (a << 1) ^ modulus
        else:
            a = a << 1

    # Reduce result
    while result.bit_length() >= modulus.bit_length():
        shift = result.bit_length() - modulus.bit_length()
        result = result ^ (modulus << shift)

    return result


a = int(input("Enter first polynomial in binary: "), 2)
b = int(input("Enter second polynomial in binary: "), 2)
modulus = int(input("Enter irreducible polynomial in binary: "), 2)

result = efficient_multiply(a, b, modulus)

print("Result:", bin(result)[2:])