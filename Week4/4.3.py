list=[1,4,6,8,11,33,44]

print(f"List : {list}")

for i in range(len(list)):
    list[i]=list[i]**2

print(f"Squared List : {list}")
