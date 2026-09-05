def efficient_multiply(a, b, modulus):
    result = 0

    while b > 0:

        if b & 1:
            result ^= a

        b >>= 1

        a <<= 1

        if a & (1 << (modulus.bit_length() - 1)):
            a ^= modulus

    return result


a = input("Enter first polynomial in binary: ")
b = input("Enter second polynomial in binary: ")
modulus = input("Enter irreducible polynomial in binary: ")

a = int(a, 2)
b = int(b, 2)
modulus = int(modulus, 2)

result = efficient_multiply(a, b, modulus)

print("Result:", bin(result)[2:])