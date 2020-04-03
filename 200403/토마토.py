from _collections import deque

dr=[1,0,-1,0]
dc=[0,-1,0,1]

Q=deque()
m,n=map(int,input().split())
arr=[]
for i in range(n):
    _list=list(map(int,input().split()))
    arr.append(_list)

visit=[]
visited=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            Q.append((i,j))
            visited[i][j] = 1


while Q:
    q=Q.popleft()
    visit.append(q)
    i=q[0]
    j=q[1]
    for dir in range(4):
        ni=i+dr[dir]
        nj=j+dc[dir]
        if 0<=ni<n and 0<=nj<m:
            if arr[ni][nj]==0:
                arr[ni][nj] = 1
                Q.append((ni,nj))
                visited[ni][nj]=visited[i][j]+1
maxvalue=-10
for i in range(n):
    for j in range(m):
        if arr[i][j]==-1:
            visited[i][j]=-1
        if visited[i][j]>maxvalue:
            maxvalue=visited[i][j]

flag=True
for i in range(n):
    for j in range(m):
        if visited[i][j]==0:
            flag=False
            break

if flag==True:
    print('{}'.format(maxvalue-1))
elif flag==False:
    print(-1)