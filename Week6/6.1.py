tuple1=tuple(map(int,input("Enter elements of first tuple : ").split()))
tuple2=tuple(map(int,input("Enter elements of second tuple : ").split()))

# def combine(tuple1,tuple2):
#     list1=list(tuple1)
#     list2=list(tuple2)

#     list3=list1+list2
#     tuple3=tuple(list3)

#     return tuple3

def combine(tup1, tup2):
    tup  = tup1+tup2
    return tup

print()
print("COMBINED TUPLE : ")

# print(combine(tuple1,tuple2))
print(combine(tuple1, tuple2))

