# RC4 Stream Cipher Implementation

def rc4(key, plaintext):

    # Step 1: Initialize the state array
    S = list(range(256))

    # Step 2: Key Scheduling Algorithm (KSA)
    j = 0
    key_length = len(key)

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256

        S[i], S[j] = S[j], S[i]

    # Step 3: Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0

    result = []

    for byte in plaintext:

        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        t = (S[i] + S[j]) % 256

        k = S[t]

        result.append(byte ^ k)

    return bytes(result)


# Main program

key = input("Enter key: ").encode()
plaintext = input("Enter plaintext: ").encode()

# Encryption
encrypted = rc4(key, plaintext)

print("Encrypted (Hex):", encrypted.hex().upper())

# Decryption
decrypted = rc4(key, encrypted)

print("Decrypted:", decrypted.decode())

# Enter key: key
# Enter plaintext: Plaintext
# Encrypted (Hex): 5B0055844AFB1E323C
# Decrypted: Plaintext