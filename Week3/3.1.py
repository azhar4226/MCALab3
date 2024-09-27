for i in range(8,0,-1):
    count=0
    for j in range(i,0,-1):
        if count%2==0:
            print('*',end=' ')
        else:
            print(j, end=' ')
        count+=1
        
    print()