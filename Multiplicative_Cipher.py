def inverse(key):

    for i in range(1, 26):
        if (key * i) % 26 == 1:
            return i

    return None


def encrypt(text, key):

    encrypted = ""

    for i in text:

        if i.isupper():
            val = ord(i) - ord('A')
            val = ((val * key) % 26) + ord('A')
            encrypted += chr(val)

        elif i.islower():
            val = ord(i) - ord('a')
            val = ((val * key) % 26) + ord('a')
            encrypted += chr(val)

        else:
            encrypted += i

    return encrypted


def decrypt(text, key):

    decrypted = ""

    inv = inverse(key)

    for i in text:

        if i.isupper():
            val = ord(i) - ord('A')
            val = ((val * inv) % 26) + ord('A')
            decrypted += chr(val)

        elif i.islower():
            val = ord(i) - ord('a')
            val = ((val * inv) % 26) + ord('a')
            decrypted += chr(val)

        else:
            decrypted += i

    return decrypted


text = input("Enter the Text: ")
key = int(input("Enter the key: "))

inv = inverse(key)

if inv is None:

    print("Invalid key! Choose a key relatively prime to 26.")

else:

    encrypted_word = encrypt(text, key)
    decrypted_word = decrypt(encrypted_word, key)

    print("Encrypted text:", encrypted_word)
    print("Decrypted text:", decrypted_word)