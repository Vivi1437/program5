def fibonacci(num):
    if(num==0):
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-2)+fibonacci(num-1)
num=int(input("Enter the fibonacci Number range:"))
sum=0
for n in range(num):
    print(fibonacci(n),end='')
    sum=sum+fibonacci(n)
print("\n The sum of fibonacci series numbers=%d"%sum)
