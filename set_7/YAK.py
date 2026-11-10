# YAK Authenticated Key Exchange Protocol
# Educational implementation using Schnorr proofs

import hashlib
import random


# Public parameters
p = 23
q = 11
g = 2


def hash_value(*values):
    data = "|".join(map(str, values)).encode()
    return int(hashlib.sha256(data).hexdigest(), 16) % q


# Generate a Schnorr proof of knowledge
def prove_knowledge(secret, public, identity):

    v = random.randint(1, q - 1)
    V = pow(g, v, p)

    h = hash_value(identity, public, V)
    z = (v - secret * h) % q

    return V, z


# Verify the Schnorr proof
def verify_knowledge(public, V, z, identity):

    h = hash_value(identity, public, V)

    return pow(g, z, p) * pow(public, h, p) % p == V


# Alice and Bob's long-term private keys
a = random.randint(1, q - 1)
b = random.randint(1, q - 1)

# Their long-term public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice's public key:", A)
print("Bob's public key:", B)


# Generate ephemeral private keys
x = random.randint(1, q - 1)
y = random.randint(1, q - 1)

# Generate ephemeral public keys
X = pow(g, x, p)
Y = pow(g, y, p)

# Generate proofs of knowledge
proof_A = prove_knowledge(x, X, "Alice")
proof_B = prove_knowledge(y, Y, "Bob")

# Verify each other's proofs
valid_A = verify_knowledge(
    X, proof_A[0], proof_A[1], "Alice"
)

valid_B = verify_knowledge(
    Y, proof_B[0], proof_B[1], "Bob"
)

print("\nAlice's proof verified:", valid_A)
print("Bob's proof verified:", valid_B)

if valid_A and valid_B:

    # Compute the shared secret
    shared_A = pow((Y * B) % p, x + a, p)
    shared_B = pow((X * A) % p, y + b, p)

    # Derive session keys
    key_A = hashlib.sha256(str(shared_A).encode()).hexdigest()
    key_B = hashlib.sha256(str(shared_B).encode()).hexdigest()

    print("\nAlice's shared secret:", shared_A)
    print("Bob's shared secret:", shared_B)

    print("Alice's session key:", key_A)
    print("Bob's session key:", key_B)

    if key_A == key_B:
        print("YAK Key Exchange Successful!")
    else:
        print("Key Exchange Failed!")

else:
    print("Authentication Failed!")


# Alice's public key: 13
# Bob's public key: 16

# Alice's proof verified: True
# Bob's proof verified: True

# Alice's shared secret: 4
# Bob's shared secret: 4

# Alice's session key: <SHA-256 hash>
# Bob's session key: <same SHA-256 hash>

# YAK Key Exchange Successful!