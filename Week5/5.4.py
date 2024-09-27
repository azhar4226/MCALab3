import random

def thirdList(list1,list2):
    list=[]

    for x in list1:
        if x%2!=0:
            list.append(x)

    for x in list2:
        if x%2==0:
            list.append(x)

    random.shuffle(list)

    return list

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[11,12,13,14,15,16,17,18,19,20]

list=thirdList(list1,list2)

print(list)