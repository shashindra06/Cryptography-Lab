from math import gcd


def matrix_inverse(key):
    a = key[0][0]
    b = key[0][1]
    c = key[1][0]
    d = key[1][1]

    determinant = (a * d - b * c) % 26

    if gcd(determinant, 26) != 1:
        return None

    det_inverse = None

    for i in range(26):
        if (determinant * i) % 26 == 1:
            det_inverse = i
            break

    inverse = [
        [(d * det_inverse) % 26, (-b * det_inverse) % 26],
        [(-c * det_inverse) % 26, (a * det_inverse) % 26]
    ]

    return inverse


def encrypt(text, key):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())

    if len(text) % 2 != 0:
        text += 'X'

    result = ""

    for i in range(0, len(text), 2):

        p1 = ord(text[i]) - ord('A')
        p2 = ord(text[i + 1]) - ord('A')

        c1 = (key[0][0] * p1 + key[0][1] * p2) % 26
        c2 = (key[1][0] * p1 + key[1][1] * p2) % 26

        result += chr(c1 + ord('A'))
        result += chr(c2 + ord('A'))

    return result


def decrypt(text, inverse_key):
    result = ""

    for i in range(0, len(text), 2):

        c1 = ord(text[i]) - ord('A')
        c2 = ord(text[i + 1]) - ord('A')

        p1 = (inverse_key[0][0] * c1 +
              inverse_key[0][1] * c2) % 26

        p2 = (inverse_key[1][0] * c1 +
              inverse_key[1][1] * c2) % 26

        result += chr(p1 + ord('A'))
        result += chr(p2 + ord('A'))

    return result


print("Enter the 2x2 key matrix:")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

key = [
    [a, b],
    [c, d]
]

inverse_key = matrix_inverse(key)

if inverse_key is None:

    print("Invalid key matrix!")
    print("The determinant must be relatively prime to 26.")

else:

    text = input("Enter the plaintext: ")

    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, inverse_key)

    print("Encrypted text:", encrypted)
    print("Decrypted text:", decrypted)