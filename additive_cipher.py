ch = input("Enter a word: ")
key = int(input("Enter key: "))
encrypt = ""
for i in ch:
    if(i.isupper()):
        val = ord(i) - ord('A')
        val = ((val + key) % 26) + ord('A')
    else:
        val = ord(i) - ord('a')
        val = ((val + key) % 26) + ord('a')
    encrypt += chr(val)
print("Encrypted word: " + encrypt)

decrypt = ""
for i in encrypt:
    if(i.isupper()):
        val = ord(i) - ord('A')
        val = ((val - key) % 26) + ord('A')
    else:
        val = ord(i) - ord('a')
        val = ((val - key) % 26) + ord('a')
    decrypt += chr(val)
print("Decrypted word: " + decrypt)