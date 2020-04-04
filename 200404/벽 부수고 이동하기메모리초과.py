from _collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

m,n=map(int,input().split())
arr=[]
for i in range(m):
    _list=list(map(int,input()))
    arr.append(_list)

Q=deque()

visit = []
visited = [[0] * n for _ in range(m)]
visitvisited=[]
stop=0
while 1:
    visitvisited.append(visited)
    if visited[m-1][n-1]!=0:
        print(visited[m-1][n-1])
        break
    if stop>2:
        if visitvisited[stop-1]==visitvisited[stop]:
            print(-1)
            break

    visited = [[0] * n for _ in range(m)]
    Q.append((0, 0))
    visited[0][0] = 1
    stop+=1
    flag = True

    while Q:
        q=Q.popleft()
        visit.append(q)
        if arr[q[0]][q[1]]!=0:
            flag=False
        for i in range(4):
            nx=q[1]+dx[i]
            ny=q[0]+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[ny][nx]==0:
                    if visited[ny][nx]==0:
                        Q.append((ny,nx))
                        visited[ny][nx]=visited[q[0]][q[1]]+1
                if flag==True:
                    if arr[ny][nx] == 1:
                        if visited[ny][nx] == 0:
                            arr[ny][nx]=2
                            Q.append((ny, nx))
                            visited[ny][nx] = visited[q[0]][q[1]] + 1
