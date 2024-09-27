import random

def randomCharacter(str):
    return random.choice(str)


str="azamgarh"
for i in range(10):
    print(f"Random characters from {str} is {randomCharacter(str)}")