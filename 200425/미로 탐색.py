from _collections import deque

dr=[1,-1,0,0]
dc=[0,0,1,-1]

n,m=map(int,input().split())
alist=[]
for i in range(n):
    arr=list(map(int,input()))
    alist.append(arr)

Q=deque()

visited=[[0]*m for _ in range(n)]

Q.append((0,0))

while Q:
    point=Q.popleft()
    r=point[0]
    c=point[1]
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<n and 0<=nc<m:
            if alist[nr][nc]==1:
                if visited[nr][nc]!=0:continue
                alist[r][c]=0
                Q.append((nr,nc))
                visited[nr][nc]=visited[r][c]+alist[nr][nc]
print(visited[n-1][m-1]+1)