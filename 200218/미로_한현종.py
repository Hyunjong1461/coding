dr = [0,1,0,-1]
dc = [1,0,-1,0]


def dfs(r, c):
    global visited
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if (miro[nr][nc] == 0 or miro[nr][nc] == 3) and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(nr, nc)
T = int(input())


for tc in range(1,T+1):
    N = int(input())
    miro = [list(map(int, ''.join(input()))) for _ in range(N)]
    st_id = ()
    ed_id = ()
    visited = [[0]*N for _ in range(N)]
    for i in range(len(miro)):
        for j in range(len(miro)):
            if miro[i][j] == 2:
                st_id = (i, j)
            elif miro[i][j] == 3:
                ed_id = (i, j)
    dfs(st_id[0],st_id[1])
    result = 0
    if visited[ed_id[0]][ed_id[1]] == 1:
        result = 1
    else:
        result = 0
    print('#{} {}'.format(tc,result))