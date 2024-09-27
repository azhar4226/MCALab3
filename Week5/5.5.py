import numpy as np

rows=int(input("Enter the number of rows : "))
cols=int(input("Enter the number of columns : "))

array=[]

print("Enter the elements row-wise (separated by spaces):")
for i in range(rows):
    elements=list(map(int, input().split()))
    array.append(elements)

np_array=np.array(array)

print("The numpy array looks like this : ")
print()
print(np_array)
print()

print("The array of odd rows and even columns is : ")

resultArray=[]

for i,row in enumerate(np_array):
    if i%2==1:
        resultArray.append(row.tolist())


transposedNumpy=np_array.T

for i,row in enumerate(transposedNumpy):
    if i%2==0:
        resultArray.append(row.tolist())


print(resultArray)
