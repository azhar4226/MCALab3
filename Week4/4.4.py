list1=[1,2,3,4,5,6,7,8,9,10]
list2=[10,9,8,7,6,5,4,3,2,1]

size=len(list1)

for i in range(size):
    print(f"List 1 : {list1[i]} , List 2 : {list2[size-i-1]}")

print()

list3=["Saud", "Aisha", "Sana", "Zaki", "Moaz"]
list4=[1,2,3,4,5]

size2=len(list3)

for i in range(size2):
    print(f"List 1 : {list3[i]} , List 2 : {list4[size2-i-1]}")