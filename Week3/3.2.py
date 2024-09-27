num=int(input("Enter the range :"))

for i in range(num):
    for j in range(i):
        if j==num-2:
            print('#', end='')
        else:
            print('*', end=' ')

    print()

for i in range(num-2,0,-1):
    for j in range(i):
        print('*', end=' ')

    print()  