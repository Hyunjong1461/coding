import sys;
sys.setrecursionlimit(10**6)

dr=[1,0,-1,0]
dc=[0,1,0,-1]

def dfs(r,c):
    global cnt
    arr[r][c]=2
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<n and 0<=nc<m and arr[nr][nc]==0:
            dfs(nr,nc)
            cnt+=1

m,n,k=map(int,input().split())

arr=[[0]*m for _ in range(n)]
for i in range(k):
    a,c,b,d=map(int,input().split())
    for i in range(a,b):
        for j in range(c,d):
            arr[i][j]=1

cntarr=[]
for i in range(n):
    for j in range(m):
        cnt=1
        if arr[i][j]==0:
            dfs(i,j)
            cntarr.append(cnt)
print(len(cntarr))
for i in sorted(cntarr):
    print(i,end=' ')