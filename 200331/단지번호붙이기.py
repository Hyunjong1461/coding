dr=[1,-1,0,0]
dc=[0,0,1,-1]

def dfs(r,c):
    global cnt
    arr[r][c]=2
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<t and 0<=nc<t and arr[nr][nc]==1:
            cnt += 1
            dfs(nr,nc)


t=int(input())
visited=[[0]*t for _ in range(t)]
arr=[]
for i in range(t):
    _list=list(map(int,input()))
    arr.append(_list)
cntarr=[]
for i in range(t):
    for j in range(t):
        cnt = 1
        if arr[i][j]==1:
            dfs(i,j)
            cntarr.append(cnt)
cntarr1=sorted(cntarr)
print('{}'.format(len(cntarr)))
for i in range(len(cntarr)):
    print(cntarr1[i])