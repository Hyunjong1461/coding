import sys;
sys.stdin = open('input.txt','r')

t=int(input())

for tc in range(1,t+1):
    n=int(input())
    arr=[]
    for i in range(n):
        _list=list(map(int,input().split()))
        arr.append(_list)

    print(arr)
    arrpoint= [[0]*200 for _ in range(2)]

    ans=[0]*200


    while 1:
        if i==len(arr):
            break
        for j in range(len(arr[0])):
            if arr[i][j]%2==1:
                ans[arr[i][j]//2]+=1
            elif arr[i][j]%2==0:
                ans[arr[i][j]//2-1]+=1


    print(ans)


