import sys;
sys.stdin = open('input.txt','r')

t=int(input())

for tc in range(1,t+1):
    n=int(input())
    arr=[]
    for i in range(n):
        _list=list(map(int,input()))
        arr.append(_list)
    num = len(arr)
    middlepoint=num//2
    ans=0
    arr2=[0]*(num)
    i = 1
    for x in range(num):
        if 2*x+1<=num:
            arr2[x]=2*x+1
        else:
            arr2[x]=arr2[middlepoint-i]
            i+=1
    for i in range(num):

        for k in range(middlepoint-arr2[i]//2,middlepoint+arr2[i]//2+1):
            ans+=arr[i][k]
    print('#{} {}'.format(tc,ans))