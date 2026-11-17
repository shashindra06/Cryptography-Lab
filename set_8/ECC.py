# Elliptic Curve Cryptography (EC-ElGamal)

p = 17
a = 2
b = 2

# Base point
G = (5, 1)


# Point Addition
def point_add(P, Q):

    if P is None:
        return Q

    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        slope = ((3 * x1 * x1 + a) *
                 pow(2 * y1, -1, p)) % p
    else:
        slope = ((y2 - y1) *
                 pow(x2 - x1, -1, p)) % p

    x3 = (slope * slope - x1 - x2) % p

    y3 = (slope * (x1 - x3) - y1) % p

    return (x3, y3)


# Point Multiplication
def point_multiply(k, P):

    result = None

    while k > 0:

        if k % 2 == 1:
            result = point_add(result, P)

        P = point_add(P, P)

        k //= 2

    return result


# Key Generation

private_key = int(input("Enter private key: "))

if not (1 <= private_key <= 18):
    print("Private key must be between 1 and 18.")

else:
    public_key = point_multiply(private_key, G)

    print("\nPublic Key:", public_key)


    # Encryption

    message = int(input("\nEnter message (1-18): "))
    k = int(input("Enter random key (1-18): "))

    if not (1 <= message <= 18 and 1 <= k <= 18):
        print("Invalid message or random key.")

    else:
        # Encode message as a point
        M = point_multiply(message, G)

        # First ciphertext point
        C1 = point_multiply(k, G)

        # Second ciphertext point
        C2 = point_add(
            M,
            point_multiply(k, public_key)
        )

        print("\nEncrypted Message:", (C1, C2))


        # Decryption

        shared = point_multiply(private_key, C1)

        negative_shared = (shared[0], (-shared[1]) % p)

        decrypted_point = point_add(C2, negative_shared)

        # Decode message point
        decrypted_message = None

        for i in range(1, 19):

            if point_multiply(i, G) == decrypted_point:
                decrypted_message = i
                break

        print("Decrypted Point:", decrypted_point)
        print("Decrypted Message:", decrypted_message)


# Enter private key: 7

# Public Key: (0, 6)

# Enter message (1-18): 4
# Enter random key (1-18): 3

# Encrypted Message: ((10, 6), (16, 13))
# Decrypted Point: (3, 1)
# Decrypted Message: 4