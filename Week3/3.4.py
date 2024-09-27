string=input("Enter the string : ")

print("The characters at even indexes are : ")
for index, char in enumerate(string):
    if index%2==0:
        print(char)