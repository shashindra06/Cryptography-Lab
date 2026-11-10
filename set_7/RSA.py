# RSA Algorithm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


p = int(input("Enter first prime number: "))
q = int(input("Enter second prime number: "))

if not is_prime(p) or not is_prime(q) or p == q:
    print("Please enter two distinct prime numbers.")

else:
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = pow(e, -1, phi)

    print("Public Key:", (e, n))
    print("Private Key:", (d, n))

    message = int(input("Enter message (integer): "))

    if 0 <= message < n:
        encrypted = pow(message, e, n)
        decrypted = pow(encrypted, d, n)

        print("Encrypted Message:", encrypted)
        print("Decrypted Message:", decrypted)
    else:
        print("Message must be between 0 and", n - 1)


# Enter first prime number: 17
# Enter second prime number: 11
# Enter message (integer): 88


# Public Key: (3, 187)
# Private Key: (107, 187)
# Encrypted Message: 11
# Decrypted Message: 88