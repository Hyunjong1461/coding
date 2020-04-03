from _collections import deque

Q=deque()
y,x=map(int,input().split())
arr=[]
for i in range(y):
    _list=list(map(str,input()))
    arr.append(_list)

dx=[1,0,-1,0]
dy=[0,1,0,-1]
maxvalue=0
for a in range(y):
    for b in range(x):
        visit = []
        visited = [[0] * x for _ in range(y)]
        if arr[a][b]=='L':
            Q.append((a,b))
            # print(a,b)
            visited[a][b]=1
            while Q:
                q=Q.popleft()
                visit.append(q)
                for k in range(4):
                    ny=q[0]+dy[k]
                    nx=q[1]+dx[k]
                    if 0<=nx<x and 0<=ny<y:
                        if arr[ny][nx]=='L':
                            if visited[ny][nx]==0:
                                Q.append((ny,nx))
                                visited[ny][nx]=visited[q[0]][q[1]]+1
            # print(visited)
            for aa in range(y):
                for bb in range(x):
                    if maxvalue<visited[aa][bb]:
                        maxvalue=visited[aa][bb]

print(maxvalue-1)