import sys;
sys.stdin = open('input.txt','r')

t=int(input())

for tc in range(1,t+1):
    n=int(input())
    arr=[]
    for i in range(n):
        _list=list(map(int,input()))
        arr.append(_list)

    middle=n//2
    sumvalue=0
    for i in range(middle+1):
        for j in range(middle-i,middle+1+i):
            sumvalue+=arr[i][j]
    i=middle+1
    j=middle
    x=1

    while 1:
        if i==n:
            break
        else:
            for k in range(j-x,0,-1):
                sumvalue+=arr[i][j+k]
                sumvalue+=arr[i][j-k]
            sumvalue+=arr[i][j]
            i+=1
            x+=1
    print('#{} {}'.format(tc,sumvalue))

