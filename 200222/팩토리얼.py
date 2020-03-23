def factorial(a,n):
    flag=0
    global fac
    global i
    if a==n:
        flag=1
        if flag ==1:
            print(fac)
    else:
        fac *= i
        i=i+1
        factorial(a+1,n)
        if flag==1:
            return


t=int(input())
fac=1
i=1
factorial(0,t)