# Miller-Rabin Primality Test

import random

def miller_rabin(n, k=5):

    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0:
        return False

    # Express n-1 as 2^s * d

    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    # Perform k iterations

    for i in range(k):

        a = random.randint(2, n - 2)

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for j in range(s - 1):

            x = (x * x) % n

            if x == n - 1:
                break

        else:
            return False

    return True


n = int(input("Enter a number: "))

if miller_rabin(n):
    print(n, "is Probably Prime")
else:
    print(n, "is Composite")