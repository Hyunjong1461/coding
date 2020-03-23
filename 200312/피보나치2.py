# def fib(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)



n=int(input())
a=[1,1]+[0]*(n-2)
for i in range(len(a)):
    if i >= 2:
        a[i]=a[i-1]+a[i-2]
print(a[-1])