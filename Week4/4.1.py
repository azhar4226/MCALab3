def cal_sum_sub(num1,num2):
    sum=num1+num2
    sub=num1-num2

    return sum,sub

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))

sum, sub=cal_sum_sub(num1,num2)

print(f"SUM : {sum}\nDIFFERENCE : {sub}")