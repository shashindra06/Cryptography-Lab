def inverse(a):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return None


def encrypt(text, a, b):
    encrypted = ""

    for ch in text:
        if ch.isupper():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            encrypted += chr(c + ord('A'))

        elif ch.islower():
            p = ord(ch) - ord('a')
            c = (a * p + b) % 26
            encrypted += chr(c + ord('a'))

        else:
            encrypted += ch

    return encrypted


def decrypt(text, a, b):
    decrypted = ""
    inv = inverse(a)

    for ch in text:
        if ch.isupper():
            c = ord(ch) - ord('A')
            p = (inv * (c - b)) % 26
            decrypted += chr(p + ord('A'))

        elif ch.islower():
            c = ord(ch) - ord('a')
            p = (inv * (c - b)) % 26
            decrypted += chr(p + ord('a'))

        else:
            decrypted += ch

    return decrypted


text = input("Enter the Text: ")
a = int(input("Enter multiplicative key (a): "))
b = int(input("Enter additive key (b): "))

inv = inverse(a)

if inv is None:
    print("Invalid key! 'a' must be relatively prime to 26.")
else:
    encrypted = encrypt(text, a, b)
    decrypted = decrypt(encrypted, a, b)

    print("Encrypted text:", encrypted)
    print("Decrypted text:", decrypted)