def divisibleBy5(numbers):
    result=[]

    for n in numbers:
        if n%5==0:
            result.append(n)

    return result

numbers=[]

for i in range(20):
    n=int(input(f"Enter number {i+1} : "))
    numbers.append(n)

result=divisibleBy5(numbers)

print()
print(f"The numbers which are divisible by 5 are : {result}")