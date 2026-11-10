# Fermat's Primality Test

import random

def fermat_test(n, k=5):

    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):

        a = random.randint(2, n - 2)

        if pow(a, n - 1, n) != 1:
            return False

    return True


n = int(input("Enter a number: "))

if fermat_test(n):
    print(n, "is Probably Prime")
else:
    print(n, "is Composite")