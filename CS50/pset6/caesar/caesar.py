from sys import argv
from cs50 import get_string

# take command line arguments
while len(argv) != 2:
    exit("Usage: python caesar.py k")

# convert command line argument to int
k = int(argv[1])

# take user input string
plainText = get_string("plaintext:  ")
cryptedText = ""

# encrypt
for c in plainText:
    newC = ''
    if ord('a') <= ord(c) <= ord('z'):
        newC = (ord(c) - ord('a') + k) % 26 + ord('a')
        newC = chr(newC)
    elif ord('A') <= ord(c) <= ord('Z'):
        newC = (ord(c) - ord('A') + k) % 26 + ord('A')
        newC = chr(newC)
    else:
        newC = c
    cryptedText += newC

# print encrypted text
print(f"ciphertext: {cryptedText}")

