phoneDictionary={}

phoneDictionary['Azhar']='7770099911'
phoneDictionary['Saif']='1222333344'
phoneDictionary['Arsalan']='44444444444'


name=input("Enter a name to get the phone number : ")

if name in phoneDictionary:
    print(f"The phone number of {name} is {phoneDictionary[name]}")

else :
    print(f"The data for {name} is not available")

