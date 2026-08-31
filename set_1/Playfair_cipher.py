def create_matrix(key):
    key = key.upper().replace("J", "I")

    matrix_text = ""

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in matrix_text:
            matrix_text += ch

    matrix = []

    for i in range(0, 25, 5):
        matrix.append(list(matrix_text[i:i + 5]))

    return matrix


def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == ch:
                return row, col


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join(ch for ch in text if ch.isalpha())

    result = ""
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 == len(text):
            result += first + 'X'
            i += 1

        elif text[i] == text[i + 1]:
            result += first + 'X'
            i += 1

        else:
            result += first + text[i + 1]
            i += 2

    return result


def process_pair(matrix, a, b, encrypting=True):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    shift = 1 if encrypting else -1

    if row1 == row2:
        col1 = (col1 + shift) % 5
        col2 = (col2 + shift) % 5

    elif col1 == col2:
        row1 = (row1 + shift) % 5
        row2 = (row2 + shift) % 5

    else:
        col1, col2 = col2, col1

    return matrix[row1][col1] + matrix[row2][col2]


def encrypt(text, matrix):
    text = prepare_text(text)
    result = ""

    for i in range(0, len(text), 2):
        result += process_pair(matrix, text[i], text[i + 1], True)

    return result


def decrypt(text, matrix):
    result = ""

    for i in range(0, len(text), 2):
        result += process_pair(matrix, text[i], text[i + 1], False)

    return result


key = input("Enter the key: ")
text = input("Enter the plaintext: ")

matrix = create_matrix(key)

print("\nPlayfair Matrix:")

for row in matrix:
    print(" ".join(row))

encrypted = encrypt(text, matrix)
decrypted = decrypt(encrypted, matrix)

print("\nEncrypted text:", encrypted)
print("Decrypted text:", decrypted)