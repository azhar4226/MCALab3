import random

def OTP():
    otp=random.randint(100000,999999)
    return otp

for i in range(10):
    print(f"6 digit OTP : {OTP()}")