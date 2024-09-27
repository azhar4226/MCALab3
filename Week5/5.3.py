import random
import string

def passwordGenerator():
    upperCase=string.ascii_uppercase
    lowerCase=string.ascii_lowercase
    digits=string.digits
    specialChar=string.punctuation
    all=upperCase+lowerCase+digits+specialChar


    password=[random.choice(upperCase) for _ in range(2)]
    password+=[random.choice(digits) for _ in range(1)]
    password+=[random.choice(specialChar) for _ in range(1)]

    password+=random.choices(all,k=6)

    random.shuffle(password)

    return ''.join(password)

for i in range(10):
    print(f"Password {i+1} : {passwordGenerator()}")
