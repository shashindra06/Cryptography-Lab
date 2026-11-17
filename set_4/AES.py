from Crypto.Cipher import AES

key = input("Enter 16-character key: ").encode()
plaintext = input("Enter 16-character plaintext: ").encode()

cipher = AES.new(key, AES.MODE_ECB)

encrypted = cipher.encrypt(plaintext)

print("Encrypted:", encrypted.hex())

decipher = AES.new(key, AES.MODE_ECB)

decrypted = decipher.decrypt(encrypted)

print("Decrypted:", decrypted.decode())

# Input
# Enter 8-character plaintext: ABCDEFGH
# Enter 8-character key: 12345678
# Output
# Encrypted (hex): 96DE603EAED6256F
# Decrypted: ABCDEFGH
