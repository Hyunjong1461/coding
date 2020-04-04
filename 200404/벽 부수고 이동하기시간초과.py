from _collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

m,n=map(int,input().split())
arr=[]
for i in range(m):
    _list=list(map(int,input()))
    arr.append(_list)

cnt=1
for i in range(m):
    for j in range(n):
        if arr[i][j]==1:
            arr[i][j]=cnt
            cnt+=1

Q=deque()

minvalue=1000000
for k in range(1,cnt):
    visit = []
    visited = [[0] * n for _ in range(m)]

    Q.append((0, 0))
    visited[0][0] = 1

    while Q:
        q=Q.popleft()
        visit.append(q)
        if minvalue<visited[q[0]][q[1]]:
            break
        for i in range(4):
            nx=q[1]+dx[i]
            ny=q[0]+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[ny][nx]==0:
                    if visited[ny][nx]==0:
                        Q.append((ny,nx))
                        visited[ny][nx]=visited[q[0]][q[1]]+1

                if arr[ny][nx] == k:
                    if visited[ny][nx] == 0:
                        Q.append((ny, nx))
                        visited[ny][nx] = visited[q[0]][q[1]] + 1
    if visited[m - 1][n - 1] != 0:
        if minvalue>visited[m-1][n-1]:
            minvalue=visited[m-1][n-1]
if minvalue!=1000000:
    print(minvalue)
else:
    print(-1)