num = int(input("Enter num: "))
for i in range (num):
    for j in range(num, 0, -1):
        # print(j, end = " ")
        print(f"{j} ", end = "")

    num = num -1
    print("\n")

5