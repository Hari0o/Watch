def fib(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return ((i-1)+(i-2))
n=int(input())
for lo in range(5,n):
    print(fib(lo),end=',')