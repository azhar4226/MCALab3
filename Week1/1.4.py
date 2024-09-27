def isPalindrome(number):
    original=number
    reverse=0

    while original>0:
        remainder=original%10
        reverse=reverse*10+remainder
        original=original//10


    return number==reverse

def isPalindrome2(number):
    return str(number) == str(number)[::-1]


number=int(input("Enter the number : "))

if(isPalindrome2(number)) :
    print("Palindrome number")

else :
    print("Not a palindrome number")