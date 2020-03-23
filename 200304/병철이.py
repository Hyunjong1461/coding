import sys;
sys.stdin = open('input.txt','r')


def dfs(a):
    global multi,maxvalue
    if a==size:
        if maxvalue < multi:
            maxvalue = multi
        return maxvalue
    if maxvalue>multi:
        return
    else:
        for i in range(size):
            if visit[i]:continue
            if arr[a][i]==0:continue
            visit[i]=1
            multi*=arr[a][i]*0.01
            dfs(a+1)
            visit[i] = 0
            multi /= arr[a][i]*0.01

t = int(input())
for tc in range(1,t+1):
    arr=[]
    size = int(input())
    visit = [0] * size
    multi = 1
    maxvalue=-1
    for ii in range(size):
        _list=list(map(int,input().split()))
        arr.append(_list)
    dfs(0)
    print('#{}'.format(tc),end=' ')
    print(format(maxvalue*100,".6f"))