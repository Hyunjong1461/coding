from _collections import deque

dx=[0,1,0,-1]
dy=[1,0,-1,0]

t= int(input())


for ii in range(t):
    m, n = map(int, input().split())
    arr=[[0]*m for _ in range(n)]
    for i in range(n):
        _str=str(input())
        for j in range(m):
            arr[i][j]=_str[j]

    Q=deque()
    visit = []
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '*':
                Q.append((i, j))
                visited[i][j] = -1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '@':
                Q.append((i, j))
                visited[i][j] = 1
    flag1=False
    for i in range(m):
        if arr[0][i] == '@':
            print(1)
            flag1 = True
        elif arr[-1][i] == '@':
            print(1)
            flag1 = True
    for j in range(1,n-1):
        if arr[j][0]== '@':
            print(1)
            flag1 = True
        elif arr[j][-1]== '@':
            print(1)
            flag1 = True

    minvalue=[]
    if flag1 ==False:
        while Q:
            q=Q.popleft()
            visit.append(q)
            for i in range(4):
                ny=q[0]+dy[i]
                nx=q[1]+dx[i]
                if 0<=nx<m and 0<=ny<n:
                    if arr[ny][nx]!='#':
                        if visited[ny][nx]==0:
                            if arr[q[0]][q[1]]=='*':
                                arr[ny][nx]='*'
                                Q.append((ny,nx))
                                visited[ny][nx]=-1

                            if arr[q[0]][q[1]]=='@':
                                if arr[ny][nx]=='.':
                                    arr[ny][nx] = '@'
                                    Q.append((ny, nx))
                                    visited[ny][nx] =visited[q[0]][q[1]]+ 1
        flag=False
        if flag == False:
            for i in range(m):
                if visited[0][i]>0:
                    minvalue.append(visited[0][i])
                    flag=True
                elif visited[-1][i]>0:
                    minvalue.append(visited[-1][i])
                    flag = True
            for j in range(1,n-1):
                if visited[j][0]>0:
                    minvalue.append(visited[j][0])
                    flag = True
                elif visited[j][-1]>0:
                    minvalue.append(visited[j][-1])
                    flag = True
        if flag == True:
            print(min(minvalue))
        if flag == False:
            print('IMPOSSIBLE')