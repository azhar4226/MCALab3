import random
from string import punctuation


def encrypt(string):
    res_str = ""
    for c in string:
        res_str+=c
        res_str+=random.choice(punctuation)
    return res_str


def decrypt(string):
    l = len(string)
    res_str = ""
    for i in range(0,l,2):
       res_str+=string[i]
    return res_str


Str = input("Enter the String: ")

print("Input String: "+Str)
encrypted = encrypt(Str)
print("Encrypted String: "+encrypted)
print("Decrypted String: "+decrypt(encrypted))
