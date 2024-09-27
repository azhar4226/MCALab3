def checkFirstLast(list):
    if not list:
        return False
    
    return list[0]==list[-1]
# list[0]==list[len(list)-1]

list=[]

print("Enter the numbers in the list (enter -1 as last element): ")

i=1
while True:
    num = int(input(f"Enter number {i} : "))
    if num==-1:
        break

    list.append(num)
    i+=1

print()

if(checkFirstLast(list)):
    print("The first and last element are the same.")

else:
    print("The first and last element are not same.")