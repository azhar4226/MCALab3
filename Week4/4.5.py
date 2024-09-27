def countOccurence(tuple,number):
    count = 0
    for x in tuple:
        if(x==number):
            count+=1

    return count

tuple=(50,10,60,70,50)
number=50

count=countOccurence(tuple,number)

print(f"{number} occurs {count} times in the {tuple}")