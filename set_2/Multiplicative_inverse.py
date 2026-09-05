def extended_gcd(a, b):

    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


a = int(input("Enter number: "))
p = int(input("Enter prime p: "))

gcd, x, y = extended_gcd(a, p)

if gcd != 1:

    print("Inverse does not exist.")

else:

    inverse = x % p

    print("GCD:", gcd)
    print("Multiplicative inverse:", inverse)

    print("Verification:", (a * inverse) % p)