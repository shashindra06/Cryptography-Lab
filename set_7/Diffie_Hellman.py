# Diffie-Hellman Key Exchange

# Public parameters
p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

# Private keys
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("\nAlice's public key:", A)
print("Bob's public key:", B)

# Shared secret calculation
key_alice = pow(B, a, p)
key_bob = pow(A, b, p)

print("\nAlice's shared secret:", key_alice)
print("Bob's shared secret:", key_bob)

if key_alice == key_bob:
    print("Key Exchange Successful!")
else:
    print("Key Exchange Failed!")


# Enter prime number (p): 23
# Enter primitive root (g): 5
# Enter Alice's private key: 6
# Enter Bob's private key: 15

# Alice's public key: 8
# Bob's public key: 19

# Alice's shared secret: 2
# Bob's shared secret: 2
# Key Exchange Successful!