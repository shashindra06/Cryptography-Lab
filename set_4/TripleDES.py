from DES import binary_to_text, des, text_to_binary


plaintext = input("Enter 8-character plaintext: ")
key1 = input("Enter 8-character key 1: ")
key2 = input("Enter 8-character key 2: ")

p = text_to_binary(plaintext)
k1 = text_to_binary(key1)
k2 = text_to_binary(key2)

# Encrypt -> Decrypt -> Encrypt
c1 = des(p, k1)
c2 = des(c1, k2, True)
c3 = des(c2, k1)

print("Encrypted (binary):", c3)
print("Encrypted (hex):", format(int(c3, 2), '016X'))

# Decrypt -> Encrypt -> Decrypt
d1 = des(c3, k1, True)
d2 = des(d1, k2)
d3 = des(d2, k1, True)

print("Decrypted:", binary_to_text(d3))