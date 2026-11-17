# ElGamal Cryptosystem

# Key Generation

p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

x = int(input("Enter private key: "))

y = pow(g, x, p)

print("\nPublic Key:", (p, g, y))
print("Private Key:", x)


# Encryption

m = int(input("\nEnter message: "))
k = int(input("Enter random key: "))

if not (1 <= x <= p - 2 and 1 <= k <= p - 2):
    print("Invalid private or random key.")

elif not (0 <= m < p):
    print("Message must be between 0 and p-1.")

else:
    c1 = pow(g, k, p)

    shared = pow(y, k, p)

    c2 = (m * shared) % p

    print("\nEncrypted Message:", (c1, c2))


    # Decryption

    shared_key = pow(c1, x, p)

    inverse = pow(shared_key, -1, p)

    decrypted = (c2 * inverse) % p

    print("Decrypted Message:", decrypted)


# Enter prime number (p): 23
# Enter primitive root (g): 6
# Enter private key: 6

# Public Key: (23, 6, 12)
# Private Key: 6

# Enter message: 10
# Enter random key: 3

# Encrypted Message: (9, 7)
# Decrypted Message: 10